from __future__ import annotations
from pathlib import Path
import subprocess
import numpy as np
import csv

# ngspice 実行ファイルへのパス
NGSPICE_EXE = r"C:\Program Files\Spice64\bin\ngspice_con.exe"

# Template 読み込み
TEMPLATE = Path("templates/template_vdid.cir").read_text(encoding="utf-8")

# 温度テーブル
TEMP_TABLE = {
    "LT": -40.0,
    "RT": 25.0,
    "HT": 125.0,
}


# --------------------------
#   Id_lin / Id_sat 抽出
# --------------------------
def compute_Id_params(Vds: np.ndarray, Id: np.ndarray, device: str):
    """
    Vds–Id カーブから Id_lin, Id_sat を抽出する。
    """

    if device == "nmos":
        lin_range = (0.05, 0.10)   # NMOS
        sat_range = (0.50, 0.60)
    else:
        lin_range = (-0.10, -0.05)  # PMOS（Vdsは負方向）
        sat_range = (-0.60, -0.50)

    # Linear
    idx_lin = np.where((Vds >= lin_range[0]) & (Vds <= lin_range[1]))[0]
    Id_lin = float(np.mean(Id[idx_lin])) if len(idx_lin) > 0 else np.nan

    # Saturation
    idx_sat = np.where((Vds >= sat_range[0]) & (Vds <= sat_range[1]))[0]
    Id_sat = float(np.mean(Id[idx_sat])) if len(idx_sat) > 0 else np.nan

    return Id_lin, Id_sat


# --------------------------
#   VDID 実行
# --------------------------
def run_vdid(
    tech: str,
    device: str,
    temp_tag: str,
    temp: float,
    model_include: str,
    model_name: str,
    Lch: float,
    Wch: float,
    vg_bias: float,
    vdd: float,
    raw_dir: Path,
):
    """
    指定条件で VDID（Vds–Id掃引）を実行し、
    .cir / .dat / .csv / .log を出力する。
    """

    raw_dir.mkdir(parents=True, exist_ok=True)

    # -------- Drain 掃引設定 --------
    if device == "nmos":
        S_volt = 0.0
        B_volt = 0.0
        VD_START = 0.0
        VD_STOP = vdd
        VD_STEP = 0.05
    else:
        S_volt = vdd
        B_volt = vdd
        VD_START = 0.0
        VD_STOP = -vdd
        VD_STEP = -0.05

    # -------- ファイル名 --------
    cir_path = raw_dir / f"{tech}_{device}_vdid_{temp_tag}.cir"
    dat_path = raw_dir / f"{tech}_{device}_vdid_{temp_tag}.dat"
    csv_path = raw_dir / f"{tech}_{device}_vdid_{temp_tag}.csv"
    log_path = raw_dir / f"{tech}_{device}_vdid_{temp_tag}.log"
    bsim_path = raw_dir / f"{tech}_{device}_vdid_{temp_tag}_bsim4.out"

    # -------- テンプレート展開 --------
    txt = (
        TEMPLATE
        .replace("{{MODEL_INCLUDE}}", f'.include "{model_include}"')
        .replace("{{MODEL_NAME}}", model_name)
        .replace("{{LCH}}", str(Lch))
        .replace("{{WCH}}", str(Wch))
        .replace("{{VG_BIAS}}", str(vg_bias))
        .replace("{{TEMP}}", str(temp))
        .replace("{{S_VOLT}}", f"{float(S_volt)}")
        .replace("{{B_VOLT}}", f"{float(B_volt)}")
        .replace("{{VD_START}}", str(VD_START))
        .replace("{{VD_STOP}}", str(VD_STOP))
        .replace("{{VD_STEP}}", str(VD_STEP))
        .replace("{{DAT_PATH}}", str(dat_path).replace("\\", "/"))
    )
    cir_path.write_text(txt, encoding="utf-8")

    # -------- ngspice 実行 --------
    print(f"[VDID] Running ngspice → {cir_path}")
    subprocess.run(
        [NGSPICE_EXE, "-b", str(cir_path)],
        stdout=open(log_path, "w", encoding="utf-8"),
        stderr=subprocess.STDOUT,
    )

    if not dat_path.exists():
        raise RuntimeError(f"ERROR: .dat not generated → {dat_path}")

    # -------- .dat 読込 (Vds, Id) --------
    data = np.loadtxt(dat_path)
    if data.ndim == 1:
        data = data.reshape(1, -1)

    Vds = data[:, 0]
    Id = data[:, 3]

    # -------- ★ 抽出パラメータ計算 --------
    Id_lin, Id_sat = compute_Id_params(Vds, Id, device)

    # -------- ★ CSV（パラメータだけ） --------
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Id_lin[A]", "Id_sat[A]"])
        writer.writerow([f"{Id_lin:.5e}", f"{Id_sat:.5e}"])

    print(f"[saved] {csv_path}")

    return {
        "dat": dat_path,
        "csv": csv_path,
        "cir": cir_path,
        "log": log_path,
        "bsim4": bsim_path,
    }


# --------------------------
#   130nm 全温度・全デバイス
# --------------------------
def run_all_130nm(vgs_mag: float = 1.2, vdd: float = 1.2):
    base_dir = Path("results/130nm/vdid")
    results = []

    for device in ("nmos", "pmos"):

        if device == "nmos":
            model = Path("models/nmos130.sp").resolve()
            model_name = "nmos130"
            vg = +vgs_mag
        else:
            model = Path("models/pmos130.sp").resolve()
            model_name = "pmos130"
            vg = -vgs_mag

        for tag, temp in TEMP_TABLE.items():
            out = run_vdid(
                tech="130nm",
                device=device,
                temp_tag=tag,
                temp=temp,
                model_include=str(model),
                model_name=model_name,
                Lch=0.13e-6,
                Wch=1e-6,
                vg_bias=vg,
                vdd=vdd,
                raw_dir=base_dir,
            )
            results.append(out)

    return results


# --------------------------
#   main
# --------------------------
if __name__ == "__main__":
    outs = run_all_130nm()
    for o in outs:
        print(o)

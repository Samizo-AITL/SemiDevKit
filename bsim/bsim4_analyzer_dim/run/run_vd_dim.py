from __future__ import annotations
from pathlib import Path
import subprocess
import numpy as np
import csv

# ============================================================
# 設定
# ============================================================

NGSPICE_EXE = r"C:\Program Files\Spice64\bin\ngspice_con.exe"

TECH = "130nm"
TEMP_RT = 25.0
VDD = 1.2

# Lスイープ [m]
L_LIST = [
    0.10e-6,
    0.13e-6,
    0.16e-6,
    0.20e-6,
    0.50e-6,
    1.00e-6,
]
W_FIXED_FOR_L = 1.0e-6

# Wスイープ [m]（0.5,1.0,10um の 3水準）
W_LIST = [
    0.50e-6,
    1.00e-6,
    10.0e-6,
]
L_FIXED_FOR_W = 0.13e-6

# Id–Vd sweep range
VD_START = 0.0
VD_STOP  = 1.2
VD_STEP  = 0.02


# ============================================================
# ngspice 実行
# ============================================================

def run_ngspice(cir_path: Path, log_path: Path, out_dir: Path):
    print(f"[VD] Running ngspice → {cir_path}")

    result = subprocess.run(
        [NGSPICE_EXE, "-b", str(cir_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    log_path.write_text(result.stdout, encoding="utf-8")

    tmp_bsim = out_dir / "bsim4.out"
    tmp_simlog = out_dir / "sim.log"
    if tmp_bsim.exists():
        tmp_bsim.rename(out_dir / (cir_path.stem + "_bsim4.out"))
    if tmp_simlog.exists():
        tmp_simlog.rename(log_path)

    if result.returncode != 0:
        raise RuntimeError(f"ngspice failed: {cir_path}")


# ============================================================
# VD パラメータ抽出
# ============================================================

def extract_params(dat_path: Path, csv_path: Path):
    """Id–Vd カーブから Id_lin / Id_sat / Vdsat_approx を抽出"""

    data = np.loadtxt(dat_path)
    if data.ndim == 1:
        data = data.reshape(1, -1)

    # Vds は 1列目（Vd）、Id は最後の列（4列目）を読む
    Vds = data[:, 0]
    Id  = data[:, -1]

    # gm = d(Id)/d(Vds)
    gm = np.gradient(Id, Vds)
    idx_knee = int(np.nanargmax(np.abs(gm)))
    Vdsat_approx = float(Vds[idx_knee])

    # Id_lin（低 Vds = 0.1V付近）
    V_LIN_TARGET = 0.1
    idx_lin = int(np.argmin(np.abs(Vds - V_LIN_TARGET)))
    Id_lin = float(Id[idx_lin])

    # Id_sat（終端平均）
    if len(Id) >= 5:
        Id_sat = float(np.mean(Id[-5:]))
    else:
        Id_sat = float(Id[-1])

    rows = [
        ["param", "value"],
        ["Id_lin", Id_lin],
        ["Id_sat", Id_sat],
        ["Vdsat_approx", Vdsat_approx],
    ]

    with open(csv_path, "w", newline="") as f:
        csv.writer(f).writerows(rows)


# ============================================================
# テンプレート展開
# ============================================================

def make_vd_cir(
    template_path: Path,
    model_include: str,
    model_name: str,
    Lch: float,
    Wch: float,
    device: str,
    dat_path: Path,
):
    tpl = template_path.read_text(encoding="utf-8")
    include_str = model_include.replace("\\", "/")

    # ★ SCEが見えやすいように Vgs バイアスは Vth+α 程度に設定
    if device == "nmos":
        S_VOLT = 0.0
        B_VOLT = 0.0
        VG_BIAS = 1.2
        VD_START_, VD_STOP_, VD_STEP_ = VD_START, VD_STOP, VD_STEP
    else:
        S_VOLT = VDD
        B_VOLT = VDD
        VG_BIAS = -1.2
        VD_START_, VD_STOP_, VD_STEP_ = 0.0, -VD_STOP, -VD_STEP

    cir = (
        tpl.replace("{{MODEL_INCLUDE}}", f'.include "{include_str}"')
           .replace("{{MODEL_NAME}}", model_name)
           .replace("{{TEMP}}", str(TEMP_RT))
           .replace("{{LCH}}", str(Lch))
           .replace("{{WCH}}", str(Wch))
           .replace("{{S_VOLT}}", str(S_VOLT))
           .replace("{{B_VOLT}}", str(B_VOLT))
           .replace("{{VG_BIAS}}", str(VG_BIAS))
           .replace("{{VD_START}}", str(VD_START_))
           .replace("{{VD_STOP}}", str(VD_STOP_))
           .replace("{{VD_STEP}}", str(VD_STEP_))
           .replace("{{DAT_PATH}}", dat_path.as_posix())
    )
    return cir


# ============================================================
# L スイープ（L別モデル読む版）
#   ★ ファイル名を 130nm_nmos_l010.sp 形式に合わせて修正
# ============================================================

def sweep_L_vd():
    base = Path(".")
    template_path = base / "templates" / "template_vd_dim.cir"
    out_dir = base / "results" / TECH / "l_vd"
    out_dir.mkdir(parents=True, exist_ok=True)

    for device in ["nmos", "pmos"]:
        for Lch in L_LIST:
            Wch = W_FIXED_FOR_L

            # L[um] を 0.01um単位 3桁コードに変換 (0.10→010, 1.00→100)
            Lum = Lch * 1e6
            lcode = int(round(Lum * 100))
            lcode_str = f"{lcode:03d}"

            # 実ファイル名に合わせる
            model_path = base / "models" / f"130nm_{device}_l{lcode_str}.sp"
            model_name = f"130nm_{device}_l{lcode_str}"

            stem = f"{TECH}_{device}_L{lcode_str}_vd"

            cir_path = out_dir / f"{stem}.cir"
            dat_path = out_dir / f"{stem}.dat"
            log_path = out_dir / f"{stem}.log"
            csv_path = out_dir / f"{stem}.csv"

            cir_text = make_vd_cir(
                template_path,
                str(model_path.resolve()),
                model_name,
                Lch,
                Wch,
                device,
                dat_path,
            )
            cir_path.write_text(cir_text, encoding="utf-8")

            run_ngspice(cir_path, log_path, out_dir)
            extract_params(dat_path, csv_path)


# ============================================================
# W スイープ（W別モデル読む版）
#   ★ こちらも 130nm_nmos_w050.sp 形式に合わせて修正
# ============================================================

def sweep_W_vd():
    base = Path(".")
    template_path = base / "templates" / "template_vd_dim.cir"
    out_dir = base / "results" / TECH / "w_vd"
    out_dir.mkdir(parents=True, exist_ok=True)

    for device in ["nmos", "pmos"]:
        for Wch in W_LIST:

            Lch = L_FIXED_FOR_W

            # W[um] → 0.01um単位コード（0.5→050, 10→1000）
            Wum = Wch * 1e6
            wcode = int(round(Wum * 100))
            wcode_str = f"{wcode:03d}"   # 050,100,1000

            # 実ファイル名に合わせる
            model_path = base / "models" / f"130nm_{device}_w{wcode_str}.sp"
            model_name = f"130nm_{device}_w{wcode_str}"

            stem = f"{TECH}_{device}_W{wcode_str}_vd"

            cir_path = out_dir / f"{stem}.cir"
            dat_path = out_dir / f"{stem}.dat"
            log_path = out_dir / f"{stem}.log"
            csv_path = out_dir / f"{stem}.csv"

            cir_text = make_vd_cir(
                template_path,
                str(model_path.resolve()),
                model_name,
                Lch,
                Wch,
                device,
                dat_path,
            )
            cir_path.write_text(cir_text, encoding="utf-8")

            run_ngspice(cir_path, log_path, out_dir)
            extract_params(dat_path, csv_path)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("===== VD Sweep : L-sweep (RT, 130nm) =====")
    sweep_L_vd()

    print("===== VD Sweep : W-sweep (RT, 130nm) =====")
    sweep_W_vd()

    print("=== run_vd_dim.py DONE ===")

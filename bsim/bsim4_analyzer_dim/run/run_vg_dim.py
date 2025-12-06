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
VG_STEP = 0.01

# L sweep
L_LIST = [
    0.10e-6,
    0.13e-6,
    0.16e-6,
    0.20e-6,
    0.50e-6,
    1.00e-6,
]
W_FIXED_FOR_L = 1.0e-6

# W sweep
W_LIST = [
    0.50e-6,
    1.00e-6,
    10.0e-6,
]
L_FIXED_FOR_W = 0.13e-6


# ============================================================
# ngspice 実行
# ============================================================

def run_ngspice(cir_path: Path, log_path: Path, out_dir: Path):
    print(f"[VG] Running ngspice → {cir_path}")

    result = subprocess.run(
        [NGSPICE_EXE, "-b", str(cir_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    # ログ保存
    log_path.write_text(result.stdout, encoding="utf-8")

    # bsim4.out / sim.log の整理
    tmp_bsim = out_dir / "bsim4.out"
    tmp_simlog = out_dir / "sim.log"
    if tmp_bsim.exists():
        tmp_bsim.rename(out_dir / (cir_path.stem + "_bsim4.out"))
    if tmp_simlog.exists():
        tmp_simlog.rename(log_path)

    if result.returncode != 0:
        raise RuntimeError(f"ngspice failed: {cir_path}")


# ============================================================
# Vth(gmmax) 抽出
# ============================================================

def extract_vth(dat_path: Path, csv_path: Path):
    data = np.loadtxt(dat_path)
    if data.ndim == 1:
        data = data.reshape(1, -1)

    # Vgs = 先頭列, Id = 最終列（2列でも4列でも対応）
    Vgs = data[:, 0]
    Id  = data[:, -1]

    gm = np.gradient(Id, Vgs)

    n = len(Vgs)
    i_start = int(n * 0.1)
    i_end   = int(n * 0.9)
    if i_end <= i_start:
        i_start, i_end = 0, n

    gm_window = gm[i_start:i_end]
    idx_local = int(np.nanargmax(np.abs(gm_window)))
    idx = i_start + idx_local

    gmmax = float(gm[idx])
    Vth   = float(Vgs[idx])

    rows = [
        ["param", "value"],
        ["Vth_gmmax", Vth],
        ["gmmax", gmmax],
    ]

    with open(csv_path, "w", newline="") as f:
        csv.writer(f).writerows(rows)


# ============================================================
# 回路テンプレート生成
# ============================================================

def make_vg_cir(
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

    if device == "nmos":
        D_VOLT = 0.05
        S_VOLT = 0.0
        B_VOLT = 0.0
        VG_START, VG_STOP, VG_STEP_ = 0.0, VDD, VG_STEP
    else:
        S_VOLT = VDD
        D_VOLT = VDD - 0.05
        B_VOLT = VDD
        VG_START, VG_STOP, VG_STEP_ = 0.0, -VDD, -VG_STEP

    cir = (
        tpl.replace("{{MODEL_INCLUDE}}", f'.include "{include_str}"')
           .replace("{{MODEL_NAME}}", model_name)
           .replace("{{TEMP}}", str(TEMP_RT))
           .replace("{{LCH}}", str(Lch))
           .replace("{{WCH}}", str(Wch))
           .replace("{{D_VOLT}}", str(D_VOLT))
           .replace("{{S_VOLT}}", str(S_VOLT))
           .replace("{{B_VOLT}}", str(B_VOLT))
           .replace("{{VG_START}}", str(VG_START))
           .replace("{{VG_STOP}}", str(VG_STOP))
           .replace("{{VG_STEP}}", str(VG_STEP_))
           .replace("{{CSV_PATH}}", dat_path.as_posix())
    )
    return cir


# ============================================================
# L スイープ
#   130nm_nmos_l010.sp / 130nm_pmos_l010.sp などを読む
# ============================================================

def sweep_L_vg():
    base = Path(".")
    template_path = base / "templates" / "template_vg_dim.cir"
    out_dir = base / "results" / TECH / "l_vg"
    out_dir.mkdir(parents=True, exist_ok=True)

    for device in ["nmos", "pmos"]:
        for Lch in L_LIST:

            Wch = W_FIXED_FOR_L

            Lum = Lch * 1e6
            code = int(round(Lum * 100))    # 0.10→10, 1.00→100
            code_str = f"{code:03d}"        # 010,013,...

            # 実ファイル名と一致させる
            model_path = base / "models" / f"{TECH}_{device}_l{code_str}.sp"
            model_name = f"{TECH}_{device}_l{code_str}"

            stem = f"{TECH}_{device}_L{code_str}_vg"

            cir_path = out_dir / f"{stem}.cir"
            dat_path = out_dir / f"{stem}.dat"
            log_path = out_dir / f"{stem}.log"
            csv_path = out_dir / f"{stem}.csv"

            cir_text = make_vg_cir(
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
            extract_vth(dat_path, csv_path)


# ============================================================
# W スイープ
#   130nm_nmos_w050.sp / 130nm_pmos_w050.sp などを読む
# ============================================================

def sweep_W_vg():
    base = Path(".")
    template_path = base / "templates" / "template_vg_dim.cir"
    out_dir = base / "results" / TECH / "w_vg"
    out_dir.mkdir(parents=True, exist_ok=True)

    for device in ["nmos", "pmos"]:
        for Wch in W_LIST:

            Lch = L_FIXED_FOR_W

            Wum = Wch * 1e6
            code = int(round(Wum * 100))   # 0.5→50, 10→1000
            code_str = f"{code:03d}"

            model_path = base / "models" / f"{TECH}_{device}_w{code_str}.sp"
            model_name = f"{TECH}_{device}_w{code_str}"

            stem = f"{TECH}_{device}_W{code_str}_vg"

            cir_path = out_dir / f"{stem}.cir"
            dat_path = out_dir / f"{stem}.dat"
            log_path = out_dir / f"{stem}.log"
            csv_path = out_dir / f"{stem}.csv"

            cir_text = make_vg_cir(
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
            extract_vth(dat_path, csv_path)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("===== VG Sweep : L-sweep (RT, 130nm) =====")
    sweep_L_vg()

    print("===== VG Sweep : W-sweep (RT, 130nm) =====")
    sweep_W_vg()

    print("=== run_vg_dim.py DONE ===")

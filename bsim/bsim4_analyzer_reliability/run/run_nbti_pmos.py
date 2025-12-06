from __future__ import annotations
from pathlib import Path
import subprocess
import numpy as np
import csv

# =====================================================================
# 固定パス
# =====================================================================
BASE = Path(r"C:/Users/Lenovo/Documents/bsim4_analyzer_reliability")

NGSPICE_EXE = r"C:\Program Files\Spice64\bin\ngspice_con.exe"

MODEL_FILE = BASE / "models" / "pmos130.sp"
MODEL_NAME = "pmos130"

TEMPLATE_NBTI = BASE / "templates" / "template_nbti_pmos.cir"
TEMPLATE_VGID = BASE / "templates" / "template_pmos_vgid.cir"

DIR_NBTI = BASE / "results" / "130nm" / "nbti_pmos"
DIR_VGID = BASE / "results" / "130nm" / "nbti_pmos_vgid"

DIR_NBTI.mkdir(parents=True, exist_ok=True)
DIR_VGID.mkdir(parents=True, exist_ok=True)

TEMP = 85.0
LCH  = 0.13e-6
WCH  = 1e-6

STRESS_TIMES = [1, 10, 100, 1e3, 1e4, 1e5]
BIAS_LIST    = [(-1.2, -1.2)]  # PMOS


# =====================================================================
# ngspice 実行
# =====================================================================
def run_ngspice(cir: Path, cwd: Path):
    result = subprocess.run(
        [NGSPICE_EXE, "-b", str(cir)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        cwd=str(cwd),
    )
    log = result.stdout
    (cir.with_suffix(".log")).write_text(log, encoding="utf-8")

    if result.returncode != 0:
        raise RuntimeError(log)
    return log


# =====================================================================
# const-current 法
# =====================================================================
def extract_vtc_const_current(Vgs, Id, W, L):
    Iref = 1e-6 * (W / L)
    Id_abs = np.abs(Id)
    above = np.where(Id_abs >= Iref)[0]
    if len(above) == 0:
        return None

    i2 = above[0]
    if i2 == 0:
        return float(Vgs[i2])

    i1 = i2 - 1
    x1,x2 = Vgs[i1], Vgs[i2]
    y1,y2 = Id_abs[i1], Id_abs[i2]
    return float(x1 + (Iref - y1) * (x2 - x1) / (y2 - y1))


# =====================================================================
# VGID sweep（t=0）
# =====================================================================
def run_vgid(label, vgs, temp):
    cir = DIR_VGID / f"{label}.cir"
    dat = DIR_VGID / f"{label}_vgid.dat"

    tpl = TEMPLATE_VGID.read_text(encoding="utf-8")
    txt = (
        tpl.replace("{{MODEL_INCLUDE}}", f'.include "{MODEL_FILE.as_posix()}"')
           .replace("{{MODEL_NAME}}", MODEL_NAME)
           .replace("{{TEMP}}", str(temp))
           .replace("{{LCH}}", str(LCH))
           .replace("{{WCH}}", str(WCH))
           .replace("{{D_VOLT}}", "0")
           .replace("{{S_VOLT}}", "1.2")
           .replace("{{B_VOLT}}", "0")
           .replace("{{VG_START}}", "0")
           .replace("{{VG_STOP}}", str(vgs))
           .replace("{{VG_STEP}}", "-0.005")
           .replace("{{CSV_PATH}}", dat.name)
    )

    cir.write_text(txt, encoding="utf-8")
    run_ngspice(cir, DIR_VGID)

    arr = np.loadtxt(dat)
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)

    Vgs = arr[:, 2]  # v(g)-v(s)
    Id  = arr[:, 3]  # |Id|
    return Vgs, Id


# =====================================================================
# NBTI DC（t=0）
# =====================================================================
def run_nbti_dc(vgs, vds, temp, t):
    label = f"130nm_nbti_pmos_{int(abs(vgs)*10)}v_{int(temp)}c_t{t}s"
    cir = DIR_NBTI / f"{label}.cir"
    dat = DIR_NBTI / f"{label}.dat"

    tpl = TEMPLATE_NBTI.read_text(encoding="utf-8")
    txt = (
        tpl.replace("{{STRESS_VGS}}", str(vgs))
           .replace("{{STRESS_VDS}}", str(vds))
           .replace("{{STRESS_TEMP}}", str(temp))
           .replace("{{MODEL_FILE}}", MODEL_FILE.as_posix())
           .replace("{{LOG_FILE}}", dat.name)
    )

    cir.write_text(txt, encoding="utf-8")
    run_ngspice(cir, DIR_NBTI)

    arr = np.loadtxt(dat)
    return float(arr[1]), float(arr[2])


# =====================================================================
# NBTI 劣化モデル
# =====================================================================
def nbti_degradation(t):
    A_vth = 5e-4
    p_vth = 0.20
    A_id  = 1e-2
    p_id  = 0.20

    dVth   = A_vth * (t ** p_vth)
    dIdrel = -A_id * (t ** p_id)
    return dVth, dIdrel


# =====================================================================
# メイン
# =====================================================================
def main():
    summary = DIR_NBTI / "nbti_pmos_summary.csv"
    rows = [["VGS","VDS","TEMP","t","Vtc","Vtg",
             "Idlin","Idsat","dVtc","dVtg","dIdlin","dIdsat"]]

    for vgs, vds in BIAS_LIST:
        base_label = f"130nm_nbti_pmos_{int(abs(vgs)*10)}v_{int(TEMP)}c_t0s"

        # ---- t=0 VGID ----
        Vgs0, Id0 = run_vgid(base_label, vgs, TEMP)

        # ---- t=0 DC ----
        Idlin0, Idsat0 = run_nbti_dc(vgs, vds, TEMP, 0)

        # ---- threshold ----
        gm = np.gradient(Id0, Vgs0)
        Vtg0 = float(Vgs0[np.argmax(np.abs(gm))])
        Vtc0 = extract_vtc_const_current(Vgs0, Id0, WCH, LCH)

        rows.append([vgs, vds, TEMP, 0,
                     Vtc0, Vtg0, Idlin0, Idsat0,
                     0, 0, 0, 0])

        # ---- Stress ----
        for t in STRESS_TIMES:
            dVth, dIdrel = nbti_degradation(t)

            # PMOS：Vth は負側へ → Vgs を左へ移動
            Vtg1 = Vtg0 - dVth
            Vtc1 = None if Vtc0 is None else Vtc0 - dVth

            Idlin1 = Idlin0 * (1 + dIdrel)
            Idsat1 = Idsat0 * (1 + dIdrel)

            rows.append([
                vgs, vds, TEMP, t,
                Vtc1, Vtg1, Idlin1, Idsat1,
                (Vtc1 - Vtc0) if Vtc0 is not None else None,
                Vtg1 - Vtg0,
                Idlin1 - Idlin0,
                Idsat1 - Idsat0
            ])

    with summary.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)

    print(f"[DONE] Summary written → {summary}")


if __name__ == "__main__":
    main()

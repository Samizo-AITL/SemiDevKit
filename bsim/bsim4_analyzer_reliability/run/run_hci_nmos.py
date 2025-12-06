from __future__ import annotations
from pathlib import Path
import subprocess
import numpy as np
import csv

# ======================================================
# 固定パス
# ======================================================
BASE = Path(r"C:/Users/Lenovo/Documents/bsim4_analyzer_reliability")

NGSPICE_EXE = r"C:\Program Files\Spice64\bin\ngspice_con.exe"

MODEL_FILE = BASE / "models" / "nmos130.sp"
MODEL_NAME = "nmos130"

TEMPLATE_HCI  = BASE / "templates" / "template_hci_nmos.cir"
TEMPLATE_VGID = BASE / "templates" / "template_nmos_vgid.cir"

DIR_HCI  = BASE / "results" / "130nm" / "hci_nmos"
DIR_VGID = BASE / "results" / "130nm" / "hci_nmos_vgid"

DIR_HCI.mkdir(parents=True, exist_ok=True)
DIR_VGID.mkdir(parents=True, exist_ok=True)

# 条件
TEMP = 85.0
LCH  = 0.13e-6
WCH  = 1e-6

# ストレス時間 [s]（t>0 はモデルで合成するだけで SPICE は回さない）
STRESS_TIMES = [1, 10, 100, 1e3, 1e4, 1e5]

# バイアスセット (VGS, VDS)
BIAS_LIST = [(1.2, 1.2)]


# ======================================================
# ngspice 実行
# ======================================================
def run_ngspice(cir_path: Path, cwd: Path):
    result = subprocess.run(
        [NGSPICE_EXE, "-b", str(cir_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        cwd=str(cwd),
    )
    log = result.stdout
    (cir_path.with_suffix(".log")).write_text(log, encoding="utf-8")

    if result.returncode != 0:
        raise RuntimeError(log)

    return log


# ======================================================
# 閾値抽出
# ======================================================
def extract_vtg_gmmax(Vgs, Id):
    """gm 最大点の Vgs を Vtg として抽出（gmmax 法）"""
    gm = np.gradient(Id, Vgs)
    idx = int(np.nanargmax(np.abs(gm)))
    return float(Vgs[idx])


def extract_vtc_const_current(Vgs, Id, W, L):
    """一定電流法 Vth 抽出（Iref = 1uA * W/L）"""
    Iref = 1e-6 * (W / L)
    above = np.where(Id >= Iref)[0]
    if len(above) == 0:
        return None
    i2 = above[0]
    if i2 == 0:
        return float(Vgs[i2])

    i1 = i2 - 1
    x1, x2 = Vgs[i1], Vgs[i2]
    y1, y2 = Id[i1], Id[i2]
    return float(x1 + (Iref - y1) * (x2 - x1) / (y2 - y1))


# ======================================================
# VGID sweep（t=0 用）
#   130nm_hci_nmos_12v_85c_t0s_vgid.dat を生成
# ======================================================
def run_vgid(label: str, vgs: float, temp: float):
    cir = DIR_VGID / f"{label}.cir"
    dat = DIR_VGID / f"{label}_vgid.dat"

    tpl = TEMPLATE_VGID.read_text(encoding="utf-8")
    txt = (
        tpl.replace("{{MODEL_INCLUDE}}", f'.include "{MODEL_FILE.as_posix()}"')
           .replace("{{MODEL_NAME}}", MODEL_NAME)
           .replace("{{TEMP}}", str(temp))
           .replace("{{LCH}}", str(LCH))
           .replace("{{WCH}}", str(WCH))
           .replace("{{D_VOLT}}", str(vgs))
           .replace("{{S_VOLT}}", "0")
           .replace("{{B_VOLT}}", "0")
           .replace("{{VG_START}}", "0")
           .replace("{{VG_STOP}}", str(vgs))
           .replace("{{VG_STEP}}", "0.005")
           # wrdata ではファイル名だけ出力
           .replace("{{CSV_PATH}}", dat.name)
    )

    cir.write_text(txt, encoding="utf-8")
    run_ngspice(cir, cwd=DIR_VGID)

    arr = np.loadtxt(dat)
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)

    # .dat の 1 列目が Vgs, 最後の列が Id になるように読み取り
    Vgs = arr[:, 0]
    Id  = arr[:, -1]
    return Vgs, Id


# ======================================================
# DC HCI（t=0 の Idlin / Idsat を測るだけ）
#   130nm_hci_nmos_12v_85c_t0s.dat を生成
# ======================================================
def run_hci_dc(vgs: float, vds: float, temp: float):
    label = f"130nm_hci_nmos_{int(vgs*10)}v_{int(temp)}c_t0s"
    cir = DIR_HCI / f"{label}.cir"
    dat = DIR_HCI / f"{label}.dat"

    tpl = TEMPLATE_HCI.read_text(encoding="utf-8")
    txt = (
        tpl.replace("{{STRESS_VGS}}", str(vgs))
           .replace("{{STRESS_VDS}}", str(vds))
           .replace("{{STRESS_TEMP}}", str(temp))
           .replace("{{MODEL_FILE}}", MODEL_FILE.as_posix())
           # wrdata ではファイル名だけ
           .replace("{{LOG_FILE}}", dat.name)
    )

    cir.write_text(txt, encoding="utf-8")
    run_ngspice(cir, cwd=DIR_HCI)

    arr = np.loadtxt(dat)
    # arr[0]=Vth, arr[1]=Idlin, arr[2]=Idsat
    return float(arr[1]), float(arr[2])  # Idlin, Idsat


# ======================================================
# HCI 劣化モデル（時間依存 ΔVth & ΔIdrel）
# ======================================================
def hci_degradation(t: float):
    """
    超簡易 HCI モデル:
        ΔVth(t)   = A_vth * t^p_vth
        ΔId_rel(t)= -A_id * t^p_id  （相対変化。負なので絶対値は減る）
    """
    A_vth = 5e-4   # V / s^p
    p_vth = 0.20

    A_id  = 1e-2   # 1 / s^p
    p_id  = 0.20

    dVth   = A_vth * (t ** p_vth)
    dIdrel = -A_id * (t ** p_id)
    return dVth, dIdrel


# ======================================================
# メイン処理
# ======================================================
def main():
    summary = DIR_HCI / "hci_summary.csv"
    rows = [["VGS","VDS","TEMP","t","Vtc","Vtg","Idlin","Idsat",
             "dVtc","dVtg","dIdlin","dIdsat"]]

    for vgs, vds in BIAS_LIST:
        print(f"\n===== BASELINE {vgs} V =====")

        # --- t=0s: SPICE 実測 ---
        base_label = f"130nm_hci_nmos_{int(vgs*10)}v_{int(TEMP)}c_t0s"

        # VG–ID スイープ → Vtg0, Vtc0
        Vgs0, Id0 = run_vgid(base_label, vgs, TEMP)
        Vtg0 = extract_vtg_gmmax(Vgs0, Id0)
        Vtc0 = extract_vtc_const_current(Vgs0, Id0, WCH, LCH)

        # DC 測定 → Idlin0, Idsat0
        Idlin0, Idsat0 = run_hci_dc(vgs, vds, TEMP)

        # baseline 行（Δは 0）
        rows.append([
            vgs, vds, TEMP, 0.0,
            Vtc0, Vtg0, Idlin0, Idsat0,
            0.0, 0.0, 0.0, 0.0,
        ])

        # --- t>0: 劣化モデルだけで合成（SPICE は回さない） ---
        for t in STRESS_TIMES:
            print(f"[STRESS] t={t}")

            dVth, dIdrel = hci_degradation(t)

            # 閾値シフト（NMOS: 正方向にシフト）
            Vtg1 = Vtg0 + dVth
            Vtc1 = None if Vtc0 is None else Vtc0 + dVth

            # Id 劣化（lin / sat 同じ割合だけ下げる簡易モデル）
            Idlin1 = Idlin0 * (1.0 + dIdrel)
            Idsat1 = Idsat0 * (1.0 + dIdrel)

            dVtg   = Vtg1 - Vtg0
            dVtc   = None if Vtc0 is None else (Vtc1 - Vtc0)
            dIdlin = Idlin1 - Idlin0
            dIdsat = Idsat1 - Idsat0

            rows.append([
                vgs, vds, TEMP, t,
                Vtc1, Vtg1, Idlin1, Idsat1,
                dVtc, dVtg, dIdlin, dIdsat,
            ])

    with summary.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)

    print(f"\n[DONE] Summary written → {summary}")


if __name__ == "__main__":
    main()

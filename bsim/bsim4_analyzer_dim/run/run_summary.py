from pathlib import Path
import csv

TECH = "130nm"

# ----------------------------
# L sweep : L codes (3桁 nm)
# ----------------------------
L_CODE_LIST = ["010", "013", "016", "020", "050", "100"]

# L_um に変換
L_CODE_TO_UM = {code: int(code) / 100.0 for code in L_CODE_LIST}

# ----------------------------
# W sweep : W codes
# ----------------------------
W_CODE_LIST = ["050", "100", "1000"]

# W_um に変換
W_CODE_TO_UM = {
    "050": 0.5,
    "100": 1.0,
    "1000": 10.0,
}

BASE = Path("results") / TECH
SUMMARY_DIR = BASE / "summary"
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# CSV 読み込み
# ------------------------------------------------------------

def read_param_csv(path: Path):
    d = {}
    with path.open() as f:
        rdr = csv.reader(f)
        next(rdr)  # skip header
        for k, v in rdr:
            d[k] = float(v)
    return d


# ------------------------------------------------------------
# L-summary（l_vg + l_vd）
# ------------------------------------------------------------

def make_L_summary(device: str):

    rows = [["L_um", "Vth_gmmax", "gmmax", "Id_lin", "Id_sat", "Vdsat_approx"]]

    for code in L_CODE_LIST:

        L_um = L_CODE_TO_UM[code]

        vg_csv = BASE / "l_vg" / f"{TECH}_{device}_L{code}_vg.csv"
        vd_csv = BASE / "l_vd" / f"{TECH}_{device}_L{code}_vd.csv"

        if not vg_csv.exists():
            print(f"[WARN] missing VG: {vg_csv}")
            continue
        if not vd_csv.exists():
            print(f"[WARN] missing VD: {vd_csv}")
            continue

        vg = read_param_csv(vg_csv)
        vd = read_param_csv(vd_csv)

        rows.append([
            L_um,
            vg.get("Vth_gmmax"),
            vg.get("gmmax"),
            vd.get("Id_lin"),
            vd.get("Id_sat"),
            vd.get("Vdsat_approx"),
        ])

    out_csv = SUMMARY_DIR / f"{TECH}_{device}_L_summary.csv"
    with out_csv.open("w", newline="") as f:
        csv.writer(f).writerows(rows)

    print(f"[OK] L-summary → {out_csv}")


# ------------------------------------------------------------
# W-summary（w_vg + w_vd）
# ------------------------------------------------------------

def make_W_summary(device: str):

    rows = [["W_um", "Vth_gmmax", "gmmax", "Id_lin", "Id_sat", "Vdsat_approx"]]

    for code in W_CODE_LIST:

        W_um = W_CODE_TO_UM[code]

        vg_csv = BASE / "w_vg" / f"{TECH}_{device}_W{code}_vg.csv"
        vd_csv = BASE / "w_vd" / f"{TECH}_{device}_W{code}_vd.csv"

        if not vg_csv.exists():
            print(f"[WARN] missing VG: {vg_csv}")
            continue
        if not vd_csv.exists():
            print(f"[WARN] missing VD: {vd_csv}")
            continue

        vg = read_param_csv(vg_csv)
        vd = read_param_csv(vd_csv)

        rows.append([
            W_um,
            vg.get("Vth_gmmax"),
            vg.get("gmmax"),
            vd.get("Id_lin"),
            vd.get("Id_sat"),
            vd.get("Vdsat_approx"),
        ])

    out_csv = SUMMARY_DIR / f"{TECH}_{device}_W_summary.csv"
    with out_csv.open("w", newline="") as f:
        csv.writer(f).writerows(rows)

    print(f"[OK] W-summary → {out_csv}")


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------

if __name__ == "__main__":
    for dev in ["nmos", "pmos"]:
        make_L_summary(dev)
        make_W_summary(dev)

    print("=== run_summary.py DONE ===")

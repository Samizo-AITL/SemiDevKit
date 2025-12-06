import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

TECH = "130nm"
BASE = Path("results") / TECH / "summary"

PARAMS = ["Vth_gmmax", "gmmax", "Id_lin", "Id_sat", "Vdsat_approx"]


# -------------------------------------------------------------
# 1項目プロット関数
# -------------------------------------------------------------
def plot_xy(df, xcol, ycol, title_prefix, outfile_prefix):

    df = df.sort_values(by=xcol)

    x = df[xcol].astype(float).to_numpy()
    y = df[ycol].astype(float).to_numpy()

    # ===== Linear plot =====
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker="o")
    plt.xlabel(xcol)
    plt.ylabel(ycol)
    plt.title(f"{title_prefix} : {ycol} (lin)")
    plt.grid(True)
    out_lin = BASE / f"{outfile_prefix}_{ycol}_lin.png"
    plt.savefig(out_lin)
    plt.close()

    # ===== Log plot =====
    # 正の y のみプロット
    pos_mask = y > 0

    if np.any(pos_mask):
        plt.figure(figsize=(6, 4))
        plt.plot(x[pos_mask], y[pos_mask], marker="o")
        plt.xlabel(xcol)
        plt.ylabel(ycol)
        plt.yscale("log")
        plt.title(f"{title_prefix} : {ycol} (log)")
        plt.grid(True)
        out_log = BASE / f"{outfile_prefix}_{ycol}_log.png"
        plt.savefig(out_log)
        plt.close()


# -------------------------------------------------------------
# Summary CSV を読み込み & 全パラメータをプロット
# -------------------------------------------------------------
def process_summary(device: str, mode: str):

    csv_path = BASE / f"{TECH}_{device}_{mode}_summary.csv"
    if not csv_path.exists():
        print(f"[WARN] missing {csv_path}")
        return

    df = pd.read_csv(csv_path)

    xcol = "L_um" if mode == "L" else "W_um"
    title_prefix = f"{device.upper()} {mode}-sweep"
    outfile_prefix = f"{TECH}_{device}_{mode}"

    for param in PARAMS:
        if param in df.columns:
            plot_xy(df, xcol, param, title_prefix, outfile_prefix)


# -------------------------------------------------------------
# MAIN
# -------------------------------------------------------------
if __name__ == "__main__":

    for dev in ["nmos", "pmos"]:
        process_summary(dev, "L")
        process_summary(dev, "W")

    print("=== plot_summary.py DONE ===")

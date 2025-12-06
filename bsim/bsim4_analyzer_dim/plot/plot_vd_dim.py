import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

TECH = "130nm"

# -------------------------------------------------------------
# dat 読み込み (Vds, Id)   ← 2列形式に修正
# -------------------------------------------------------------
def load_dat(dat_path):
    data = np.loadtxt(dat_path)
    Vds = data[:, 0]    # 横軸
    Id  = data[:, 3]    # 縦軸（正負含む）
    return Vds, Id


# -------------------------------------------------------------
# 個別プロット
# -------------------------------------------------------------
def plot_individual(dat_path, title):
    Vds, Id = load_dat(dat_path)

    # ===== linear =====
    plt.figure(figsize=(6,4))
    plt.plot(Vds, Id)
    plt.title(title + " (lin)")
    plt.xlabel("Vds [V]")
    plt.ylabel("Id [A]")
    plt.grid()
    out_lin = dat_path.with_suffix(".vd_lin.png")
    plt.savefig(out_lin)
    plt.close()

    # ===== log =====
    plt.figure(figsize=(6,4))
    mask = (Id != 0)
    plt.semilogy(Vds[mask], np.abs(Id[mask]))
    plt.title(title + " (log)")
    plt.xlabel("Vds [V]")
    plt.ylabel("|Id| [A]")
    plt.grid(True, which="both")
    out_log = dat_path.with_suffix(".vd_log.png")
    plt.savefig(out_log)
    plt.close()

    print("[OK] →", out_lin, ",", out_log)


# -------------------------------------------------------------
# まとめプロット（Lall / Wall）
# -------------------------------------------------------------
def summary_plot(dat_files, out_png_base, title):

    # ===== linear =====
    plt.figure(figsize=(7,5))
    for dat in dat_files:
        Vds, Id = load_dat(dat)
        label = dat.stem.split("_")[2]   # L010, W050 など
        plt.plot(Vds, Id, label=label)

    plt.title(title + " (lin)")
    plt.xlabel("Vds [V]")
    plt.ylabel("Id [A]")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_png_base + "_lin.png")
    plt.close()

    # ===== log =====
    plt.figure(figsize=(7,5))
    for dat in dat_files:
        Vds, Id = load_dat(dat)
        mask = (Id != 0)
        label = dat.stem.split("_")[2]
        plt.semilogy(Vds[mask], np.abs(Id[mask]), label=label)

    plt.title(title + " (log)")
    plt.xlabel("Vds [V]")
    plt.ylabel("|Id| [A]")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_png_base + "_log.png")
    plt.close()

    print("[OK] summary →", out_png_base)


# -------------------------------------------------------------
# MAIN
# -------------------------------------------------------------
if __name__ == "__main__":
    print("===== plot_vd_dim.py START =====")

    base = Path("results") / TECH

    # ---------------------------------------------------------
    # 個別プロット
    # ---------------------------------------------------------
    for mode in ["l_vd", "w_vd"]:
        for dat in sorted((base / mode).glob("*.dat")):
            plot_individual(dat, dat.stem)

    # ---------------------------------------------------------
    # L sweep summary（数値ソート）
    # ---------------------------------------------------------
    for device in ["nmos", "pmos"]:
        dat_files = sorted(
            (base / "l_vd").glob(f"{TECH}_{device}_L*_vd.dat"),
            key=lambda p: int(p.stem.split("_")[2][1:])    # "L010" → 10
        )
        out_png_base = str(base / "l_vd" / f"{TECH}_{device}_Lall_vd")
        summary_plot(dat_files, out_png_base, f"Id-Vd L-sweep ({device.upper()})")

    # ---------------------------------------------------------
    # W sweep summary（数値ソート）
    # ---------------------------------------------------------
    for device in ["nmos", "pmos"]:
        dat_files = sorted(
            (base / "w_vd").glob(f"{TECH}_{device}_W*_vd.dat"),
            key=lambda p: int(p.stem.split("_")[2][1:])    # "W050" → 50, "W1000" → 1000
        )
        out_png_base = str(base / "w_vd" / f"{TECH}_{device}_Wall_vd")
        summary_plot(dat_files, out_png_base, f"Id-Vd W-sweep ({device.upper()})")

    print("===== plot_vd_dim.py DONE =====")

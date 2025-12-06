import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

TECH = "130nm"

# -----------------------
# DAT 読み込み
# -----------------------
def load_dat(dat_path):
    data = np.loadtxt(dat_path)

    # GNUPLOT ASCII → 2列: Vgs, Id
    Vgs = data[:, 0]
    Id  = data[:, 3]
    return Vgs, Id

# -----------------------
# 個別プロット
# -----------------------
def plot_individual(dat_path, title):
    Vgs, Id = load_dat(dat_path)

    # ===== 線形 =====
    plt.figure(figsize=(6,4))
    plt.plot(Vgs, Id)
    plt.title(title + " (lin)")
    plt.xlabel("Vgs [V]")
    plt.ylabel("Id [A]")
    plt.grid()
    out_lin = dat_path.with_suffix(".vg_lin.png")
    plt.savefig(out_lin)
    plt.close()

    # ===== 対数 =====
    plt.figure(figsize=(6,4))
    mask = (Id != 0)
    plt.semilogy(Vgs[mask], np.abs(Id[mask]))
    plt.title(title + " (log)")
    plt.xlabel("Vgs [V]")
    plt.ylabel("|Id| [A]")
    plt.grid(True, which="both")
    out_log = dat_path.with_suffix(".vg_log.png")
    plt.savefig(out_log)
    plt.close()

    print("[OK] →", out_lin, ",", out_log)


# -----------------------
# L/W sweep summary plot
# -----------------------
def summary_plot(dat_files, out_png_base, title):

    # ===== 線形 =====
    plt.figure(figsize=(7,5))
    for dat in dat_files:
        Vgs, Id = load_dat(dat)
        label = dat.stem.split("_")[2]   # L010 / W1000 など
        plt.plot(Vgs, Id, label=label)

    plt.title(title + " (lin)")
    plt.xlabel("Vgs [V]")
    plt.ylabel("Id [A]")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_png_base + "_lin.png")
    plt.close()

    # ===== 対数 =====
    plt.figure(figsize=(7,5))
    for dat in dat_files:
        Vgs, Id = load_dat(dat)
        mask = (Id != 0)
        label = dat.stem.split("_")[2]
        plt.semilogy(Vgs[mask], np.abs(Id[mask]), label=label)

    plt.title(title + " (log)")
    plt.xlabel("Vgs [V]")
    plt.ylabel("|Id| [A]")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_png_base + "_log.png")
    plt.close()

    print("[OK] summary →", out_png_base)


# -----------------------
# MAIN
# -----------------------
if __name__ == "__main__":
    print("===== plot_vg_dim.py START =====")

    base = Path("results") / TECH

    # ------------------------------
    # 個別プロット（L + W 全部）
    # ------------------------------
    for mode in ["l_vg", "w_vg"]:
        for dat in sorted((base / mode).glob("*.dat")):
            plot_individual(dat, dat.stem)

    # ------------------------------
    # L-sweep summary
    # ------------------------------
    for device in ["nmos", "pmos"]:
        dat_files = sorted(
            (base / "l_vg").glob(f"{TECH}_{device}_L*_vg.dat"),
            key=lambda p: int(p.stem.split("_")[2][1:])  # L010 → 10
        )
        out_png_base = str(base / "l_vg" / f"{TECH}_{device}_Lall_vg")
        summary_plot(dat_files, out_png_base, f"Id-Vg L-sweep ({device.upper()})")

    # ------------------------------
    # W-sweep summary
    # ------------------------------
    for device in ["nmos", "pmos"]:
        dat_files = sorted(
            (base / "w_vg").glob(f"{TECH}_{device}_W*_vg.dat"),
            key=lambda p: int(p.stem.split("_")[2][1:])  # W050 → 50, W1000 → 1000
        )
        out_png_base = str(base / "w_vg" / f"{TECH}_{device}_Wall_vg")
        summary_plot(dat_files, out_png_base, f"Id-Vg W-sweep ({device.upper()})")

    print("===== plot_vg_dim.py DONE =====")

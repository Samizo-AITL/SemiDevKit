import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path("results/130nm/vdid")

# 対応する温度タグ
TEMP_LIST = ["LT", "RT", "HT"]
TEMP_LABEL = {"LT": "LT", "RT": "RT", "HT": "HT"}

# NMOS / PMOS
DEVICES = ["nmos", "pmos"]


def load_dat(path: Path):
    """
    VDID 用 .dat を読み込みます。
    仕様（ngspice + wrdata VX IY）:
        col0: Vds (VX)
        col1: Vds のコピー（使わない）
        col2: Vds のコピー（使わない）
        col3: Id  (IY)
    """
    data = np.loadtxt(path)
    if data.ndim == 1:
        data = data.reshape(1, -1)

    # 列数チェック（4 列想定）
    if data.shape[1] < 4:
        raise RuntimeError(f".dat format unexpected (cols={data.shape[1]}): {path}")

    Vds = data[:, 0]
    Id = data[:, 3]

    return Vds, Id


def plot_device(device: str):
    """NMOS または PMOS の VDID をプロット"""

    # ---------------------------------------------------------------
    # Linear Plot
    # ---------------------------------------------------------------
    plt.figure(figsize=(10, 7))
    for tag in TEMP_LIST:
        dat = BASE / f"130nm_{device}_vdid_{tag}.dat"
        if not dat.exists():
            print(f"[warn] missing: {dat}")
            continue

        Vds, Id = load_dat(dat)
        plt.plot(Vds, Id, label=TEMP_LABEL[tag])

    plt.xlabel("Vds = V(d) - V(s) [V]")
    plt.ylabel("Id [A]")
    plt.title(f"VDID – 130NM – {device.upper()} (Linear, SPICE Polarity)")
    plt.grid(True)
    plt.legend()
    out_png = BASE / f"130nm_{device}_vdid_lin.png"
    plt.savefig(out_png, dpi=200)
    print(f"[saved] {out_png}")

    # ---------------------------------------------------------------
    # Log Plot
    # ---------------------------------------------------------------
    plt.figure(figsize=(10, 7))
    for tag in TEMP_LIST:
        dat = BASE / f"130nm_{device}_vdid_{tag}.dat"
        if not dat.exists():
            continue

        Vds, Id = load_dat(dat)
        # PMOS は Id < 0 なので絶対値を取って log プロット
        plt.semilogy(Vds, np.abs(Id), label=TEMP_LABEL[tag])

    plt.xlabel("Vds = V(d) - V(s) [V]")
    plt.ylabel("Id [A] (log)")
    plt.title(f"VDID – 130NM – {device.upper()} (Log, SPICE Polarity)")
    plt.grid(True, which="both")
    plt.legend()
    out_png = BASE / f"130nm_{device}_vdid_log.png"
    plt.savefig(out_png, dpi=200)
    print(f"[saved] {out_png}")


if __name__ == "__main__":
    for dev in DEVICES:
        plot_device(dev)

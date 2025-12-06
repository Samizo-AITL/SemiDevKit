import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# run_hci_nmos.py と同じ設定
BASE = Path(r"C:/Users/Lenovo/Documents/bsim4_analyzer_reliability")
CSV_FILE = BASE / "results/130nm/hci_nmos/hci_summary.csv"
DIR_VGID = BASE / "results/130nm/hci_nmos_vgid"

# HCI 劣化モデル（run_hci_nmos.py と同じ）
def hci_degradation(t: float):
    A_vth = 5e-4
    p_vth = 0.20
    A_id  = 1e-2
    p_id  = 0.20
    dVth   = A_vth * (t ** p_vth)
    dIdrel = -A_id * (t ** p_id)
    return dVth, dIdrel


def main():
    df = pd.read_csv(CSV_FILE)

    # stress time (log scale)
    t = df["t"].values

    # delta values
    dVtg   = df["dVtg"].values
    dVtc   = df["dVtc"].values
    dIdlin = df["dIdlin"].values
    dIdsat = df["dIdsat"].values

    # ----------------------------------------------------
    # 図1: dVtg (gmmax)
    # ----------------------------------------------------
    plt.figure()
    plt.semilogx(t, dVtg, "-o")
    plt.xlabel("Stress time (s)")
    plt.ylabel("dVtg (V)")
    plt.title("HCI: dVtg vs Stress Time (gmmax)")
    plt.grid()
    plt.tight_layout()
    plt.savefig(BASE / "results/130nm/hci_nmos/dVtg_vs_time.png", dpi=150)
    plt.show()

    # ----------------------------------------------------
    # 図2: dVtc (const-current)
    # ----------------------------------------------------
    plt.figure()
    plt.semilogx(t, dVtc, "-o")
    plt.xlabel("Stress time (s)")
    plt.ylabel("dVtc (V)")
    plt.title("HCI: dVtc vs Stress Time (const-current)")
    plt.grid()
    plt.tight_layout()
    plt.savefig(BASE / "results/130nm/hci_nmos/dVtc_vs_time.png", dpi=150)
    plt.show()

    # ----------------------------------------------------
    # 図3: dIdlin
    # ----------------------------------------------------
    plt.figure()
    plt.semilogx(t, dIdlin, "-o")
    plt.xlabel("Stress time (s)")
    plt.ylabel("dIdlin (A)")
    plt.title("HCI: dIdlin vs Stress Time")
    plt.grid()
    plt.tight_layout()
    plt.savefig(BASE / "results/130nm/hci_nmos/dIdlin_vs_time.png", dpi=150)
    plt.show()

    # ----------------------------------------------------
    # 図4: dIdsat
    # ----------------------------------------------------
    plt.figure()
    plt.semilogx(t, dIdsat, "-o")
    plt.xlabel("Stress time (s)")
    plt.ylabel("dIdsat (A)")
    plt.title("HCI: dIdsat vs Stress Time")
    plt.grid()
    plt.tight_layout()
    plt.savefig(BASE / "results/130nm/hci_nmos/dIdsat_vs_time.png", dpi=150)
    plt.show()

    # ----------------------------------------------------
    # 図5: Vg–Id Linear scale
    # ----------------------------------------------------
    base_label = "130nm_hci_nmos_12v_85c_t0s"
    dat0 = DIR_VGID / f"{base_label}_vgid.dat"

    arr0 = np.loadtxt(dat0)
    if arr0.ndim == 1:
        arr0 = arr0.reshape(1, -1)

    Vgs0 = arr0[:, 0]
    Id0  = arr0[:, -1]

    stress_times = [0, 1, 10, 100, 1e3, 1e4, 1e5]

    # ---- Linear plot ----
    plt.figure(figsize=(8, 6))
    for tt in stress_times:
        if tt == 0:
            Vgs = Vgs0
            Id  = Id0
            label = "0 s"
        else:
            dVth, dIdrel = hci_degradation(tt)
            Vgs = Vgs0 + dVth
            Id  = Id0 * (1.0 + dIdrel)
            label = f"{tt} s"

        plt.plot(Vgs, Id, label=label)

    plt.xlabel("Vgs (V)")
    plt.ylabel("Id (A)")
    plt.title("NMOS HCI: Vg–Id (Linear scale)")
    plt.grid(True)
    plt.legend(title="Stress time")
    plt.tight_layout()

    out_linear = DIR_VGID / "vgid_all_times_linear.png"
    plt.savefig(out_linear, dpi=150)
    plt.show()

    # ----------------------------------------------------
    # 図6: Vg–Id Log scale（Id を log10 表示）
    # ----------------------------------------------------
    plt.figure(figsize=(8, 6))
    for tt in stress_times:
        if tt == 0:
            Vgs = Vgs0
            Id  = Id0
            label = "0 s"
        else:
            dVth, dIdrel = hci_degradation(tt)
            Vgs = Vgs0 + dVth
            Id  = Id0 * (1.0 + dIdrel)
            label = f"{tt} s"

        plt.semilogy(Vgs, Id, label=label)

    plt.xlabel("Vgs (V)")
    plt.ylabel("Id (A, log scale)")
    plt.title("NMOS HCI: Vg–Id (Log scale)")
    plt.grid(True, which="both")
    plt.legend(title="Stress time")
    plt.tight_layout()

    out_log = DIR_VGID / "vgid_all_times_log.png"
    plt.savefig(out_log, dpi=150)
    plt.show()

    print(f"[DONE] Saved:")
    print(f" - {out_linear}")
    print(f" - {out_log}")


if __name__ == "__main__":
    main()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(r"C:/Users/Lenovo/Documents/bsim4_analyzer_reliability")
CSV_FILE = BASE / "results/130nm/nbti_pmos/nbti_pmos_summary.csv"
DIR_VGID = BASE / "results/130nm/nbti_pmos_vgid"

def nbti_degradation(t):
    A_vth = 5e-4
    p_vth = 0.20
    A_id  = 1e-2
    p_id  = 0.20
    dVth   = A_vth * (t ** p_vth)
    dIdrel = -A_id * (t ** p_id)
    return dVth, dIdrel


def main():
    df = pd.read_csv(CSV_FILE)
    t = df["t"].values

    dVtg   = df["dVtg"].values
    dVtc   = df["dVtc"].values
    dIdlin = df["dIdlin"].values
    dIdsat = df["dIdsat"].values

    # ---- ΔVtg ----
    plt.figure()
    plt.semilogx(t, dVtg, "-o")
    plt.grid()
    plt.xlabel("Stress time (s)")
    plt.ylabel("dVtg (V)")
    plt.title("PMOS NBTI: dVtg")
    plt.savefig(BASE / "results/130nm/nbti_pmos/dVtg_vs_time.png", dpi=150)

    # ---- ΔVtc ----
    plt.figure()
    plt.semilogx(t, dVtc, "-o")
    plt.grid()
    plt.xlabel("Stress time (s)")
    plt.ylabel("dVtc (V)")
    plt.title("PMOS NBTI: dVtc")
    plt.savefig(BASE / "results/130nm/nbti_pmos/dVtc_vs_time.png", dpi=150)

    # ---- ΔId ----
    plt.figure()
    plt.semilogx(t, dIdlin, "-o")
    plt.grid()
    plt.xlabel("Stress time (s)")
    plt.ylabel("dIdlin (A)")
    plt.title("PMOS NBTI: dIdlin")
    plt.savefig(BASE / "results/130nm/nbti_pmos/dIdlin_vs_time.png", dpi=150)

    plt.figure()
    plt.semilogx(t, dIdsat, "-o")
    plt.grid()
    plt.xlabel("Stress time (s)")
    plt.ylabel("dIdsat (A)")
    plt.title("PMOS NBTI: dIdsat")
    plt.savefig(BASE / "results/130nm/nbti_pmos/dIdsat_vs_time.png", dpi=150)

    # ---- Vg–Id: 全 stress ----
    base_label = "130nm_nbti_pmos_12v_85c_t0s"
    dat0 = DIR_VGID / f"{base_label}_vgid.dat"
    arr0 = np.loadtxt(dat0)
    if arr0.ndim == 1:
        arr0 = arr0.reshape(1, -1)

    Vgs0 = arr0[:, 2]
    Id0  = arr0[:, 3]

    stress_list = [0, 1, 10, 100, 1e3, 1e4, 1e5]

    # ---- Linear ----
    plt.figure()
    for tt in stress_list:
        if tt == 0:
            Vgs = Vgs0
            Id  = Id0
        else:
            dVth, dIdrel = nbti_degradation(tt)
            Vgs = Vgs0 - dVth
            Id  = Id0 * (1 + dIdrel)

        plt.plot(Vgs, Id, label=f"{tt} s")

    plt.legend()
    plt.grid(True)
    plt.xlabel("Vgs (V)")
    plt.ylabel("Id (A)")
    plt.title("PMOS NBTI: Vg–Id (Linear)")
    plt.savefig(DIR_VGID / "vgid_all_linear.png", dpi=150)

    # ---- Log ----
    plt.figure()
    for tt in stress_list:
        if tt == 0:
            Vgs = Vgs0
            Id  = Id0
        else:
            dVth, dIdrel = nbti_degradation(tt)
            Vgs = Vgs0 - dVth
            Id  = Id0 * (1 + dIdrel)

        plt.semilogy(Vgs, Id, label=f"{tt} s")

    plt.legend()
    plt.grid(True, which="both")
    plt.xlabel("Vgs (V)")
    plt.ylabel("Id (A)")
    plt.title("PMOS NBTI: Vg–Id (Log)")
    plt.savefig(DIR_VGID / "vgid_all_log.png", dpi=150)

    print("\n[DONE] All plots saved.")


if __name__ == "__main__":
    main()

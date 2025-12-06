#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os

# ====== Base parameters ======
Pm = 42.0
Pr_target = 30.0
Vmax = 30.0
t_list = [1.0e-6, 1.2e-6, 1.4e-6]   # membrane thickness variation (1.0–1.4 µm)
Ec_phys = 6e6   # material coercive field (constant)

def make_branch(E, Ec, Es, Pm):
    P_up   = Pm*np.tanh((E+Ec)/Es)
    P_down = Pm*np.tanh((E-Ec)/Es)

    P_pos = 0.5*(P_up.max()+P_down.max())
    P_neg = 0.5*(P_up.min()+P_down.min())

    def scale(P):
        return np.where(P>=0, P*(P_pos/P_up.max()), P*(P_neg/P_up.min()))

    return scale(P_up), scale(P_down)


def make_loop(E, P_up, P_down):
    E1, P1 = E, P_up
    Ej1 = np.full(100, E[-1])
    Pj1 = np.linspace(P_up[-1], P_down[-1], 100)
    E2, P2 = E[::-1], P_down[::-1]
    Ej2 = np.full(100, E[0])
    Pj2 = np.linspace(P_down[0], P_up[0], 100)

    Eloop = np.concatenate([E1, Ej1, E2, Ej2])
    Ploop = np.concatenate([P1, Pj1, P2, Pj2])

    return Eloop, Ploop


def main():
    os.makedirs("fig", exist_ok=True)

    # Pr → Es を決定
    ratio = Pr_target / Pm
    Ec_over_Es = 0.5*np.log((1+ratio)/(1-ratio))
    Es = Ec_phys / Ec_over_Es

    # ============================
    # 1) P–E plot
    # ============================
    plt.figure(figsize=(7,5))
    for t in t_list:
        E = np.linspace(-Vmax/t, Vmax/t, 2000)
        P_up, P_down = make_branch(E, Ec_phys, Es, Pm)
        Eloop, Ploop = make_loop(E, P_up, P_down)

        plt.plot(Eloop/1e6, Ploop, lw=2, label=f"t={t*1e6:.2f} µm")

    plt.xlabel("E [MV/m]")
    plt.ylabel("P [µC/cm²]")
    plt.title("P–E Loop Variation vs Thickness (Material View)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("fig/pzt_pe_tvar_PE.png", dpi=200)

    # ============================
    # 2) P–V plot
    # ============================
    plt.figure(figsize=(7,5))

    for t in t_list:
        # voltage sweep
        V = np.linspace(-Vmax, Vmax, 2000)
        E = V / t

        P_up, P_down = make_branch(E, Ec_phys, Es, Pm)
        Eloop, Ploop = make_loop(E, P_up, P_down)

        # 4200点の Vloop を作る
        V1 = V
        Vj1 = np.full(100, V[-1])
        V2 = V[::-1]
        Vj2 = np.full(100, V[0])

        Vloop = np.concatenate([V1, Vj1, V2, Vj2])

        plt.plot(Vloop, Ploop, lw=2, label=f"t={t*1e6:.2f} µm")

    plt.xlabel("V [V]")
    plt.ylabel("P [µC/cm²]")
    plt.title("P–V Loop Variation vs Thickness (Device View)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("fig/pzt_pe_tvar_PV.png", dpi=200)

    plt.show()


if __name__ == "__main__":
    main()

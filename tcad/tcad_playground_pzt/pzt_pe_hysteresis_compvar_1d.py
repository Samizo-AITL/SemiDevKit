#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os

# nominal values
Pm0 = 42
Pr0 = 30
Ec0 = 6e6
Vmax = 30
t_pzt = 1.2e-6

# composition shift (Ti/Zr ratio deviation)
# negative → Zr-rich, positive → Ti-rich
composition_list = [-0.10, 0.00, +0.10]

def comp_model(d):
    """
    d = composition deviation
    -0.10 → Zr-rich side
    +0.10 → Ti-rich side
    """
    Pm = Pm0*(1+0.5*d)
    Pr = Pr0*(1+0.6*d)
    Ec = Ec0*(1+0.8*d)
    return Pm, Pr, Ec

def compute_branch(E, Ec, Es, Pm):
    P_up   = Pm*np.tanh((E+Ec)/Es)
    P_down = Pm*np.tanh((E-Ec)/Es)

    P_pos = 0.5*(np.max(P_up)+np.max(P_down))
    P_neg = 0.5*(np.min(P_up)+np.min(P_down))

    def scale(P):
        return np.where(P>=0, P*(P_pos/np.max(P)), P*(P_neg/np.min(P)))

    return scale(P_up), scale(P_down)

def make_loop(E, P_up, P_down):
    E1=E; P1=P_up
    Ej1=np.full(100,E[-1]); Pj1=np.linspace(P_up[-1],P_down[-1],100)
    E2=E[::-1]; P2=P_down[::-1]
    Ej2=np.full(100,E[0]); Pj2=np.linspace(P_down[0],P_up[0],100)
    return np.concatenate([E1,Ej1,E2,Ej2]), np.concatenate([P1,Pj1,P2,Pj2])

def label_for_comp(d):
    """凡例ラベルを人間が理解できる文字列に変換"""
    if d < 0:
        return f"{d:+.2f}  (Zr-rich)"
    elif d > 0:
        return f"{d:+.2f}  (Ti-rich)"
    else:
        return f"{d:+.2f}  (Nominal)"

def main():
    os.makedirs("fig", exist_ok=True)
    plt.figure(figsize=(7,5))

    E = np.linspace(-Vmax/t_pzt, Vmax/t_pzt, 2000)

    for d in composition_list:
        Pm, Pr, Ec = comp_model(d)
        ratio = Pr/Pm
        Ec_over_Es = 0.5*np.log((1+ratio)/(1-ratio))
        Es = Ec/Ec_over_Es

        P_up, P_down = compute_branch(E, Ec, Es, Pm)
        Eloop, Ploop = make_loop(E, P_up, P_down)

        plt.plot(Eloop/1e6, Ploop, lw=2, label=label_for_comp(d))

    plt.xlabel("E [MV/m]")
    plt.ylabel("P [µC/cm²]")
    plt.title("P–E Loop Variation vs PZT Composition (Zr/Ti Ratio)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("fig/pzt_pe_hysteresis_compvar.png", dpi=200)
    plt.show()

if __name__=="__main__":
    main()

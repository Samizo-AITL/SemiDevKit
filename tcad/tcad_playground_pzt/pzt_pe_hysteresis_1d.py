#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os

# ============================
# Parameters
# ============================
Pm = 42.0        # [uC/cm2]
Pr_target = 30.0 # [uC/cm2]  ← ここだけ変えれば Pr 調整
Vmax = 30.0      # [V]
t_pzt = 1.2e-6   # [m]

Ec = 5e6        # [V/m]  ヒステリシス幅の目安（細くしたければ下げる）

# --- Pr_target から Es を決める ---
ratio = Pr_target / Pm
if abs(ratio) >= 1.0:
    raise ValueError("Pr_target は |Pr| < Pm を満たす必要があります。")

Ec_over_Es = 0.5 * np.log((1 + ratio) / (1 - ratio))  # = arctanh(ratio)
Es = Ec / Ec_over_Es    # smoothing parameter（自動決定）

print(f"Pm = {Pm:.2f} uC/cm2, Pr_target = {Pr_target:.2f} uC/cm2")
print(f"Ec = {Ec/1e6:.2f} MV/m, Es = {Es/1e6:.2f} MV/m (from Pr_target)")

def make_branches(E, Ec, Es, Pm):
    """rising/falling 枝（±Pm 揃え付き）"""
    P_up   = Pm * np.tanh((E + Ec) / Es)
    P_down = Pm * np.tanh((E - Ec) / Es)

    # ±Pm を揃える
    P_pos = 0.5 * (np.max(P_up) + np.max(P_down))
    P_neg = 0.5 * (np.min(P_up) + np.min(P_down))

    def scale(P):
        return np.where(P >= 0,
                        P * (P_pos / np.max(P)),
                        P * (P_neg / np.min(P)))

    return scale(P_up), scale(P_down)

def main():
    os.makedirs("fig", exist_ok=True)

    # E sweep
    E = np.linspace(-Vmax/t_pzt, Vmax/t_pzt, 2000)

    # rising / falling
    P_up, P_down = make_branches(E, Ec, Es, Pm)

    # E≈0 の Pr を確認
    idx0 = np.argmin(np.abs(E))
    Pr_up = P_up[idx0]
    Pr_dn = P_down[idx0]
    print(f"Pr (rising)  @E≈0 = {Pr_up:6.2f} uC/cm2")
    print(f"Pr (falling) @E≈0 = {Pr_dn:6.2f} uC/cm2")

    # ============================
    # Closed loop construction
    # ============================
    # 1. 左→右は rising
    E1 = E
    P1 = P_up

    # 2. 右側ジャンプ（falling の始点へ）
    Ejump1 = np.full(100, E[-1])
    Pjump1 = np.linspace(P_up[-1], P_down[-1], 100)

    # 3. 右→左は falling
    E2 = E[::-1]
    P2 = P_down[::-1]

    # 4. 左側ジャンプ（rising の始点へ）
    Ejump2 = np.full(100, E[0])
    Pjump2 = np.linspace(P_down[0], P_up[0], 100)

    # final loop
    Eloop = np.concatenate([E1, Ejump1, E2, Ejump2])
    Ploop = np.concatenate([P1, Pjump1, P2, Pjump2])

    # ============================
    # Plot
    # ============================
    plt.figure(figsize=(7,5))
    plt.plot(Eloop/1e6, Ploop, lw=2)
    plt.xlabel("E [MV/m]")
    plt.ylabel("P [µC/cm²]")
    plt.title(f"Closed P–E Loop (Pm={Pm:.0f}µC/cm², Vm={Vmax:.0f}V, Pr≈{Pr_target:.0f}µC/cm²)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("fig/pzt_pe_hysteresis_1d.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os

# ============================
# P–E ループ用パラメータ
# ============================
Pm = 42.0        # [uC/cm2]
Pr_target = 30.0 # [uC/cm2]
Vmax = 30.0      # [V]
t_pzt = 1.2e-6   # [m]

Ec = 5e6         # [V/m]  ヒステリシス幅（狭めたければ下げる）

# --- Pr_target から Es を決める ---
ratio = Pr_target / Pm
if abs(ratio) >= 1.0:
    raise ValueError("Pr_target は |Pr| < Pm を満たす必要があります。")

Ec_over_Es = 0.5 * np.log((1 + ratio) / (1 - ratio))  # = arctanh(ratio)
Es = Ec / Ec_over_Es    # smoothing parameter（自動決定）

print(f"Pm = {Pm:.2f} uC/cm2, Pr_target = {Pr_target:.2f} uC/cm2")
print(f"Ec = {Ec/1e6:.2f} MV/m, Es = {Es/1e6:.2f} MV/m (from Pr_target)")


# ============================
# P–E branches
# ============================
def make_branches(E, Ec, Es, Pm):
    """rising/falling 枝（±Pm 揃え付き）"""
    P_up   = Pm * np.tanh((E + Ec) / Es)
    P_down = Pm * np.tanh((E - Ec) / Es)

    # ±Pm を揃える
    P_pos = 0.5 * (np.max(P_up) + np.max(P_down))
    P_neg = 0.5 * (np.min(P_up) + np.min(P_down))

    def scale(P):
        return np.where(
            P >= 0,
            P * (P_pos / np.max(P)),
            P * (P_neg / np.min(P))
        )

    return scale(P_up), scale(P_down)


def make_closed_loop(E, P_up, P_down):
    """P–E の閉ループ（rising → jump → falling → jump）"""
    # 1. 左→右 : rising
    E1 = E
    P1 = P_up

    # 2. 右側ジャンプ（falling の始点へ）
    Ejump1 = np.full(100, E[-1])
    Pjump1 = np.linspace(P_up[-1], P_down[-1], 100)

    # 3. 右→左 : falling
    E2 = E[::-1]
    P2 = P_down[::-1]

    # 4. 左側ジャンプ（rising の始点へ）
    Ejump2 = np.full(100, E[0])
    Pjump2 = np.linspace(P_down[0], P_up[0], 100)

    Eloop = np.concatenate([E1, Ejump1, E2, Ejump2])
    Ploop = np.concatenate([P1, Pjump1, P2, Pjump2])

    return Eloop, Ploop


# ============================
# Strain model (butterfly S–E)
# ============================
def polarization_to_strain(P, Q_eff=1.0):
    """
    超シンプル電歪モデル:
        S ~ Q_eff * (P/Pm)^2
    戻り値は [microstrain] 想定
    """
    P_norm = P / Pm
    S = Q_eff * (P_norm**2) * 1000.0  # 例: 最大 ~1000 µstrain 程度
    return S


# ============================
# Main
# ============================
def main():
    os.makedirs("fig", exist_ok=True)

    # E sweep
    E = np.linspace(-Vmax/t_pzt, Vmax/t_pzt, 2000)

    # P–E branches & closed loop
    P_up, P_down = make_branches(E, Ec, Es, Pm)
    Eloop, Ploop = make_closed_loop(E, P_up, P_down)

    # E≈0 の Pr 確認
    idx0 = np.argmin(np.abs(E))
    Pr_up = P_up[idx0]
    Pr_dn = P_down[idx0]
    print(f"Pr (rising)  @E≈0 = {Pr_up:6.2f} uC/cm2")
    print(f"Pr (falling) @E≈0 = {Pr_dn:6.2f} uC/cm2")

    # --- Butterfly (S–E) ---
    Q_eff = 1.0   # 形だけ見るならこのまま。実測に合わせるときに調整。
    Sloop = polarization_to_strain(Ploop, Q_eff=Q_eff)

    # ============================
    # Plot: P–E & S–E
    # ============================
    fig, ax = plt.subplots(2, 1, figsize=(7, 8), sharex=True)

    # --- P–E loop ---
    ax[0].plot(Eloop/1e6, Ploop, lw=2)
    ax[0].set_ylabel("P [µC/cm²]")
    ax[0].set_title("P–E Hysteresis Loop")
    ax[0].grid(True)

    # --- S–E butterfly ---
    ax[1].plot(Eloop/1e6, Sloop, lw=2)
    ax[1].set_xlabel("E [MV/m]")
    ax[1].set_ylabel("Strain [µstrain]")
    ax[1].set_title("Butterfly Curve (S–E)")
    ax[1].grid(True)

    plt.tight_layout()
    plt.savefig("fig/pzt_se_butterfly_1d.png", dpi=300)
    plt.show()
    print("Saved: fig/pzt_se_butterfly_1d.png")


if __name__ == "__main__":
    main()

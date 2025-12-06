import numpy as np
import matplotlib.pyplot as plt
import os

# =========================================================
#  MOSFET Vd–Id (1D) Temperature スイープ
#   - 長チャネル MOSFET 簡易モデル
#   - nMOS / pMOS 両対応
#   - linear / log の両方を 1 本で出力
#   - 出力：
#       fig/mosfet_vdid_T_sweep_nmos_linear.png
#       fig/mosfet_vdid_T_sweep_nmos_semilog.png
#       fig/mosfet_vdid_T_sweep_pmos_linear.png
#       fig/mosfet_vdid_T_sweep_pmos_semilog.png
# =========================================================

# -------------------------
#  ユーザー設定
# -------------------------
tox      = 3e-9                  # gate oxide thickness [m]
Nsub     = 1e21                  # 基板ドーピング（絶対値）[1/m^3]

# Temperature sweep [K]
T_LIST   = [200.0, 300.0, 400.0]

W        = 1e-6                  # [m]
L        = 1e-6                  # [m]
mu_n     = 0.05                  # [m^2/Vs]
mu_p     = 0.02                  # [m^2/Vs]

# Vd sweep
Vd_min_n = 0.0
Vd_max_n = 0.8
Vd_min_p = 0.0
Vd_max_p = -0.8
Nvd      = 121

# Gate bias for Vd–Id
Vg_bias_n = 0.8                  # [V]
Vg_bias_p = -0.8                 # [V]

FIG_DIR  = "fig"

# -------------------------
#  物理定数
# -------------------------
q    = 1.602e-19
kB   = 1.380649e-23
eps0 = 8.854e-12
eps_ox = 3.9 * eps0
eps_si = 11.7 * eps0

ni = 1e16                        # [1/m^3] （T依存はここでは無視）

# =========================================================
#  MOSFET モデル
# =========================================================
def calc_cox(tox):
    return eps_ox / tox

def calc_vth_mag(Nsub, T, tox):
    """|Vth| = 2φF + γ sqrt(2φF)"""
    Vt = kB * T / q
    phi_F = Vt * np.log(Nsub / ni)
    Cox = calc_cox(tox)
    gamma = np.sqrt(2*q*eps_si*Nsub) / Cox
    return 2*phi_F + gamma*np.sqrt(2*phi_F)

def id_vs_vd_nmos(Vd_array, Vg, Nsub, T, tox, mu, W, L):
    Cox = calc_cox(tox)
    Vth = +calc_vth_mag(Nsub, T, tox)
    Id  = np.zeros_like(Vd_array)

    Vgt = Vg - Vth
    if Vgt <= 0:
        return Id, Vth

    for i, Vd in enumerate(Vd_array):
        if Vd < Vgt:
            Id[i] = mu*Cox*(W/L)*(Vgt*Vd - 0.5*Vd**2)
        else:
            Id[i] = 0.5*mu*Cox*(W/L)*Vgt**2

    return Id, Vth

def id_vs_vd_pmos(Vd_array, Vg, Nsub, T, tox, mu, W, L):
    Cox = calc_cox(tox)
    Vth_mag = calc_vth_mag(Nsub, T, tox)
    Vth_p   = -Vth_mag
    Id      = np.zeros_like(Vd_array)

    Vgt = Vg - Vth_p
    if Vgt >= 0:
        return Id, Vth_p

    Vgt_abs = -Vgt

    for i, Vd in enumerate(Vd_array):
        Vd_abs = -Vd
        if Vd_abs < Vgt_abs:
            Id_abs = mu*Cox*(W/L)*(Vgt_abs*Vd_abs - 0.5*Vd_abs**2)
        else:
            Id_abs = 0.5*mu*Cox*(W/L)*Vgt_abs**2
        Id[i] = -Id_abs

    return Id, Vth_p

# =========================================================
#  メイン：nMOS / pMOS × linear / log
# =========================================================
os.makedirs(FIG_DIR, exist_ok=True)

# ---------- nMOS ----------
Vd_n = np.linspace(Vd_min_n, Vd_max_n, Nvd)

# nMOS linear
plt.figure(figsize=(6,4))
for T in T_LIST:
    Id, Vth = id_vs_vd_nmos(Vd_n, Vg_bias_n, Nsub, T, tox, mu_n, W, L)
    label = f"T = {T:.0f} K (Vth={Vth:.2f} V)"
    plt.plot(Vd_n, Id, label=label)

plt.xlabel("Vd [V]")
plt.ylabel("Id [A]")
plt.title(f"nMOS Vd–Id (T sweep, linear, Vg = {Vg_bias_n} V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vdid_T_sweep_nmos_linear.png"), dpi=300)
plt.show()

# nMOS log
plt.figure(figsize=(6,4))
for T in T_LIST:
    Id, _ = id_vs_vd_nmos(Vd_n, Vg_bias_n, Nsub, T, tox, mu_n, W, L)
    plt.plot(Vd_n, np.maximum(Id, 1e-20), label=f"T = {T:.0f} K")

plt.xlabel("Vd [V]")
plt.ylabel("|Id| [A]")
plt.yscale("log")
plt.title(f"nMOS Vd–Id (T sweep, log, Vg = {Vg_bias_n} V)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vdid_T_sweep_nmos_semilog.png"), dpi=300)
plt.show()

# ---------- pMOS ----------
Vd_p = np.linspace(Vd_min_p, Vd_max_p, Nvd)   # 0 → 負方向

# pMOS linear
plt.figure(figsize=(6,4))
for T in T_LIST:
    Id, Vth_p = id_vs_vd_pmos(Vd_p, Vg_bias_p, Nsub, T, tox, mu_p, W, L)
    label = f"T = {T:.0f} K (Vth={Vth_p:.2f} V)"
    plt.plot(Vd_p, Id, label=label)

plt.xlabel("Vd [V]")
plt.ylabel("Id [A]")
plt.title(f"pMOS Vd–Id (T sweep, linear, Vg = {Vg_bias_p} V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vdid_T_sweep_pmos_linear.png"), dpi=300)
plt.show()

# pMOS log
plt.figure(figsize=(6,4))
for T in T_LIST:
    Id, _ = id_vs_vd_pmos(Vd_p, Vg_bias_p, Nsub, T, tox, mu_p, W, L)
    plt.plot(Vd_p, np.maximum(np.abs(Id), 1e-20), label=f"T = {T:.0f} K")

plt.xlabel("Vd [V]")
plt.ylabel("|Id| [A]")
plt.yscale("log")
plt.title(f"pMOS Vd–Id (T sweep, log, Vg = {Vg_bias_p} V)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vdid_T_sweep_pmos_semilog.png"), dpi=300)
plt.show()

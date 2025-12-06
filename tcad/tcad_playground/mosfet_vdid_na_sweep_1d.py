import numpy as np
import matplotlib.pyplot as plt
import os

# =========================================================
#  MOSFET Vd–Id (1D) Na スイープ
#   - 長チャネル MOSFET 簡易モデル
#   - nMOS / pMOS 両対応
#   - linear / log の両方を出力
# =========================================================

# -------------------------
#  ユーザー設定
# -------------------------
T        = 300.0                 # [K]
tox      = 3e-9                  # gate oxide thickness [m]

Na_list  = [1e20, 1e21, 1e22]    # 基板ドーピング（絶対値）[1/m^3]

W        = 1e-6                  # [m]
L        = 1e-6                  # [m]
mu_n     = 0.05                  # [m^2/Vs]
mu_p     = 0.02                  # [m^2/Vs]

# Vd スイープ条件
Vd_min_n = 0.0
Vd_max_n = 0.8
Vd_min_p = 0.0
Vd_max_p = -0.8
Nvd      = 121

# Vg バイアス（Vd–Id を描くときの Vg）
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
ni     = 1e16                    # [1/m^3]

# =========================================================
#  MOSFET モデル
# =========================================================
def calc_cox(tox):
    return eps_ox / tox

def calc_vth_mag(Nsub, T, tox):
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
        # 全領域ほぼオフ
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

    Vgt = Vg - Vth_p   # Vth_p < 0
    if Vgt >= 0:
        # ほぼオフ
        return Id, Vth_p

    Vgt_abs = -Vgt  # >0

    for i, Vd in enumerate(Vd_array):
        Vd_abs = -Vd
        if Vd_abs < Vgt_abs:
            Id_abs = mu*Cox*(W/L)*(Vgt_abs*Vd_abs - 0.5*Vd_abs**2)
        else:
            Id_abs = 0.5*mu*Cox*(W/L)*Vgt_abs**2
        Id[i] = -Id_abs     # pMOS は Id < 0

    return Id, Vth_p

# =========================================================
#  メイン：nMOS / pMOS × linear / log
# =========================================================
os.makedirs(FIG_DIR, exist_ok=True)

# ---------- nMOS ----------
Vd_n = np.linspace(Vd_min_n, Vd_max_n, Nvd)

# nMOS linear
plt.figure(figsize=(6,4))
for Na in Na_list:
    Id, Vth = id_vs_vd_nmos(Vd_n, Vg_bias_n, Na, T, tox, mu_n, W, L)
    label = f"Na = {Na:.1e} m$^{{-3}}$ (Vth={Vth:.2f} V)"
    plt.plot(Vd_n, Id, label=label)

plt.xlabel("Vd [V]")
plt.ylabel("Id [A]")
plt.title(f"nMOS Vd–Id (Na sweep, linear, Vg = {Vg_bias_n} V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vdid_na_sweep_nmos_linear.png"), dpi=300)
plt.show()

# nMOS log
plt.figure(figsize=(6,4))
for Na in Na_list:
    Id, _ = id_vs_vd_nmos(Vd_n, Vg_bias_n, Na, T, tox, mu_n, W, L)
    plt.plot(Vd_n, np.maximum(Id, 1e-20), label=f"Na = {Na:.1e} m$^{{-3}}$")

plt.xlabel("Vd [V]")
plt.ylabel("|Id| [A]")
plt.yscale("log")
plt.title(f"nMOS Vd–Id (Na sweep, log, Vg = {Vg_bias_n} V)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vdid_na_sweep_nmos_semilog.png"), dpi=300)
plt.show()

# ---------- pMOS ----------
Vd_p = np.linspace(Vd_min_p, Vd_max_p, Nvd)  # 0 → -0.8V

# pMOS linear
plt.figure(figsize=(6,4))
for Na in Na_list:
    Id, Vth_p = id_vs_vd_pmos(Vd_p, Vg_bias_p, Na, T, tox, mu_p, W, L)
    label = f"Na = {Na:.1e} m$^{{-3}}$ (Vth={Vth_p:.2f} V)"
    plt.plot(Vd_p, Id, label=label)

plt.xlabel("Vd [V]")
plt.ylabel("Id [A]")
plt.title(f"pMOS Vd–Id (Na sweep, linear, Vg = {Vg_bias_p} V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vdid_na_sweep_pmos_linear.png"), dpi=300)
plt.show()

# pMOS log
plt.figure(figsize=(6,4))
for Na in Na_list:
    Id, _ = id_vs_vd_pmos(Vd_p, Vg_bias_p, Na, T, tox, mu_p, W, L)
    plt.plot(Vd_p, np.maximum(np.abs(Id), 1e-20), label=f"Na = {Na:.1e} m$^{{-3}}$")

plt.xlabel("Vd [V]")
plt.ylabel("|Id| [A]")
plt.yscale("log")
plt.title(f"pMOS Vd–Id (Na sweep, log, Vg = {Vg_bias_p} V)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vdid_na_sweep_pmos_semilog.png"), dpi=300)
plt.show()

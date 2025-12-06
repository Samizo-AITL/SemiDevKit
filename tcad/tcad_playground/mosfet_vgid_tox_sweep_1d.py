import numpy as np
import matplotlib.pyplot as plt
import os

# =========================================================
#  MOSFET Vg–Id (1D) tox スイープ
#   - 長チャネル MOSFET の簡易モデル
#   - nMOS / pMOS 両対応
#   - linear / log の両方を 1 本で出力
#   - 出力：
#       fig/mosfet_vgid_tox_sweep_nmos_linear.png
#       fig/mosfet_vgid_tox_sweep_nmos_semilog.png
#       fig/mosfet_vgid_tox_sweep_pmos_linear.png
#       fig/mosfet_vgid_tox_sweep_pmos_semilog.png
# =========================================================

# -------------------------
#  ユーザー設定
# -------------------------
T        = 300.0                # [K]
Nsub     = 1e21                 # p-sub（絶対値） [1/m^3]

# tox スイープ [m]
TOX_LIST = [2e-9, 3e-9, 4e-9]

W        = 1e-6                 # [m]
L        = 1e-6                 # [m]
mu_n     = 0.05                 # [m^2/Vs]
mu_p     = 0.02                 # [m^2/Vs]

# Vg スイープ条件
Vg_min_n = -0.4
Vg_max_n =  0.8
Vg_min_p =  0.4
Vg_max_p = -0.8
Nvg      = 121

Vd_n     =  0.05                # [V]
Vd_p     = -0.05                # [V]

FIG_DIR  = "fig"

# -------------------------
#  物理定数
# -------------------------
q    = 1.602e-19
kB   = 1.380649e-23
eps0 = 8.854e-12
eps_ox = 3.9 * eps0
eps_si = 11.7 * eps0

ni = 1e16               # [1/m^3]

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

def id_vs_vg_nmos(Vg_array, Nsub, T, tox, mu, W, L, Vd):
    Cox = calc_cox(tox)
    Vth = +calc_vth_mag(Nsub, T, tox)
    Vt  = kB * T / q

    Id = np.zeros_like(Vg_array)
    for i, Vg in enumerate(Vg_array):
        Vgt = Vg - Vth
        if Vgt <= 0:
            Id[i] = 1e-12 * np.exp(Vgt / (1.5*Vt))
        else:
            if Vd < Vgt:
                Id[i] = mu*Cox*(W/L)*(Vgt*Vd - 0.5*Vd**2)
            else:
                Id[i] = 0.5*mu*Cox*(W/L)*Vgt**2
    return Id, Vth

def id_vs_vg_pmos(Vg_array, Nsub, T, tox, mu, W, L, Vd):
    Cox = calc_cox(tox)
    Vth_mag = calc_vth_mag(Nsub, T, tox)
    Vth_p = -Vth_mag
    Vt  = kB * T / q

    Id = np.zeros_like(Vg_array)
    for i, Vg in enumerate(Vg_array):
        Vgt = Vg - Vth_p   # Vth_p < 0
        if Vgt >= 0:
            Id[i] = -1e-12 * np.exp(-Vgt / (1.5*Vt))
        else:
            Vgt_abs = -Vgt
            Vd_abs = -Vd
            if Vd_abs < Vgt_abs:
                Id_abs = mu*Cox*(W/L)*(Vgt_abs*Vd_abs - 0.5*Vd_abs**2)
            else:
                Id_abs = 0.5*mu*Cox*(W/L)*Vgt_abs**2
            Id[i] = -Id_abs
    return Id, Vth_p

# =========================================================
#  nMOS: linear / log
# =========================================================
os.makedirs(FIG_DIR, exist_ok=True)

Vg_n = np.linspace(Vg_min_n, Vg_max_n, Nvg)

# --- nMOS linear ---
plt.figure(figsize=(6,4))
for tox in TOX_LIST:
    Id, Vth = id_vs_vg_nmos(Vg_n, Nsub, T, tox, mu_n, W, L, Vd_n)
    plt.plot(Vg_n, Id, label=f"tox = {tox*1e9:.1f} nm (Vth={Vth:.2f} V)")

plt.xlabel("Vg [V]")
plt.ylabel("Id [A]")
plt.title(f"nMOS Vg–Id (tox sweep, linear, Vd = {Vd_n} V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vgid_tox_sweep_nmos_linear.png"), dpi=300)
plt.show()

# --- nMOS log ---
plt.figure(figsize=(6,4))
for tox in TOX_LIST:
    Id, _ = id_vs_vg_nmos(Vg_n, Nsub, T, tox, mu_n, W, L, Vd_n)
    plt.plot(Vg_n, np.maximum(Id, 1e-20), label=f"tox = {tox*1e9:.1f} nm")

plt.yscale("log")
plt.xlabel("Vg [V]")
plt.ylabel("|Id| [A]")
plt.title(f"nMOS Vg–Id (tox sweep, log, Vd = {Vd_n} V)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vgid_tox_sweep_nmos_semilog.png"), dpi=300)
plt.show()

# =========================================================
#  pMOS: linear / log
# =========================================================
Vg_p = np.linspace(Vg_min_p, Vg_max_p, Nvg)

# --- pMOS linear ---
plt.figure(figsize=(6,4))
for tox in TOX_LIST:
    Id, Vth = id_vs_vg_pmos(Vg_p, Nsub, T, tox, mu_p, W, L, Vd_p)
    plt.plot(Vg_p, Id, label=f"tox = {tox*1e9:.1f} nm (Vth={Vth:.2f} V)")

plt.xlabel("Vg [V]")
plt.ylabel("Id [A]")
plt.title(f"pMOS Vg–Id (tox sweep, linear, Vd = {Vd_p} V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vgid_tox_sweep_pmos_linear.png"), dpi=300)
plt.show()

# --- pMOS log ---
plt.figure(figsize=(6,4))
for tox in TOX_LIST:
    Id, _ = id_vs_vg_pmos(Vg_p, Nsub, T, tox, mu_p, W, L, Vd_p)
    plt.plot(Vg_p, np.maximum(np.abs(Id), 1e-20), label=f"tox = {tox*1e9:.1f} nm")

plt.yscale("log")
plt.xlabel("Vg [V]")
plt.ylabel("|Id| [A]")
plt.title(f"pMOS Vg–Id (tox sweep, log, Vd = {Vd_p} V)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mosfet_vgid_tox_sweep_pmos_semilog.png"), dpi=300)
plt.show()

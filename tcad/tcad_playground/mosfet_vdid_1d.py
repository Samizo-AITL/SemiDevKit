import numpy as np
import matplotlib.pyplot as plt

# ===========================================
#  ユーザー設定パラメータ（ここを変えればOK）
# ===========================================

# 電源電圧
Vdd = 1.0          # [V]

# 温度
T = 300.0          # [K]

# デバイス寸法
W   = 1e-6         # [m]
Lch = 1e-6         # [m]

# 酸化膜厚・ドーピング
tox = 3e-9         # [m]
Na  = 1e21         # [1/m^3]

# 移動度
mu_n = 0.05        # [m^2/Vs]
mu_p = 0.05        # [m^2/Vs]

# Vd スイープ範囲
Vd_start = 0.0
Vd_stop  = Vdd
Nvd      = 101

# Vg ライン（NMOS 用）
Vg_list_n = [0.30, 0.40, 0.50, 0.60, 0.70]

# Vg ライン（PMOS 用：|Vg|）
Vg_list_p_abs = [0.30, 0.40, 0.50, 0.60, 0.70]

# サブスレッショルド
nfac = 1.5
I0   = 1e-12

# ===========================================
#  物理定数
# ===========================================
q    = 1.602e-19
kB   = 1.380649e-23
eps0 = 8.854e-12
eps_ox = 3.9 * eps0
eps_si = 11.7 * eps0

ni = 1.0e16
Vt = kB * T / q

# ===========================================
#  Vth 計算（長チャネル近似）
# ===========================================
Cox   = eps_ox / tox
phi_f = Vt * np.log(Na / ni)

Vfb_n = 0.0
Vth_n = Vfb_n + 2*phi_f + np.sqrt(4*eps_si*q*Na*phi_f) / Cox

Vfb_p = 0.0
Vth_p = -Vth_n  # 対称デバイスを仮定

print(f"[INFO] nMOS Vth ≈ {Vth_n:.3f} V, pMOS Vth ≈ {Vth_p:.3f} V")

# ===========================================
#  長チャネル Id(Vd) モデル（大きさ）
# ===========================================
def Id_long_vd_mag(Vov, Vd, mu, Cox, W, Lch, nfac, I0):
    """
    Vov = Vg - Vth (>0) を入力として Id 大きさを返す。
    """
    if Vov <= 0:
        return I0 * np.exp(Vov / (nfac * Vt)) * (Vd / 0.1)

    beta = mu * Cox * (W / Lch)
    Vdsat = Vov

    if Vd < Vdsat:
        return beta * (Vov * Vd - 0.5 * Vd**2)
    else:
        return 0.5 * beta * Vov**2

# ===========================================
#  nMOS: Vd–Id
# ===========================================
Vd_list = np.linspace(Vd_start, Vd_stop, Nvd)
Id_n_curves = []

for Vg in Vg_list_n:
    Vov = Vg - Vth_n
    Id_list_for_Vg = [
        Id_long_vd_mag(Vov, Vd, mu_n, Cox, W, Lch, nfac, I0)
        for Vd in Vd_list
    ]
    Id_n_curves.append(np.array(Id_list_for_Vg))

Id_n_curves = np.array(Id_n_curves)

# ---- プロット（nMOS, linear）----
plt.figure(figsize=(6,4))
for i, Vg in enumerate(Vg_list_n):
    plt.plot(Vd_list, Id_n_curves[i], marker="o", markersize=3,
             label=f"Vg={Vg:.2f} V")
plt.xlabel("Vd [V]")
plt.ylabel("Id [A]")
plt.title("1D nMOSFET Vd–Id (linear)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("fig/mosfet_vdid_nmos_linear.png", dpi=300)
plt.show()

# ---- プロット（nMOS, semi-log）----
plt.figure(figsize=(6,4))
for i, Vg in enumerate(Vg_list_n):
    plt.semilogy(Vd_list, Id_n_curves[i] + 1e-20, marker="o", markersize=3,
                 label=f"Vg={Vg:.2f} V")
plt.xlabel("Vd [V]")
plt.ylabel("Id [A] (log)")
plt.title("1D nMOSFET Vd–Id (semi-log)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("fig/mosfet_vdid_nmos_semilog.png", dpi=300)
plt.show()

# ===========================================
#  pMOS: |Vsd|–|Id|
# ===========================================
Id_p_curves = []

for Vg_abs in Vg_list_p_abs:
    # 実際には Vg = -Vg_abs で動かす
    Vov_abs = Vg_abs - abs(Vth_p)
    Id_list_for_Vg = [
        Id_long_vd_mag(Vov_abs, Vd, mu_p, Cox, W, Lch, nfac, I0)
        for Vd in Vd_list
    ]
    Id_p_curves.append(np.array(Id_list_for_Vg))

Id_p_curves = np.array(Id_p_curves)

# ---- プロット（pMOS, linear）----
plt.figure(figsize=(6,4))
for i, Vg_abs in enumerate(Vg_list_p_abs):
    plt.plot(Vd_list, Id_p_curves[i], marker="o", markersize=3,
             label=f"|Vg|={Vg_abs:.2f} V")
plt.xlabel("|Vsd| [V]")
plt.ylabel("|Id| [A]")
plt.title("1D pMOSFET Vd–Id (linear, magnitude)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("fig/mosfet_vdid_pmos_linear.png", dpi=300)
plt.show()

# ---- プロット（pMOS, semi-log）----
plt.figure(figsize=(6,4))
for i, Vg_abs in enumerate(Vg_list_p_abs):
    plt.semilogy(Vd_list, Id_p_curves[i] + 1e-20, marker="o", markersize=3,
                 label=f"|Vg|={Vg_abs:.2f} V")
plt.xlabel("|Vsd| [V]")
plt.ylabel("|Id| [A] (log)")
plt.title("1D pMOSFET Vd–Id (semi-log, magnitude)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("fig/mosfet_vdid_pmos_semilog.png", dpi=300)
plt.show()

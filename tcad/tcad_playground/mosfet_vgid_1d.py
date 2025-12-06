import numpy as np
import matplotlib.pyplot as plt

# ===========================================
#  ユーザー設定パラメータ（ここを変えればOK）
# ===========================================

# 電源電圧（Id–Vg では Vds_lin の上限の目安）
Vdd = 1.0          # [V]

# 温度
T = 300.0          # [K]

# デバイス寸法
W   = 1e-6         # [m]
Lch = 1e-6         # [m]

# 酸化膜厚・ドーピング
tox = 3e-9         # [m]
Na  = 1e21         # [1/m^3]  p-type body

# 移動度
mu_n = 0.05        # [m^2/Vs]  nMOS
mu_p = 0.05        # [m^2/Vs]  pMOS

# Id–Vg 用 Vds（小さめの線形領域）
Vds_lin = 0.1      # [V]

# Vg スイープ範囲
Vg_start_n = -0.2
Vg_stop_n  = 0.8
Nvg_n      = 41

Vg_start_p = 0.0    # pMOS は 0 → -0.8V へ
Vg_stop_p  = -0.8
Nvg_p      = 41

# サブスレッショルド
nfac = 1.5
I0   = 1e-12       # [A] Vg ≈ Vth 付近の基準電流

# ===========================================
#  物理定数
# ===========================================
q    = 1.602e-19
kB   = 1.380649e-23
eps0 = 8.854e-12
eps_ox = 3.9 * eps0
eps_si = 11.7 * eps0

ni = 1.0e16        # [1/m^3] 簡易値

Vt = kB * T / q

# ===========================================
#  Vth 計算（長チャネル近似）
# ===========================================
Cox   = eps_ox / tox
phi_f = Vt * np.log(Na / ni)

# nMOS
Vfb_n = 0.0
Vth_n = Vfb_n + 2*phi_f + np.sqrt(4*eps_si*q*Na*phi_f) / Cox

# pMOS（対称デバイスを仮定して |Vth_p| = Vth_n）
Vfb_p = 0.0
Vth_p = -Vth_n

print(f"[INFO] nMOS Vth ≈ {Vth_n:.3f} V, pMOS Vth ≈ {Vth_p:.3f} V")

# ===========================================
#  長チャネル Id(Vg) モデル（大きさを返す）
# ===========================================
def Id_long_vg_mag(Vov, Vds, mu, Cox, W, Lch, nfac, I0):
    """
    Vov = Vg - Vth (>0) を入力として Id 大きさを返す。
    サブスレッショルドでは I0 * exp(Vov/(nfac*Vt)) を使う。
    """
    # サブスレッショルド
    if Vov <= 0:
        return I0 * np.exp(Vov / (nfac * Vt)) * (Vds / 0.1)

    beta = mu * Cox * (W / Lch)
    Vdsat = Vov

    if Vds < Vdsat:
        # 線形領域
        return beta * (Vov * Vds - 0.5 * Vds**2)
    else:
        # 飽和
        return 0.5 * beta * Vov**2


# ===========================================
#  nMOS Vg–Id
# ===========================================
Vg_list_n = np.linspace(Vg_start_n, Vg_stop_n, Nvg_n)
Id_n = []

for Vg in Vg_list_n:
    Vov = Vg - Vth_n
    Id_val = Id_long_vg_mag(Vov, Vds_lin, mu_n, Cox, W, Lch, nfac, I0)
    Id_n.append(Id_val)

Id_n = np.array(Id_n)

# ===========================================
#  pMOS Vg–Id（Vg は負方向へスイープ）
#  プロットでは負の Vg をそのまま横軸に使う
# ===========================================
Vg_list_p = np.linspace(Vg_start_p, Vg_stop_p, Nvg_p)  # 0 → -0.8
Id_p = []

for Vg in Vg_list_p:
    # pMOS のオーバードライブ Vov_p = Vsg - |Vth_p|
    # ここでは対称モデルで Vov_abs ≈ |Vg| - |Vth_p|
    Vov_abs = abs(Vg) - abs(Vth_p)
    Id_val = Id_long_vg_mag(Vov_abs, Vds_lin, mu_p, Cox, W, Lch, nfac, I0)
    Id_p.append(Id_val)

Id_p = np.array(Id_p)

# ===========================================
#  nMOS: Vg–Id プロット
# ===========================================
plt.figure(figsize=(6,4))
plt.plot(Vg_list_n, Id_n, marker="o")
plt.xlabel("Vg [V]")
plt.ylabel("Id [A]")
plt.title("1D nMOSFET Vg–Id (linear)")
plt.grid(True)
plt.tight_layout()
plt.savefig("fig/mosfet_vgid_nmos_linear.png", dpi=300)
plt.show()

plt.figure(figsize=(6,4))
plt.semilogy(Vg_list_n, Id_n + 1e-20, marker="o")
plt.xlabel("Vg [V]")
plt.ylabel("Id [A] (log)")
plt.title("1D nMOSFET Vg–Id (semi-log)")
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig("fig/mosfet_vgid_nmos_semilog.png", dpi=300)
plt.show()

# ===========================================
#  pMOS: Vg–Id プロット（Vg は負）
# ===========================================
plt.figure(figsize=(6,4))
plt.plot(Vg_list_p, Id_p, marker="o")
plt.xlabel("Vg [V]")     # 負の Vg
plt.ylabel("|Id| [A]")
plt.title("1D pMOSFET Vg–Id (linear, magnitude)")
plt.grid(True)
plt.tight_layout()
plt.savefig("fig/mosfet_vgid_pmos_linear.png", dpi=300)
plt.show()

plt.figure(figsize=(6,4))
plt.semilogy(Vg_list_p, Id_p + 1e-20, marker="o")
plt.xlabel("Vg [V]")
plt.ylabel("|Id| [A] (log)")
plt.title("1D pMOSFET Vg–Id (semi-log, magnitude)")
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig("fig/mosfet_vgid_pmos_semilog.png", dpi=300)
plt.show()

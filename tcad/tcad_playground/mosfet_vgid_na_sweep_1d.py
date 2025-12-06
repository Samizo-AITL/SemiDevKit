import numpy as np
import matplotlib.pyplot as plt
import os

# =========================================================
#  MOSFET Vg–Id (1D) Na スイープ
#   - 長チャネル MOSFET の簡易モデル
#   - nMOS / pMOS 両対応
#   - linear / log の両方を 1 本で出力
#   - 出力：
#       fig/mosfet_vgid_na_sweep_nmos_linear.png
#       fig/mosfet_vgid_na_sweep_nmos_semilog.png
#       fig/mosfet_vgid_na_sweep_pmos_linear.png
#       fig/mosfet_vgid_na_sweep_pmos_semilog.png
# =========================================================

# -------------------------
#  ユーザー設定
# -------------------------
T        = 300.0                  # [K]
tox      = 3e-9                   # gate oxide thickness [m]

Na_list  = [1e20, 1e21, 1e22]     # 基板ドーピング（絶対値）[1/m^3]

W        = 1e-6                   # [m]
L        = 1e-6                   # [m]
mu_n     = 0.05                   # [m^2/Vs] nMOS 有効移動度
mu_p     = 0.02                   # [m^2/Vs] pMOS 有効移動度

# Vg スイープ条件
Vg_min_n = -0.4
Vg_max_n =  0.8
Vg_min_p =  0.4    # pMOS は負バイアスに降りていくので逆向きに取る
Vg_max_p = -0.8
Nvg      = 121

Vd_n     =  0.05   # nMOS のドレイン電圧 [V]
Vd_p     = -0.05   # pMOS のドレイン電圧 [V]

FIG_DIR  = "fig"

# -------------------------
#  物理定数
# -------------------------
q    = 1.602e-19
kB   = 1.380649e-23
eps0 = 8.854e-12

eps_ox = 3.9 * eps0
eps_si = 11.7 * eps0

ni = 1e16               # [1/m^3] ここでは T 依存は無視

# =========================================================
#  MOSFET モデル関数
# =========================================================
def calc_cox(tox):
    """ゲート酸化膜容量密度 Cox [F/m^2]"""
    return eps_ox / tox

def calc_vth_mag(Nsub, T, tox):
    """
    Vth の絶対値を計算（nMOS と pMOS で ± だけ変える）
      |Vth| = 2φF + γ * sqrt(2φF)
    とし、Vfb ≈ 0, Vsb = 0 とする。
    """
    Vt = kB * T / q
    phi_F = Vt * np.log(Nsub / ni)
    Cox = calc_cox(tox)
    gamma = np.sqrt(2.0 * q * eps_si * Nsub) / Cox
    Vth_mag = 2.0 * phi_F + gamma * np.sqrt(2.0 * phi_F)
    return Vth_mag

def id_vs_vg_nmos(Vg_array, Nsub, T, tox, mu, W, L, Vd):
    """
    nMOS の Id–Vg
    - ドレイン電圧 Vd > 0
    - subthreshold は簡易指数で近似
    """
    Cox = calc_cox(tox)
    Vth = +calc_vth_mag(Nsub, T, tox)
    Vt  = kB * T / q

    Id = np.zeros_like(Vg_array)

    for i, Vg in enumerate(Vg_array):
        Vgt = Vg - Vth
        if Vgt <= 0:
            # 簡易サブスレショルド
            Id[i] = 1e-12 * np.exp(Vgt / (1.5 * Vt))
        else:
            if Vd < Vgt:  # 線形領域
                Id[i] = mu * Cox * (W / L) * (Vgt * Vd - 0.5 * Vd**2)
            else:         # 飽和
                Id[i] = 0.5 * mu * Cox * (W / L) * Vgt**2

    return Id, Vth

def id_vs_vg_pmos(Vg_array, Nsub, T, tox, mu, W, L, Vd):
    """
    pMOS の Id–Vg
    - ドレイン電圧 Vd < 0
    - nMOS と対称なモデルを使い、符号だけ反転
    """
    # nMOS の式に変換して計算（|Id| を求めた後で符号を付ける）
    Cox = calc_cox(tox)
    Vth_mag = calc_vth_mag(Nsub, T, tox)
    Vth_p = -Vth_mag
    Vt  = kB * T / q

    Id = np.zeros_like(Vg_array)

    for i, Vg in enumerate(Vg_array):
        Vgt = Vg - Vth_p  # ここでは Vth_p < 0
        if Vgt >= 0:
            # オフ側（nMOS と対称にするため符号を逆転させる）
            Id[i] = -1e-12 * np.exp(-Vgt / (1.5 * Vt))
        else:
            # 有効オーバードライブ領域（|Vgt| > 0）
            Vgt_abs = -Vgt     # > 0
            Vd_abs  = -Vd      # > 0
            if Vd_abs < Vgt_abs:
                Id_abs = mu * Cox * (W / L) * (Vgt_abs * Vd_abs - 0.5 * Vd_abs**2)
            else:
                Id_abs = 0.5 * mu * Cox * (W / L) * Vgt_abs**2
            Id[i] = -Id_abs     # pMOS は Id < 0 とする

    return Id, Vth_p

# =========================================================
#  nMOS: linear / log
# =========================================================
os.makedirs(FIG_DIR, exist_ok=True)

Vg_n = np.linspace(Vg_min_n, Vg_max_n, Nvg)

# --- nMOS linear ---
plt.figure(figsize=(6,4))
for Na in Na_list:
    Id, Vth = id_vs_vg_nmos(Vg_n, Na, T, tox, mu_n, W, L, Vd_n)
    label = f"Na = {Na:.1e} m$^{{-3}}$ (Vth={Vth:.2f} V)"
    plt.plot(Vg_n, Id, label=label)

plt.xlabel("Vg [V]")
plt.ylabel("Id [A]")
plt.title(f"nMOS Vg–Id (Na sweep, linear, Vd = {Vd_n} V)")
plt.grid(True)
plt.legend()
plt.tight_layout()

out_path = os.path.join(FIG_DIR, "mosfet_vgid_na_sweep_nmos_linear.png")
plt.savefig(out_path, dpi=300)
print(f"[INFO] saved: {out_path}")
plt.show()

# --- nMOS log ---
plt.figure(figsize=(6,4))
for Na in Na_list:
    Id, Vth = id_vs_vg_nmos(Vg_n, Na, T, tox, mu_n, W, L, Vd_n)
    Id_abs = np.maximum(Id, 1e-20)
    plt.plot(Vg_n, Id_abs, label=f"Na = {Na:.1e} m$^{{-3}}$")

plt.xlabel("Vg [V]")
plt.ylabel("|Id| [A]")
plt.yscale("log")
plt.title(f"nMOS Vg–Id (Na sweep, log, Vd = {Vd_n} V)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()

out_path = os.path.join(FIG_DIR, "mosfet_vgid_na_sweep_nmos_semilog.png")
plt.savefig(out_path, dpi=300)
print(f"[INFO] saved: {out_path}")
plt.show()

# =========================================================
#  pMOS: linear / log
# =========================================================
Vg_p = np.linspace(Vg_min_p, Vg_max_p, Nvg)  # 正 → 負 に降りる sweep

# --- pMOS linear ---
plt.figure(figsize=(6,4))
for Na in Na_list:
    Id, Vth_p = id_vs_vg_pmos(Vg_p, Na, T, tox, mu_p, W, L, Vd_p)
    label = f"Na = {Na:.1e} m$^{{-3}}$ (Vth={Vth_p:.2f} V)"
    plt.plot(Vg_p, Id, label=label)

plt.xlabel("Vg [V]")
plt.ylabel("Id [A]")
plt.title(f"pMOS Vg–Id (Na sweep, linear, Vd = {Vd_p} V)")
plt.grid(True)
plt.legend()
plt.tight_layout()

out_path = os.path.join(FIG_DIR, "mosfet_vgid_na_sweep_pmos_linear.png")
plt.savefig(out_path, dpi=300)
print(f"[INFO] saved: {out_path}")
plt.show()

# --- pMOS log ---
plt.figure(figsize=(6,4))
for Na in Na_list:
    Id, Vth_p = id_vs_vg_pmos(Vg_p, Na, T, tox, mu_p, W, L, Vd_p)
    Id_abs = np.maximum(np.abs(Id), 1e-20)
    plt.plot(Vg_p, Id_abs, label=f"Na = {Na:.1e} m$^{{-3}}$")

plt.xlabel("Vg [V]")
plt.ylabel("|Id| [A]")
plt.yscale("log")
plt.title(f"pMOS Vg–Id (Na sweep, log, Vd = {Vd_p} V)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()

out_path = os.path.join(FIG_DIR, "mosfet_vgid_na_sweep_pmos_semilog.png")
plt.savefig(out_path, dpi=300)
print(f"[INFO] saved: {out_path}")
plt.show()

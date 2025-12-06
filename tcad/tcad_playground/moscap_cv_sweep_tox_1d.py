import numpy as np
import matplotlib.pyplot as plt
import os

# =========================================================
#  MOSCAP C–V (1D) tox スイープ
#   - 非線形 Poisson（可変誘電率）
#   - tox を複数値でスイープ
#   - 図保存：fig/moscap_cv_tox_sweep.png
# =========================================================

# -------------------------
#  ユーザー設定
# -------------------------
T        = 300.0           # [K]
tsi      = 97e-9           # Si 厚さ [m]
Na_sub   = 1e21            # p-sub (nMOS 相当) [1/m^3]
Nmesh    = 401             # メッシュ数
Vg_min   = -0.4
Vg_max   =  0.4
Nvg      = 41

# tox をスイープするリスト [m]
TOX_LIST = [2e-9, 3e-9, 4e-9]

FIG_DIR  = "fig"
FIG_NAME = "moscap_cv_tox_sweep.png"

# -------------------------
#  物理定数
# -------------------------
q    = 1.602e-19
kB   = 1.380649e-23
Vt   = kB * T / q
eps0 = 8.854e-12

eps_ox = 3.9 * eps0
eps_si = 11.7 * eps0

ni = 1e16                 # [1/m^3]

max_iter = 200
alpha    = 0.1
tol      = 1e-6

# =========================================================
#  Poisson ソルバ & ρ(ψ)
# =========================================================
def build_mesh(tox):
    """toxごとにメッシュ＆εプロファイルを生成"""
    L = tox + tsi
    x = np.linspace(0.0, L, Nmesh)
    dx = x[1] - x[0]
    eps = np.where(x < tox, eps_ox, eps_si)
    mask_si = (x >= tox)
    return x, dx, eps, mask_si, L

def solve_poisson_eps(x, eps, rho, psi_left, psi_right):
    N = len(x)
    dx = x[1] - x[0]

    A = np.zeros((N, N))
    b = np.zeros(N)

    eps_ip = np.zeros(N)
    eps_im = np.zeros(N)
    eps_ip[:-1] = 0.5 * (eps[:-1] + eps[1:])
    eps_im[1:]  = eps_ip[:-1]

    for i in range(1, N-1):
        A[i, i-1] = -eps_im[i] / dx**2
        A[i, i]   =  (eps_ip[i] + eps_im[i]) / dx**2
        A[i, i+1] = -eps_ip[i] / dx**2
        b[i]      = -rho[i]

    A[0, :] = 0.0
    A[0, 0] = 1.0
    b[0]    = psi_left

    A[-1, :]  = 0.0
    A[-1,-1]  = 1.0
    b[-1]     = psi_right

    psi = np.linalg.solve(A, b)
    return psi

def charge_density(psi, Nd_minus_Na):
    eta_n = np.clip( psi / Vt, -40.0, 40.0)
    eta_p = np.clip(-psi / Vt, -40.0, 40.0)
    n = ni * np.exp(eta_n)
    p = ni * np.exp(eta_p)
    rho = q * (p - n + Nd_minus_Na)
    return rho

def solve_nonlinear(Vg, psi_init, x, eps, Nd_minus_Na):
    psi_right = 0.0
    psi = psi_init.copy()

    for it in range(max_iter):
        rho = charge_density(psi, Nd_minus_Na)
        psi_new = solve_poisson_eps(x, eps, rho, psi_left=Vg, psi_right=psi_right)
        diff = psi_new - psi
        err  = np.max(np.abs(diff))
        psi += alpha * diff
        if err < tol:
            break
    return psi

# =========================================================
#  tox ごとの C–V を計算
# =========================================================
def compute_cv_for_tox(tox):
    # メッシュなど構築
    x, dx, eps, mask_si, L = build_mesh(tox)

    # ドーピング（p-sub, nMOS 相当）
    Nd_minus_Na = np.zeros_like(x)
    Nd_minus_Na[mask_si] = -Na_sub

    # 初期値（Vg = 0 の線形 Poisson）
    rho_lin = q * Nd_minus_Na
    psi_init = solve_poisson_eps(x, eps, rho_lin, psi_left=0.0, psi_right=0.0)

    psi = psi_init.copy()
    Qs_list = []

    Vg_list = np.linspace(Vg_min, Vg_max, Nvg)

    for Vg in Vg_list:
        psi = solve_nonlinear(Vg, psi, x, eps, Nd_minus_Na)
        rho = charge_density(psi, Nd_minus_Na)

        Qs = np.trapz(rho[mask_si], x[mask_si])
        Qs_list.append(Qs)

    Qs_array = np.array(Qs_list)
    dV = Vg_list[1] - Vg_list[0]
    C = -np.gradient(Qs_array, dV)      # F/m^2
    C_uF_cm2 = C * 1e2                  # μF/cm^2 に変換

    return Vg_list, C_uF_cm2

# =========================================================
#  メイン：tox スイープしてプロット
# =========================================================
plt.figure(figsize=(6,4))

for tox in TOX_LIST:
    Vg, C = compute_cv_for_tox(tox)
    label = f"tox = {tox*1e9:.1f} nm"
    plt.plot(Vg, C, marker="o", label=label)

plt.xlabel("Vg [V]")
plt.ylabel("C [μF/cm$^2$]")
plt.title("MOSCAP C–V (1D, tox sweep)")
plt.grid(True)
plt.legend()
plt.tight_layout()

os.makedirs(FIG_DIR, exist_ok=True)
out_path = os.path.join(FIG_DIR, FIG_NAME)
plt.savefig(out_path, dpi=300)
plt.show()

print(f"[INFO] saved: {out_path}")

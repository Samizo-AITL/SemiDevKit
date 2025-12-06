import numpy as np
import matplotlib.pyplot as plt
import os

# =========================================================
#  MOSCAP C–V (1D) — nMOS & pMOS 両対応版
#   - 非線形 Poisson（可変誘電率）
#   - 収束安定化（exp クリップ & アンダーリラックス）
#   - 図保存：fig/moscap_cv_nmos_pmos.png
# =========================================================

# -------------------------
#  ユーザー設定
# -------------------------
T       = 300.0      # 温度 [K]
tox     = 3e-9       # Oxide 厚さ [m]
tsi     = 97e-9      # Si 厚さ [m]
Na_sub  = 1e21       # p-sub（nMOS 用）[1/m^3]
Nd_sub  = 1e21       # n-sub（pMOS 用）[1/m^3]

Nmesh   = 401        # メッシュ数
Vg_min  = -0.4
Vg_max  =  0.4
Nvg     = 41

FIG_DIR  = "fig"
FIG_NAME = "moscap_cv_nmos_pmos.png"

# -------------------------
#  物理定数
# -------------------------
q    = 1.602e-19
kB   = 1.380649e-23
Vt   = kB * T / q               # ≒ 0.0259 V
eps0 = 8.854e-12

eps_ox = 3.9 * eps0
eps_si = 11.7 * eps0

ni = 1e16                       # [1/m^3] ≒ 10^10 cm^-3

# -------------------------
#  メッシュ & 誘電率
# -------------------------
L = tox + tsi
x = np.linspace(0.0, L, Nmesh)
dx = x[1] - x[0]

eps = np.where(x < tox, eps_ox, eps_si)
mask_si = (x >= tox)            # Si 域マスク

# =========================================================
# 1) Poisson ソルバ（線形）
# =========================================================
def solve_poisson_eps(x, eps, rho, psi_left, psi_right):
    N = len(x)
    dx = x[1] - x[0]

    A = np.zeros((N, N))
    b = np.zeros(N)

    # eps at i+1/2, i-1/2
    eps_ip = np.zeros(N)
    eps_im = np.zeros(N)
    eps_ip[:-1] = 0.5 * (eps[:-1] + eps[1:])
    eps_im[1:]  = eps_ip[:-1]

    for i in range(1, N-1):
        A[i, i-1] = -eps_im[i] / dx**2
        A[i, i]   =  (eps_ip[i] + eps_im[i]) / dx**2
        A[i, i+1] = -eps_ip[i] / dx**2
        b[i]      = -rho[i]

    # Dirichlet 境界条件
    A[0, :] = 0.0
    A[0, 0] = 1.0
    b[0]    = psi_left

    A[-1, :]  = 0.0
    A[-1, -1] = 1.0
    b[-1]     = psi_right

    psi = np.linalg.solve(A, b)
    return psi

# =========================================================
# 2) ρ(ψ) — exp を安全化（オーバーフロー防止）
# =========================================================
def charge_density(psi, Nd_minus_Na):
    # ψ/Vt をクリップして exp のオーバーフローを防止
    eta_n = np.clip( psi / Vt, -40.0, 40.0)
    eta_p = np.clip(-psi / Vt, -40.0, 40.0)

    n = ni * np.exp(eta_n)
    p = ni * np.exp(eta_p)

    rho = q * (p - n + Nd_minus_Na)
    return rho

# =========================================================
# 3) 非線形 Poisson ソルバ
# =========================================================
max_iter = 200
alpha    = 0.1      # アンダーリラックス
tol      = 1e-6

def solve_nonlinear(Vg, psi_init, Nd_minus_Na):
    psi_right = 0.0
    psi = psi_init.copy()

    for it in range(max_iter):
        rho = charge_density(psi, Nd_minus_Na)
        psi_new = solve_poisson_eps(x, eps, rho,
                                    psi_left=Vg,
                                    psi_right=psi_right)
        diff = psi_new - psi
        err  = np.max(np.abs(diff))

        psi += alpha * diff

        if err < tol:
            break

    return psi

# =========================================================
# 4) MOSCAP C–V を計算（nMOS / pMOS）
# =========================================================
def compute_CV(mode="nmos"):
    """
    mode = "nmos": p-type substrate (Na>0)
    mode = "pmos": n-type substrate (Nd>0)
    """
    Nd_minus_Na = np.zeros_like(x)

    if mode == "nmos":
        # p-sub: Nd - Na = -Na
        Nd_minus_Na[mask_si] = -Na_sub
    elif mode == "pmos":
        # n-sub: Nd - Na = +Nd
        Nd_minus_Na[mask_si] = +Nd_sub
    else:
        raise ValueError("mode must be 'nmos' or 'pmos'.")

    # 初期値：線形 Poisson（Vg = 0）
    rho_lin = q * Nd_minus_Na
    psi_init = solve_poisson_eps(x, eps, rho_lin,
                                 psi_left=0.0,
                                 psi_right=0.0)

    psi = psi_init.copy()
    Qs_list = []

    Vg_list = np.linspace(Vg_min, Vg_max, Nvg)

    for Vg in Vg_list:
        psi = solve_nonlinear(Vg, psi, Nd_minus_Na)
        rho = charge_density(psi, Nd_minus_Na)

        # Si 部分の体積電荷を積分 → 表面電荷密度 [C/m^2]
        Qs = np.trapz(rho[mask_si], x[mask_si])
        Qs_list.append(Qs)

    Qs_array = np.array(Qs_list)
    dV = Vg_list[1] - Vg_list[0]

    # C = -dQs/dVg  [F/m^2]
    C = -np.gradient(Qs_array, dV)

    # [F/m^2] → [μF/cm^2]
    C_uF_cm2 = C * 1e2

    return Vg_list, C_uF_cm2

# =========================================================
# 5) nMOS & pMOS の C–V を計算
# =========================================================
Vg_n, C_n = compute_CV("nmos")
Vg_p, C_p = compute_CV("pmos")

# =========================================================
# 6) 図を保存
# =========================================================
plt.figure(figsize=(6, 4))
plt.plot(Vg_n, C_n, 'o-', label="nMOS")
plt.plot(Vg_p, C_p, 's-', label="pMOS")

plt.xlabel("Vg [V]")
plt.ylabel("C [μF/cm$^2$]")
plt.title("MOSCAP C–V (1D, nMOS & pMOS)")
plt.grid(True)
plt.legend()
plt.tight_layout()

os.makedirs(FIG_DIR, exist_ok=True)
plt.savefig(os.path.join(FIG_DIR, FIG_NAME), dpi=300)
plt.show()

print(f"[INFO] saved: {os.path.join(FIG_DIR, FIG_NAME)}")

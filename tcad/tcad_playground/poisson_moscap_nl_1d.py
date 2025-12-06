import numpy as np
import matplotlib.pyplot as plt

# =========================
#  非線形 Poisson MOSCAP (1D)
#  SiO2 + p型 Si
# =========================

# ---- 物理定数 ----
q    = 1.602e-19
kB   = 1.380649e-23
T    = 300.0
Vt   = kB * T / q                 # 熱電圧 ≒ 0.0259 V
eps0 = 8.854e-12
eps_ox = 3.9 * eps0               # SiO2
eps_si = 11.7 * eps0              # Si

ni = 1.0e16                       # [1/m^3] ≒ 1e10 cm^-3（簡易値）

# ---- 構造パラメータ ----
tox = 3e-9                        # oxide 厚さ [m]
tsi = 97e-9                       # Si 厚さ [m]
L   = tox + tsi                   # 全長 [m]

N = 401                           # メッシュ点
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# ---- 誘電率プロファイル eps(x) ----
eps = np.where(x < tox, eps_ox, eps_si)

# ---- ドーピング (Si 部分だけ p型) ----
Na = 1e21                         # [1/m^3] ≒ 1e15 cm^-3（控えめ）
Nd_minus_Na = np.zeros_like(x)
Nd_minus_Na[x >= tox] = -Na       # p型: Nd - Na < 0

# ---- 境界条件（ゲート電圧） ----
Vg = 0.1                          # ゲート電圧 [V]（小さめにして収束させる）
psi_left  = Vg
psi_right = 0.0

# =========================================================
#  可変 eps 版 Poisson ソルバ（線形）
#  d/dx( eps dpsi/dx ) = -rho
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
    eps_im[1:]  = eps_ip[:-1].copy()

    for i in range(1, N - 1):
        A[i, i - 1] = -eps_im[i] / dx**2
        A[i, i]     =  (eps_ip[i] + eps_im[i]) / dx**2
        A[i, i + 1] = -eps_ip[i] / dx**2
        b[i] = -rho[i]

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
#  ρ(ψ) を計算する関数（非線形部分）
# =========================================================
def charge_density(psi):
    # 非縮退・平衡近似の簡易モデル
    # n, p は Si 部分で支配的。SiO2 部分では実際にはキャリア ~ 0 だが、
    # ここでは計算を簡単にするため全領域で同じ式を使う。
    n = ni * np.exp( psi / Vt)
    p = ni * np.exp(-psi / Vt)
    rho = q * (p - n + Nd_minus_Na)
    return rho

# =========================================================
#  非線形 Poisson を反復で解く
# =========================================================

# 初期値：線形 Poisson 解を使うと安定しやすい
rho_lin = q * Nd_minus_Na
psi = solve_poisson_eps(x, eps, rho_lin, psi_left, psi_right)

max_iter = 100
alpha = 0.2                       # アンダーリラックス（0<alpha<=1）
tol = 1e-6

for it in range(max_iter):
    rho = charge_density(psi)
    psi_new = solve_poisson_eps(x, eps, rho, psi_left, psi_right)

    diff = psi_new - psi
    err = np.max(np.abs(diff))
    print(f"iter {it:3d}: err = {err:.3e}")

    psi = psi + alpha * diff

    if err < tol:
        print(">>> 収束しました")
        break
else:
    print(">>> 収束しませんでした（max_iter 到達）")

# =========================================================
#  結果表示
# =========================================================
print("\n代表点:")
for pos in [0, tox/2, tox, tox + tsi/2, L]:
    idx = np.argmin(np.abs(x - pos))
    region = "OX" if x[idx] < tox else "Si"
    print(f"x={x[idx]*1e9:6.1f} nm ({region}), psi={psi[idx]:.4f} V")

# プロット
plt.figure(figsize=(6, 4))
plt.plot(x * 1e9, psi)
plt.axvline(tox * 1e9, color="k", linestyle="--", linewidth=1)
plt.text(tox * 1e9 / 2, psi.max() * 0.9, "SiO2", ha="center")
plt.text((tox * 1e9 + L * 1e9) / 2, psi.max() * 0.9, "Si", ha="center")

plt.xlabel("x [nm]")
plt.ylabel("psi [V]")
plt.title("Nonlinear MOSCAP Poisson (1D)")
plt.grid(True)
plt.tight_layout()
plt.show()

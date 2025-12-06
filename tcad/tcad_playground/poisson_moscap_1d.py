import numpy as np
import matplotlib.pyplot as plt

# ===== 定数 =====
q    = 1.602e-19
eps0 = 8.854e-12
eps_ox = 3.9 * eps0        # SiO2
eps_si = 11.7 * eps0       # Si

# ===== 構造パラメータ =====
tox = 3e-9                 # oxide thickness [m]
tsi = 97e-9                # Si thickness [m]
L   = tox + tsi            # total length

N = 401                    # mesh points
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# ===== 誘電率プロファイル eps(x) =====
eps = np.where(x < tox, eps_ox, eps_si)

# ===== ドーピングと電荷 rho(x) =====
Na = 1e23                  # p-type in Si [1/m^3] ~ 1e17 cm^-3

doping = np.zeros_like(x)
doping[x >= tox] = -Na     # Si 部分だけ p型（符号に注意）

rho = q * doping           # rho = q(p - n + Nd - Na) → ここでは単純化

# ===== 境界条件（ゲート電圧と基板） =====
Vg = 1.0                   # gate voltage [V]
psi_left  = Vg
psi_right = 0.0

# ===== Poisson: d/dx( eps dpsi/dx ) = -rho を FDM で離散化 =====
#   ( eps_{i+1/2} (psi_{i+1}-psi_i)/dx - eps_{i-1/2} (psi_i-psi_{i-1})/dx ) / dx = -rho_i
# → -eps_im / dx^2 * psi_{i-1} + (eps_ip + eps_im)/dx^2 * psi_i - eps_ip/dx^2 * psi_{i+1} = -rho_i

Npts = N
A = np.zeros((Npts, Npts))
b = np.zeros(Npts)

# セル境界の誘電率（i±1/2）
eps_ip = np.zeros(Npts)    # eps at i+1/2
eps_im = np.zeros(Npts)    # eps at i-1/2
eps_ip[:-1] = 0.5 * (eps[:-1] + eps[1:])
eps_im[1:]  = eps_ip[:-1].copy()

# 内部点
for i in range(1, Npts - 1):
    A[i, i - 1] = -eps_im[i] / dx**2
    A[i, i]     =  (eps_ip[i] + eps_im[i]) / dx**2
    A[i, i + 1] = -eps_ip[i] / dx**2
    b[i] = -rho[i]

# Dirichlet BC：x=0, x=L
A[0, :] = 0.0
A[0, 0] = 1.0
b[0]    = psi_left

A[-1, :]  = 0.0
A[-1, -1] = 1.0
b[-1]     = psi_right

# ===== 解く =====
psi = np.linalg.solve(A, b)

# ===== 結果表示 =====
print("代表点:")
for pos in [0, tox/2, tox, tox + tsi/2, L]:
    idx = np.argmin(np.abs(x - pos))
    region = "OX" if x[idx] < tox else "Si"
    print(f"x={x[idx]*1e9:6.1f} nm ({region}), psi={psi[idx]:.4f} V")

# ===== プロット =====
plt.figure(figsize=(6,4))
plt.plot(x*1e9, psi)
plt.axvline(tox*1e9, color="k", linestyle="--", linewidth=1)
plt.text(tox*1e9/2, psi.max()*0.9, "SiO2", ha="center")
plt.text((tox*1e9 + L*1e9)/2, psi.max()*0.9, "Si", ha="center")

plt.xlabel("x [nm]")
plt.ylabel("psi [V]")
plt.title("1D MOSCAP Poisson (SiO2 + Si)")
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# --- 物理定数 ---
eps0 = 8.854e-12           # vacuum permittivity [F/m]
eps_si = 11.7 * eps0       # Si permittivity
q = 1.602e-19              # electron charge [C]

# --- メッシュ ---
L = 100e-9                 # 100 nm
N = 201
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# --- 境界条件 ---
psi_left = 0.0
psi_right = 1.0

# --- ドーピング → 空間電荷 ---
Na = 1e23                  # ~1e17 cm^-3
rho = -q * Na * np.ones_like(x)

# --- 行列 A とベクトル b ---
A = np.zeros((N, N))
b = np.zeros(N)

# 内部点
for i in range(1, N - 1):
    A[i, i - 1] = 1.0
    A[i, i]     = -2.0
    A[i, i + 1] = 1.0
    b[i] = -rho[i] * dx**2 / eps_si

# 左境界
A[0, :] = 0
A[0, 0] = 1
b[0] = psi_left

# 右境界
A[-1, :] = 0
A[-1, -1] = 1
b[-1] = psi_right

# --- 解く ---
psi = np.linalg.solve(A, b)

# --- 結果出力 ---
print("計算OK：代表点5つだけ表示")
for i in np.linspace(0, N-1, 5, dtype=int):
    print(f"x={x[i]*1e9:6.1f} nm   psi={psi[i]:.4f} V")

# --- プロット ---
plt.plot(x*1e9, psi)
plt.xlabel("x [nm]")
plt.ylabel("ψ [V]")
plt.title("1D Poisson (Simple FDM)")
plt.grid(True)
plt.show()

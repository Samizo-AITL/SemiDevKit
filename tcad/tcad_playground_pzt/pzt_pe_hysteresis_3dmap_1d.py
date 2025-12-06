#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import os

# ============================
# Create directory
# ============================
os.makedirs("fig", exist_ok=True)

# ============================
# Fine parameter sweep
# ============================
composition_fine = np.linspace(-0.10, 0.10, 40)    # Zr-rich → Ti-rich
anneal_fine = np.linspace(720, 760, 40)            # [°C]

# ============================
# Pm model (your P–E/loop trend)
# ============================
def get_Pm(comp, an):
    base = 42.0

    # Ti-rich increases Pm / Zr-rich decreases
    comp_effect = 1.5 * comp

    # anneal temp: peak at 740°C, symmetric decay
    anneal_effect = -0.02 * abs(an - 740)

    return base + comp_effect + anneal_effect


# ============================
# Generate mesh grid
# ============================
X, Y = np.meshgrid(anneal_fine, composition_fine)   # ← ここで axis を入れ替え
Z = np.zeros_like(X)

for i in range(len(composition_fine)):
    for j in range(len(anneal_fine)):
        Z[i, j] = get_Pm(Y[i, j], X[i, j])

# ============================
# Plot smooth 3D surface
# ============================
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

surface = ax.plot_surface(
    X, Y, Z,
    cmap=cm.viridis,
    edgecolor='none',
    antialiased=True
)

ax.set_xlabel("Anneal Temp [°C]")
ax.set_ylabel("Composition (Zr-rich → Ti-rich)")
ax.set_zlabel("Pm [µC/cm²]")
ax.set_title("Smoothed 3D Surface of Pm (Axes Swapped)")

fig.colorbar(surface, shrink=0.6, label="Pm [µC/cm²]")

# ============================
# Save PNG
# ============================
plt.tight_layout()
plt.savefig("fig/pzt_pm_surface.png", dpi=300)
plt.show()

print("Saved: fig/pzt_pm_surface.png")

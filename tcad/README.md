# 🧪 TCAD Playground — Device Physics Simulation

---

##  Links

### 📁 Top-level (TCAD)

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/tcad/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/tcad) |

---

This directory contains **lightweight 1D TCAD educational tools** for semiconductor device physics.

These modules help learners understand:
- ✔ Poisson equation  
- ✔ Drift–Diffusion transport  
- ✔ MOSFET I–V behavior  
- ✔ Ferroelectric device simulation（PZT / HfO₂）

---

## 📁 Directory Contents

```
tcad/
├── tcad_playground/        # Standard MOSFET & semiconductor physics simulations
│
└── tcad_playground_pzt/    # Ferroelectric (PZT/HfO₂) polarization & FE-FET analysis
```

### 🔬 TCAD / Device Physics Modules

| No. | Module | Focus | Description | Pages | Repo |
|----:|--------|-------|-------------|-------|------|
| 1 | **tcad_playground** | MOSFET / Semiconductor Physics | 1D device physics playground<br>Poisson & Drift–Diffusion solvers<br>MOS capacitor & MOSFET electrostatics | [Pages](https://samizo-aitl.github.io/SemiDevKit/tcad/tcad_playground/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/tcad/tcad_playground) |
| 2 | **tcad_playground_pzt** | Ferroelectric Devices | Ferroelectric material modeling<br>PZT / HfO₂ polarization (P–E)<br>Landau–Khalatnikov-based simulation | [Pages](https://samizo-aitl.github.io/SemiDevKit/tcad/tcad_playground_pzt/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/tcad/tcad_playground_pzt) |

---

## 🚀 How to Use

Example: Run MOSFET simulation
```bash
cd tcad_playground
python simulate_mosfet.py
```

Example: Run ferroelectric P–E simulation
```bash
cd tcad_playground_pzt
python simulate_fe_pe.py
```

---

## 📘 Documentation

Full explanations, derivations, and mathematical formulas are provided under:

👉 https://samizo-aitl.github.io/SemiDevKit/

---

## 📄 License

- Code: MIT  
- Text: CC BY  
- Figures: CC BY-NC  

---

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

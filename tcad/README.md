# 🧪 TCAD Playground — Device Physics Simulation

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

## 👤 Maintainer

Shinichi Samizo (Samizo-AITL)

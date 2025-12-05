---
layout: default
title: SemiDevKit/README.md
---

----

# SemiDevKit
### *Open Educational Toolkit for Semiconductor Device Modeling, SPICE Simulation, Reliability Analysis, and VLSI Physical Design*

SemiDevKit is a unified, open-source learning suite that covers the entire semiconductor device workflow:  
from **device physics** and **compact modeling (BSIM4)** to **SPICE analysis**, **reliability evaluation (NBTI/HCI)**, and **OpenLane-based physical design**.

It is designed for students, researchers, and engineers who want a practical and lightweight environment to explore the foundations of semiconductor devices and integrated circuit design.

---

## 📚 Features

### 🔹 Device Physics
- 1D Poisson & Drift–Diffusion solvers  
- MOSFET Id–Vd / Id–Vg characteristics  
- Ferroelectric P–E modeling (Landau–Khalatnikov)  

### 🔹 Compact Modeling (BSIM4)
- Automatic generation of BSIM4 model cards  
- Physical-parameter-based extraction workflow  
  (tox / Na / Vfb / μ0 / L / W)

### 🔹 SPICE Simulation
- DC characteristics (Id–Vd, Id–Vg)  
- AC characteristics (Cgg–Vg)  
- Device dimension scaling (L/W sweep)  
- Reliability degradation (NBTI & HCI)

### 🔹 VLSI Physical Design
- Lightweight OpenLane environment  
- Minimal example design (inverter)  
- Docker / WSL2 ready  
- Full RTL → GDSII educational flow

---

## 🧩 Repository Structure
```
SemiDevKit/
│
├── device_physics/
│   ├── TCAD_PLAYGROUND
│   └── TCAD_PLAYGROUND_PZT
│
├── compact_modeling/
│   └── Paramus
│
├── spice_analysis/
│   ├── BSIM4_ANALYZER_DC
│   ├── BSIM4_ANALYZER_CV
│   ├── BSIM4_ANALYZER_DIM
│   └── BSIM4_ANALYZER_RELIABILITY
│
├── physical_design/
│   └── OpenLane-Lite
│
└── docs/
    └── (Tutorials, theory notes, math formulas, examples)
```

---

## 🚀 Getting Started

### Requirements
- Python 3.10+  
- NumPy / SciPy / Matplotlib  
- ngspice  
- Docker (for OpenLane-Lite)  
- WSL2 (recommended for Windows users)

---

### Clone the repository
```bash
git clone https://github.com/Samizo-AITL/SemiDevKit.git
cd SemiDevKit
```

---

### Example: Run a SPICE DC simulation
```bash
cd spice_analysis/BSIM4_ANALYZER_DC/run
python run_vd.py
python run_vg.py
```

---

### Example: Run OpenLane-Lite flow
```bash
cd physical_design/OpenLane-Lite
./docker/run_flow.sh
```

---

## 📘 Documentation

Comprehensive tutorials, equations (MathJax), workflows, and examples will be provided under:

```
docs/
```

Including:
- Device physics background  
- Compact modeling theory  
- SPICE simulation techniques  
- Reliability mechanisms (NBTI/HCI)  
- OpenLane RTL-to-GDS educational flow  

---

## 🤝 Contributions

Contributions, bug reports, and feature requests are welcome.  
Please open an **Issue** or **Pull Request**.

---

## 📄 License

MIT License (or specify your preferred license).

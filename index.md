---
layout: default
title: SemiDevKit
---

# 🧪 SemiDevKit  
### *Open Educational Toolkit for Semiconductor Device Modeling, SPICE Simulation, Reliability Analysis, and VLSI Physical Design*

> **SemiDevKit** is a unified, open-source educational toolkit that spans the *entire semiconductor device workflow* —  
> from **device physics** and **compact modeling (BSIM4)** to **SPICE simulation**, **reliability analysis (NBTI / HCI)**,  
> and **OpenLane-based RTL-to-GDSII physical design**.

🎓 Designed for **students**, **researchers**, and **practicing engineers**  
🔧 Focused on **practical, lightweight, and reproducible** experimentation  
📦 Built with **Python, ngspice, and OpenLane**

---

## 🔗 Official Links

| 🌐 Language | GitHub Pages | GitHub Repository |
|------------|-------------|------------------|
| 🇺🇸 English | [![Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/) | [![Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main) |

---

## 📚 What You Can Learn with SemiDevKit

### 🔹 Device Physics
- 🧮 1D **Poisson** & **Drift–Diffusion** solvers  
- 📈 MOSFET **Vg–Id / Vd–Id** characteristics  
- ⚡ Ferroelectric **P–E modeling** (Landau–Khalatnikov)

---

### 🔹 Compact Modeling (BSIM4)
- 🧩 Automatic **BSIM4 model card generation**  
- 🧪 Physical-parameter-based extraction workflow  
  - tox / Na / Vfb / μ₀ / L / W  
- 🔁 TCAD → Compact Model consistency checks

---

### 🔹 SPICE Simulation
- 🔌 DC analysis: Vg–Id, Vd–Id  
- 🌊 AC / CV analysis: Vg–Cgg  
- 📐 Geometry scaling: L / W sweep  
- 🧯 Reliability degradation:
  - NBTI
  - HCI

---

### 🔹 VLSI Physical Design
- 🏗 Lightweight **OpenLane-Lite** environment  
- 🔁 Minimal example designs:
  - Inverter  
  - SPM (standard primitive module)  
- 🐳 Docker / 🪟 WSL2 ready  
- 🧭 Full **RTL → GDSII** educational flow

---

## 🧩 Repository Structure (Conceptual View)

```text
SemiDevKit/
│
├── device_physics/        (implemented in tcad/)
│   ├── TCAD_PLAYGROUND
│   └── TCAD_PLAYGROUND_PZT
│
├── compact_modeling/      (implemented in bsim/)
│   └── Paramus
│
├── spice_analysis/        (also under bsim/)
│   ├── BSIM4_ANALYZER_DC
│   ├── BSIM4_ANALYZER_CV
│   ├── BSIM4_ANALYZER_DIM
│   └── BSIM4_ANALYZER_RELIABILITY
│
├── physical_design/
│   ├── OpenLane-Lite
│   └── OpenLane-superstable
│
└── docs/
    └── Tutorials / Theory / Math / Examples
```

📌 **Note**: Actual folder mapping  
- Device physics / TCAD → `tcad/`  
- Compact modeling & SPICE → `bsim/`  
- Physical design → `openlane/`  
- Site & docs → `docs/`, `assets/`, `_includes/`, `_layouts/`

---

## 📁 Quick Navigation

| Module | GitHub Pages | Repository |
|------|--------------|------------|
| 🔬 **Device Physics / TCAD** | [Pages](https://samizo-aitl.github.io/SemiDevKit/tcad/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/tcad) |
| 🧩 **BSIM4 & SPICE Suite** | [Pages](https://samizo-aitl.github.io/SemiDevKit/bsim/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim) |
| 🏗  **OpenLane-Lite** | [Pages](https://samizo-aitl.github.io/SemiDevKit/openlane/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane) |
| 📘 **Documentation** | [Pages](https://samizo-aitl.github.io/SemiDevKit/docs/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/docs) |

---

## 🚀 Getting Started

### ✅ Requirements

- 🐍 Python 3.10+  
- NumPy / SciPy / Matplotlib  
- 🔌 ngspice  
- 🐳 Docker (for OpenLane-Lite)  
- 🪟 WSL2 (recommended on Windows)

---

### 📥 Clone the Repository

```bash
git clone https://github.com/Samizo-AITL/SemiDevKit.git
cd SemiDevKit
```

---

### ▶ Example: Run a SPICE DC Simulation

```bash
cd bsim/BSIM4_ANALYZER_DC/run
python run_vd.py
python run_vg.py
```

---

### ▶ Example: Run OpenLane-Lite Flow

```bash
cd openlane/openlane-lite
./docker/run_in_docker.sh
```

This will:
1. Launch the OpenLane 2023 container  
2. Use the included minimal `spm` design  
3. Execute the full RTL → GDSII flow  
4. Generate a verified `spm.gds` (Dec 2025)

---

## 📘 Documentation

All tutorials and theory notes are provided under:

```text
docs/
```

Including:
- 📐 Device physics fundamentals  
- 🧩 Compact modeling theory  
- 🔌 SPICE simulation techniques  
- 🧯 Reliability mechanisms (NBTI / HCI)  
- 🏗 OpenLane RTL-to-GDS educational flow  

---

## 👤 Author

| Item | Details |
|----|--------|
| 👨‍🔬 Name | **Shinichi Samizo** |
| 🧠 Expertise | Semiconductor devices (logic, memory, HV mixed-signal)<br>Thin-film piezo actuators (inkjet systems)<br>PrecisionCore printhead productization, BOM, ISO training |
| 💻 GitHub | [Samizo-AITL](https://github.com/Samizo-AITL) |

---

## 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/SemiDevKit/#---license)

| Component | License | Notes |
|---------|---------|------|
| 💻 Source Code | [**MIT License**](https://opensource.org/licenses/MIT) | Free use / modification |
| 📄 Text Materials | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) / [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | Attribution required |
| 🎨 Figures & Diagrams | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | Non-commercial only |
| 🔗 External References | Original license | Proper citation required |

---

## 💬 Feedback & Discussion

> Suggestions, improvements, and technical discussions are welcome!

[![GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/discussions)

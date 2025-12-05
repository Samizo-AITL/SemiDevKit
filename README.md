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


[![Back to Samizo-AITL Portal](https://img.shields.io/badge/Back%20to%20Samizo--AITL%20Portal-brightgreen)](https://samizo-aitl.github.io/en) 

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)

> 🆕 **Check the latest updates in the [ChangeLog](../revision_history.md).**  
> *Review all recent modifications in the [ChangeLog](../revision_history.md).*

<p align="right">
  <img src="https://img.shields.io/badge/Last%20Update-2025--08--15-orange" alt="Last Update">
  <a href="../revision_history.md">
    <img src="https://img.shields.io/badge/View-ChangeLog-blue?logo=markdown" alt="View ChangeLog">
  </a>
</p>

---

## 🔗 Official Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main) |

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

## 👤 **Author**

> Primary developer and author of this educational toolkit.  
> Professional background in semiconductor devices and inkjet actuators, creating learning materials that integrate theory, simulation, and practical engineering insights.

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **Education** | M.S. in Electrical and Electronic Engineering, Shinshu University |
| **Career** | Former Engineer at Seiko Epson Corporation (since 1997) |
| **Expertise** | Semiconductor devices (logic, memory, high-voltage mixed-signal)<br>Thin-film piezo actuators for inkjet systems<br>PrecisionCore printhead productization, BOM management, ISO training |
| **Email** | [![Email](https://img.shields.io/badge/Email-shin3t72%40gmail.com-red?style=for-the-badge&logo=gmail)](mailto:shin3t72@gmail.com) |
| **X (Twitter)** | [![X](https://img.shields.io/badge/X-@shin3t72-black?style=for-the-badge&logo=x)](https://x.com/shin3t72) |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 **License**

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/Edusemi-v4x/#-license)

> SemiDevKit adopts a hybrid licensing approach tailored to the nature of each component—source code, text materials, and graphical content.

| 📌 Item | License | Description |
|--------|----------|-------------|
| **Source Code** | [**MIT License**](https://opensource.org/licenses/MIT) | Free to use, modify, and redistribute |
| **Text Materials** | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) or [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | Attribution required; share-alike applies for BY-SA |
| **Figures & Diagrams** | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | Non-commercial use only |
| **External References** | Follow the original license | Cite the original source properly |

---

## 💬 **Feedback**

> Suggestions, improvements, and discussions are welcome via GitHub Discussions.

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)

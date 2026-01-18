---
layout: default
title: directory_structure
---

---

# 📁 Directory Structure Overview — SemiDevKit

This document describes the **recommended directory structure** of the **SemiDevKit** repository  
and explains the role of each top-level and module-level directory.

Understanding this structure will help you **navigate the toolkit, modify modules safely,  
and maintain reproducibility**.

---

## 🗂 1. Top-Level Layout

The top-level layout of SemiDevKit is organized as follows:

```
SemiDevKit/
│
├── 1_install.md
├── 2_setup.md
├── 3_usage.md
├── 4_license.md
├── 5_openlane_lite_usage.md
├── 6_troubleshooting.md
├── 7_faq.md
├── 8_directory_structure.md
│
├── tcad_playground/
├── tcad_playground_pzt/
├── bsim4_analyzer_dc/
├── bsim4_analyzer_cv/
├── bsim4_analyzer_dim/
├── bsim4_analyzer_reliability/
├── paramus_physical/
└── openlane_lite/
```

### 📌 Notes

- Markdown files (`1_install.md` … `8_directory_structure.md`) form the **official documentation flow**
- Each **technical module lives in its own directory**
- There are **no cross-module runtime dependencies**

---

## 🧪 2. Module-Level Structure

### 2.1 TCAD Playground

Lightweight **1D TCAD modeling** for MOSFETs, MOSCAPs, and Poisson equation studies.

```
tcad_playground/
├── fig/                   # Generated figures
├── mosfet_vdid_*.py       # VD–ID simulations
├── mosfet_vgid_*.py       # VG–ID simulations
├── moscap_cv_*.py         # C–V simulations
├── poisson_1d.py          # 1D Poisson solver
└── README.md
```

---

### 2.2 PZT Playground

Exploration of **ferroelectric PZT behavior**, including hysteresis and material effects.

```
tcad_playground_pzt/
├── fig/                       # Generated figures
├── pzt_pe_hysteresis_*.py     # P–E loop simulation
├── pzt_pm_surface_3dmap.py    # 3D polarization maps
├── pzt_se_butterfly_1d.py     # Strain–electric field behavior
└── README.md
```

---

### 2.3 BSIM4 Analyzer — DC

Automated **VG–ID / VD–ID DC sweep analysis** using BSIM4 and ngspice.

```
bsim4_analyzer_dc/
├── models/        # BSIM model cards
├── templates/     # SPICE netlist templates
├── run/           # Simulation scripts
├── plot/          # Plotting utilities
├── results/       # Generated results
└── README.md
```

---

### 2.4 BSIM4 Analyzer — CV

Capacitance extraction focusing on **physically meaningful Cgg–Vg** characteristics.

```
bsim4_analyzer_cv/
├── models/
├── template_cv.cir
├── run_cv.py
├── plot_cv.py
└── results/
```

---

### 2.5 BSIM4 Analyzer — DIM (L / W Sweep)

Analysis of **short-channel and geometry-dependent effects**.

```
bsim4_analyzer_dim/
├── models/
├── templates/
├── run/
├── plot/
└── results/
```

---

### 2.6 BSIM4 Reliability Analyzer

Modeling of **HCI (NMOS)** and **NBTI (PMOS)** degradation mechanisms.

```
bsim4_analyzer_reliability/
├── models/
├── templates/
├── run/
├── plot/
└── results/
```

---

### 2.7 Paramus Physical Edition

Generation of **BSIM4 model cards from physical parameters**.

```
paramus_physical/
├── modelcard/      # Generated model cards
├── physical/       # Physical parameter definitions
├── presets/        # Technology presets
├── paramus.py
└── README.md
```

---

### 2.8 OpenLane-Lite

Minimal **RTL → GDSII** digital implementation flow.

```
openlane_lite/
├── docker/         # Docker wrapper and image
├── scripts/        # Flow execution scripts
├── examples/       # Example designs
└── README.md
```

---

## 📐 3. Directory Rules and Conventions

To maintain clarity and reproducibility:

- Each module must remain **self-contained**
- Generated figures must be stored under **`fig/`**
- Scripts must **not write outside their module directory**
- Use consistent naming conventions (`snake_case`)
- Clean **`results/`** directories before publishing or sharing

---

## 🧭 4. Summary

Each module in SemiDevKit:

- Follows a **consistent directory structure**
- Supports **independent execution**
- Enables **reproducible experiments**
- Supports a full learning path from  
  **device physics → compact modeling → physical design**

---

📘 **This structure is intentional — do not modify it unless you know exactly what you are doing**

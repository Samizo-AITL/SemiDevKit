---
layout: default
title: directory_structure
---

----

# 8_directory_structure.md
# SemiDevKit — Directory Structure Overview

This document explains the recommended directory structure for the **SemiDevKit** repository
and describes the purpose of each module directory.

---

# 1. Top-Level Layout

```
SemiDevKit/
│
├── 1_install.md
├── 2_quickstart.md
├── 3_tutorials.md
├── 4_module_overview.md
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

---

# 2. Module-Level Structure

## 2.1 TCAD Playground

Lightweight TCAD modeling (MOSFET, MOSCAP, Poisson).

```
tcad_playground/
├── fig/
├── mosfet_vdid_*.py
├── mosfet_vgid_*.py
├── moscap_cv_*.py
├── poisson_1d.py
└── README.md
```

---

## 2.2 PZT Playground

Ferroelectric P–E / P–V / composition / anneal behavior exploration.

```
tcad_playground_pzt/
├── fig/
├── pzt_pe_hysteresis_*.py
├── pzt_pm_surface_3dmap.py
├── pzt_se_butterfly_1d.py
└── README.md
```

---

## 2.3 BSIM4 Analyzer — DC

Automated Vg–Id, Vd–Id sweep.

```
bsim4_analyzer_dc/
├── models/
├── templates/
├── run/
├── plot/
├── results/
└── README.md
```

---

## 2.4 BSIM4 Analyzer — CV

Extract Cgg–Vg only (physically meaningful).

```
bsim4_analyzer_cv/
├── models/
├── template_cv.cir
├── run_cv.py
├── plot_cv.py
└── results/
```

---

## 2.5 BSIM4 Analyzer — DIM (L/W Sweep)

Short-channel effect analysis vs. geometry.

```
bsim4_analyzer_dim/
├── models/
├── templates/
├── run/
├── plot/
└── results/
```

---

## 2.6 BSIM4 Reliability Analyzer

HCI (NMOS) / NBTI (PMOS) degradation modeling.

```
bsim4_analyzer_reliability/
├── models/
├── templates/
├── run/
├── plot/
└── results/
```

---

## 2.7 Paramus Physical Edition

Generate BSIM4 model cards from physical parameters.

```
paramus_physical/
├── modelcard/
├── physical/
├── presets/
├── paramus.py
└── README.md
```

---

## 2.8 OpenLane-Lite

Minimal OpenLane flow.

```
openlane_lite/
├── docker/
├── scripts/
├── examples/
└── README.md
```

---

# 3. Directory Rules

- Keep each module **self-contained**
- Use **fig/** for plots
- Scripts must not write outside module folder
- Maintain naming consistency (snake_case)
- Keep **results/** clean before publishing

---

# 4. Summary

Each module in SemiDevKit:
- Follows consistent structure  
- Has independent workflows  
- Ensures reproducibility  
- Enables device → model → design learning

# 10_changelog.md
# SemiDevKit — ChangeLog / Release Notes

This document summarizes all updates, improvements, and structural changes made to **SemiDevKit**.
It is intended for version tracking, documentation updates, and module maintenance.

---

# 📌 Version 0.1.0 — Initial Structured Release
**Date:** 2025-01-01  
**Status:** Public Alpha

### 🔧 Core Repository Setup
- Created top-level documentation files:
  - 1_install.md
  - 2_quickstart.md
  - 3_tutorials.md
  - 4_module_overview.md
  - 5_openlane_lite_usage.md
  - 6_troubleshooting.md
  - 7_faq.md
  - 8_directory_structure.md
  - 9_glossary.md
- Added standardized directory structure for all modules.

---

# 🚀 Module Updates

## 1. TCAD Playground (MOSFET/MOSCAP/Poisson)
- Added MOSFET Id–Vd / Id–Vg sweep models.
- Implemented MOSCAP CV analysis.
- Added Poisson 1D solver.
- Added auto-generated figures under `fig/`.

---

## 2. PZT Playground
- Added P–E hysteresis closed-loop model.
- Added composition and anneal-temperature variation models.
- Added Pm surface map & butterfly (S–E) curve generator.

---

## 3. BSIM4 Analyzer — DC
- Implemented VGID / VDID sweep automation.
- Added Vth (gmmax), gmmax, Idlin, Idsat extraction.
- Added `.csv`, `.png`, `.dat`, `.log` export formats.

---

## 4. BSIM4 Analyzer — CV
- Added physically correct NMOS/PMOS CV extraction.
- Implemented Cgg-only extraction policy (no partitioned caps).
- Automated batch simulation for LT/RT/HT.

---

## 5. BSIM4 Analyzer — DIM (L/W Sweep)
- Added DIM auto-generation for L/W sweeps.
- Added short-channel effect modeling:
  - Vth roll-off
  - DIBL scaling
  - Mobility degradation
  - RDSW width dependency
- Automated VGID / VDID plots per geometry.

---

## 6. BSIM4 Reliability Analyzer
- Added HCI (NMOS) and NBTI (PMOS) reliability framework.
- Included ΔVth, ΔId lin/sat, gm shifts.
- Added stress & VGID template separation.
- Added Python-based degradation modeling (t > 0).

---

## 7. Paramus Physical Edition
- Added physical-to-BSIM4 model-card generator.
- Added support for:
  - tox
  - Na
  - Vfb
  - mobility μ0
  - L/W geometry
- Added preset JSON-based technology definitions.

---

## 8. OpenLane-Lite
- Added minimal OpenLane environment with scripts:
  - docker/run_in_docker.sh
  - scripts/run_flow.sh
- Added example designs.
- Added PDK folder auto-check.

---

# 📁 Documentation Updates

### New documents added:
- **Changelog (this file)**
- Glossary of semiconductor and modeling terms.
- Directory structure guidelines.
- Completed FAQ and troubleshooting guide.
- Added hybrid license summary references.

---

# 🛠 Planned for Next Release (v0.2.0)

### ✔ Documentation
- Example workflows (TCAD → BSIM → SPICE → Layout).
- Architecture diagram of the entire SemiDevKit flow.
- Module comparison table.

### ✔ Features
- TCAD 2D extensions (Poisson/DD-lite).
- BSIM4 parameter sweeping automation.
- Reliability Arrhenius model support (temperature dependence).
- OpenLane-Lite: add post-GDS analysis step.

### ✔ Repository
- Add CI checks for Python formatting.
- Add simulation validation script set.

---

# 🏁 Summary
SemiDevKit v0.1.0 establishes:
- A unified modeling-to-layout educational ecosystem
- Reproducible workflows
- A stable documentation framework
- Consistent directory and naming rules

Further releases will enhance physical accuracy, automation, and usability.

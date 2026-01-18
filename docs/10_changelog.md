---
layout: default
title: changelog
---

---

# 🧾 ChangeLog / Release Notes — SemiDevKit

This document summarizes all **updates, improvements, and structural changes** made to  
**SemiDevKit**. It is intended for **version tracking, documentation maintenance, and module evolution**.

---

## 📌 Version 0.1.0 — Initial Structured Release

**Release Date:** 2025-01-01  
**Status:** Public Alpha

This release establishes the **foundation of SemiDevKit** as a unified educational and research toolkit  
spanning **device physics, compact modeling, reliability, and physical design**.

---

## 🔧 Core Repository Setup

- Introduced a structured documentation set:
  - `1_install.md`
  - `2_setup.md`
  - `3_usage.md`
  - `4_license.md`
  - `5_openlane_lite_usage.md`
  - `6_troubleshooting.md`
  - `7_faq.md`
  - `8_directory_structure.md`
  - `9_glossary.md`
  - `10_changelog.md`
- Defined a **standardized directory structure** for all modules
- Enforced consistent naming conventions and self-contained module design

---

## 🚀 Module Updates

### 1. TCAD Playground (MOSFET / MOSCAP / Poisson)

- Added MOSFET **Id–Vd** and **Id–Vg** sweep models
- Implemented MOSCAP **C–V analysis**
- Added a **1D Poisson equation solver**
- Enabled automatic figure generation under `fig/`

---

### 2. PZT Playground

- Implemented **P–E hysteresis closed-loop model**
- Added composition- and anneal-temperature-dependent models
- Added:
  - Polarization surface maps
  - Butterfly (S–E) curve generation

---

### 3. BSIM4 Analyzer — DC

- Implemented automated **VG–ID / VD–ID** sweeps
- Added extraction of:
  - Threshold voltage (gmmax method)
  - gmmax
  - Idlin / Idsat
- Enabled export of:
  - `.csv`
  - `.png`
  - `.dat`
  - `.log`

---

### 4. BSIM4 Analyzer — CV

- Implemented physically consistent **NMOS / PMOS C–V extraction**
- Adopted **Cgg-only extraction policy** (no artificial capacitance partitioning)
- Added automated batch simulations for:
  - Low temperature (LT)
  - Room temperature (RT)
  - High temperature (HT)

---

### 5. BSIM4 Analyzer — DIM (L / W Sweep)

- Implemented automated **geometry sweep generation**
- Added modeling of short-channel effects:
  - Vth roll-off
  - DIBL scaling
  - Mobility degradation
  - RDSW width dependence
- Automated VG–ID / VD–ID plotting per geometry

---

### 6. BSIM4 Reliability Analyzer

- Added reliability frameworks for:
  - **HCI (NMOS)**
  - **NBTI (PMOS)**
- Implemented extraction of:
  - ΔVth
  - ΔId (linear / saturation)
  - gm degradation
- Separated **stress** and **measurement** templates
- Added Python-based time-dependent degradation modeling (t > 0)

---

### 7. Paramus Physical Edition

- Introduced **physical-to-BSIM4 model-card generator**
- Added support for physical parameters:
  - Oxide thickness (`tox`)
  - Channel doping (`Na`)
  - Flatband voltage (`Vfb`)
  - Low-field mobility (`μ0`)
  - Channel geometry (L / W)
- Added JSON-based **technology preset definitions**

---

### 8. OpenLane-Lite

- Added minimal OpenLane backend environment
- Implemented Docker-based execution with:
  - `docker/run_in_docker.sh`
  - `scripts/run_flow.sh`
- Added example RTL designs
- Added automatic PDK directory validation

---

## 📘 Documentation Enhancements

- Added **ChangeLog** (this document)
- Added a comprehensive **Glossary of semiconductor and modeling terms**
- Added **Directory Structure Overview**
- Completed **FAQ** and **Troubleshooting Guide**
- Added references to the **hybrid licensing model**

---

## 🛠 Planned for Next Release (v0.2.0)

### 📘 Documentation
- End-to-end example workflows  
  *(TCAD → BSIM → SPICE → Layout)*
- Architecture and workflow diagrams for the full SemiDevKit flow
- Module comparison and capability tables

---

### ⚙️ Features
- TCAD **2D extensions** (Poisson / DD-lite)
- BSIM4 **parameter sweep automation**
- Reliability **Arrhenius temperature modeling**
- OpenLane-Lite: post-GDS analysis and reporting

---

### 🧩 Repository Infrastructure
- Continuous Integration (CI) for Python formatting and linting
- Automated simulation validation scripts

---

## 🏁 Summary

SemiDevKit **v0.1.0** establishes:

- A unified **device-to-layout educational ecosystem**
- Fully reproducible modeling and simulation workflows
- A stable, extensible documentation framework
- Consistent directory, naming, and execution rules

Future releases will focus on **physical accuracy, automation depth, and usability improvements**.

---

📌 **End of ChangeLog**

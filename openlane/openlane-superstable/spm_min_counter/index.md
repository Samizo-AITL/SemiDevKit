---
layout: default
title: spm_min_counter
---

# spm_min_counter — Minimal RTL → GDS Reference Flow

A **pre-declared, self-authored minimal RTL flow**  
validated through **OpenLane (superstable)** on **SKY130A**.

This project demonstrates a *clean, modification-free*  
**RTL → GDS completion**, serving as a **baseline physical design reference**.

---

##  Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-superstable/spm_min_counter) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-superstable/spm_min_counter) |

---

## 🎯 Purpose

This design exists to **prove flow stability**, not functionality richness.

- Validate **OpenLane superstable** using a *designer-authored* RTL
- Confirm **complete RTL → GDS generation** with **no flow customization**
- Establish a **pre-declared baseline** for future comparative experiments

All design intent, constraints, and structure were defined **before execution**,  
explicitly avoiding post-hoc tuning or interpretation.

---

## 🧩 Design Overview

| Item | Description |
|------|------------|
| Function | Free-running binary counter |
| FSM | None |
| Clock domains | Single |
| Reset | Synchronous, active-low |
| Macros / SRAM | Not used |

RTL implementation:  
➡ `rtl/spm_min_counter.v`

The logic is intentionally minimal to isolate **physical design behavior**  
from architectural complexity.

---

## ⏱ Pre-declared Constraints

| Parameter | Value |
|----------|-------|
| Clock period | 10 ns (100 MHz) |
| Core utilization | 30 % |
| Aspect ratio | 1.0 |

OpenLane configuration file:  
➡ `openlane/config.tcl`

These constraints were fixed **prior to running the flow**  
and were not adjusted based on results.

---

## 📦 Flow Results

- **RTL → GDS**: ✅ Completed successfully
- **CTS**: Stable clock tree construction
- **Routing**: No congestion-induced blockage observed
- **DRC/LVS**: Pass (OpenLane default checks)

Flow summary:  
➡ `run_log/flow_summary.md`

Final layout database:  
➡ `results/spm_min_counter.gds`

---

## 🖼 Layout Visualization (KLayout)

The following PNGs are provided for **layer-wise inspection without requiring KLayout**:

| File | Description |
|------|------------|
| `1_overview.png` | Floorplan & row overview |
| `2_full.png` | All layers (debug view) |
| `3_metal.png` | Metal routing focus |
| `4_cts_clock.png` | Clock tree distribution |
| `5_pnd.png` | Power / ground network |
| `6_cell_density.png` | Cell & diffusion density |
| `7_min_rtl.png` | RTL signal correspondence |

Location:  
➡ `results/`

---

## 🧠 Design Intent Notes

- Acts as a **minimal physical load generator**
- Suitable for observing:
  - placement regularity
  - CTS topology
  - routing layer usage
- Designed as a **baseline reference**, prior to introducing:
  - higher clock frequencies
  - wider datapaths
  - FSM or control-heavy logic

All subsequent variants will be derived **relative to this design**.

---

## 📍 Position within SemiDevKit

```
openlane/
└─ openlane-superstable/
├─ spm_reference/ # OpenLane reference (Golden)
└─ spm_min_counter/ # Self-authored minimal RTL
```


This project complements the reference flow by validating  
**designer-authored RTL behavior under identical tool conditions**.

---

## ✅ Takeaway

> **If this design fails, the flow is unstable.**  
> **If this design passes, the flow is usable.**

`spm_min_counter` defines the **zero-point** for all future OpenLane-based exploration.

---

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |


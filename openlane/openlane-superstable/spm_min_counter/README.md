# spm_min_counter — Minimal RTL Flow

A **pre-declared minimal RTL → GDS flow** using  
**OpenLane (superstable)** and **SKY130A**,  
designed to verify flow stability with a self-authored RTL.

---

##  Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-superstable/spm_min_counter) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-superstable/spm_min_counter) |

---

## 🎯 Purpose

- Verify **OpenLane superstable** flow using a *self-authored* RTL
- Confirm **RTL → GDS completion** without any flow modification
- Establish a **baseline reference** for subsequent design variations

This design is intentionally minimal and declared **before execution**  
to eliminate post-hoc interpretation.

---

## 🧩 Design Overview

| Item | Description |
|----|------------|
| Function | Free-running counter |
| FSM | None |
| Clock domains | Single |
| Reset | Synchronous, active-low |
| Macros / SRAM | Not used |

RTL source:  
➡ [`rtl/spm_min_counter.v`](./rtl/spm_min_counter.v)

---

## ⏱ Constraints (Pre-declared)

| Parameter | Value |
|---------|------|
| Clock period | 10 ns (100 MHz) |
| Core utilization | 30 % |
| Aspect ratio | 1.0 |

OpenLane configuration:  
➡ [`openlane/config.tcl`](./openlane/config.tcl)

---

## 📦 Flow Execution Result

- **GDS generation**: ✅ Successful
- **CTS behavior**: Stable
- **Routing**: No congestion blocking observed

Summary report:  
➡ [`run_log/flow_summary.md`](./run_log/flow_summary.md)

Final artifact:  
➡ [`results/spm_min_counter.gds`](./results/spm_min_counter.gds)

---

## 🧠 Notes

- This design serves as a **minimal load generator** for physical design observation
- Intended as a **baseline** before introducing:
  - higher clock frequency
  - wider datapath
  - FSM / control logic

Subsequent variants will be added as parallel experiments.

---

## 📍 Position in SemiDevKit

This flow is located under:

```
openlane/
└─ openlane-superstable/
├─ spm_reference/ (Golden reference)
└─ spm_min_counter/ (Self-authored minimal design)
```

It complements the reference flow by validating **designer-authored RTL** behavior.


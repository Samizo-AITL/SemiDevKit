# spm_min_counter — Minimal RTL → GDS Reference Flow

A **pre-declared, self-authored minimal RTL flow**
validated through **OpenLane (superstable)** on **SKY130A**.

This project demonstrates a *clean, modification-free*
**RTL → GDS completion**, serving as a **baseline physical design reference**.

---

## 🔗 Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-superstable/spm_min_counter | https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-superstable/spm_min_counter |

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
| Reset | None (simulation-only initialization) |
| Macros / SRAM | Not used |

RTL implementation:
`rtl/spm_min_counter.v`

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
`openlane/config.tcl`

These constraints were fixed **prior to running the flow**
and were not adjusted based on results.

---

## 📦 Flow Results

- **RTL → GDS**: Completed successfully
- **CTS**: Stable clock tree construction
- **Routing**: No congestion-induced blockage observed
- **DRC/LVS**: Pass (OpenLane default checks)

Final layout database:
`results/spm_min_counter.gds`

---

## 🖼 Layout Visualization (KLayout)

<img src="https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/1_overview.png" width="80%"/>

---

## 🧪 RTL Simulation (Testbench & GTKWave)

This project includes a **standalone RTL simulation environment**
to validate logical behavior *before* physical design.

```
spm_min_counter/
├─ rtl/
├─ sim/
│  ├─ tb_spm_min_counter.v
│  ├─ run.sh
│  └─ wave/
```

Simulation is executed via:

```
cd sim
./run.sh
```

---

## 📈 GTKWave – RTL Counter Behavior

<img src="https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/gtkwave.png" width="80%"/>

---

## 📍 Position within SemiDevKit

```
openlane/
└─ openlane-superstable/
   ├─ spm_reference/
   └─ spm_min_counter/
```

---

## 👤 Author

Name: Shinichi Samizo
GitHub: https://github.com/Samizo-AITL

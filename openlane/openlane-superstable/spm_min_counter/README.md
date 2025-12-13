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
| Reset | None (simulation-only initialization) |
| Macros / SRAM | Not used |

RTL implementation:
`rtl/spm_min_counter.v`

---

## ⏱ Pre-declared Constraints

| Parameter | Value |
|----------|-------|
| Clock period | 10 ns (100 MHz) |
| Core utilization | 30 % |
| Aspect ratio | 1.0 |

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

All layout images are provided as PNG for **browser-based inspection**.

### Embedded Overview

<img src="https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/1_overview.png" width="80%"/>

### Direct Links to All KLayout PNGs

- Floorplan overview  
  https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/1_overview.png

- Full layer view  
  https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/2_full.png

- Metal routing focus  
  https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/3_metal.png

- Clock tree (CTS)  
  https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/4_cts_clock.png

- Power / ground network  
  https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/5_pnd.png

- Cell & diffusion density  
  https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/6_cell_density.png

- RTL signal correspondence  
  https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/7_min_rtl.png

---

## 🧪 RTL Simulation (Testbench & GTKWave)

Standalone RTL simulation is provided **without modifying the OpenLane RTL**.

```
spm_min_counter/
├─ rtl/
├─ sim/
│  ├─ tb_spm_min_counter.v
│  ├─ run.sh
│  └─ wave/
```

Simulation run:

```
cd sim
./run.sh
```

---

## 📈 GTKWave – RTL Counter Behavior

Waveform snapshot:

<img src="https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/gtkwave.png" width="80%"/>

Direct link:
https://raw.githubusercontent.com/Samizo-AITL/SemiDevKit/main/openlane/openlane-superstable/spm_min_counter/results/gtkwave.png

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

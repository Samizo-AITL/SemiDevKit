---
layout: default
title: openLane-lite
---

----

# OpenLane-Lite  
Minimal educational version of the OpenLane RTL-to-GDSII flow.

OpenLane-Lite is a simplified, lightweight environment designed for **education, training, and conceptual understanding** of the ASIC physical design flow.  
It preserves the *core essence* of OpenLane while removing heavy components such as full PDKs and industrial-scale flow automation.

---

##  Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-lite/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-lite) |

---

## 🎯 Purpose

This repository is intended for:

- Students and engineers learning digital physical design  
- Lightweight experimentation without a full PDK installation  
- Demonstrating the RTL → Synthesis → APR → GDSII pipeline  
- Running inside **WSL2** or **Docker** with minimal setup  

This project **does not** replace the official OpenLane toolchain;  
instead, it provides a *small, easy-to-run sandbox* suitable for learning and prototyping.

---

## 📌 ✔ NEW (Dec 2025) — Verified GDSII Output Generation

This repository has been **successfully validated** by producing a full GDSII layout using the sample design **spm**.

### ✔ Verification Conditions
- **Environment**: WSL2 (Ubuntu-20.04)  
- **Runner**: Docker-based OpenLane container — commit `a35b64a`  
- **PDK**: sky130A enabled via `volare enable 0fe599b2afb6...`  
- **Flow**: Full RTL → Synthesis → Floorplan → APR → Signoff → GDS  

### ✔ Result
The following GDS was generated without errors:

spm.gds

The GDS has been visually verified in **KLayout**, confirming:
- Standard-cell placement  
- Global & detailed routing  
- PDN rails  
- IO placement  
- Final DRC/LVS/ANT checks all clean  

This confirms that **OpenLane-Lite is a fully functional minimal learning flow** that can execute a *complete* ASIC physical design pipeline.

---

## 📦 Repository Contents

```
OpenLane-Lite/
├── config/                 # Minimal example config for the flow
│   ├── config.tcl
│
├── designs/
│   └── example_inv/        # Simple inverter sample design
│       ├── src/
│       ├── sim/
│       └── inv.v
│
├── docker/
│   ├── Dockerfile
│   ├── run_in_docker.sh    # Start flow inside container
│
├── docs/
│   ├── wsl2_setup.md
│   └── usage.md
│
├── scripts/
│   └── run_flow.sh         # Main script for launching the mini-flow
│
├── spm.gds                 # Verified GDS output (Dec 2025)
└── README.md
```

---

## ✨ Features

- ✔ Minimal, easy-to-understand OpenLane-like flow  
- ✔ Standalone example design (**inverter**)  
- ✔ Docker-based execution for consistency  
- ✔ WSL2 support (Ubuntu recommended)  
- ✔ Very small footprint for teaching and experimentation  
- ✔ **Verified to generate GDSII** using `spm` (Dec 2025)  

---

## 🎉 Why OpenLane-Lite Is Valuable for Learning

OpenLane-Lite provides a complete miniaturized ASIC design experience without requiring a full industrial setup.

Despite being lightweight, the flow allows users to:
- ✔ Inspect real chip layouts (GDSII) using KLayout
- ✔ Verify digital logic behavior through Verilog testbenches
- ✔ View waveforms interactively with GTKWave
- ✔ Follow the full RTL → Synthesis → APR → GDSII cycle in a minimal environment
- ✔ Run entirely on WSL2 or Docker with almost no setup effort
  
This makes OpenLane-Lite an ideal platform for:
- Education & training
- University coursework
- Hackathons & workshops
- Self-study and experimentation
- Research prototypes
- In short, you can learn the entire ASIC design flow — from logic simulation to physical layout — in a compact, easy-to-run sandbox.

---

## ❌ This repository intentionally excludes:

These components are *not provided*, by design, to maintain lightweight operation:

- ❌ **PDKs**  
- ❌ **Toolchain binaries from OpenLane**  
- ❌ **Full APR flow automation**  
- ❌ **Run artifacts (logs, reports, DEF, etc.) except spm.gds**  
- ❌ **Machine-specific settings**  

Users must install their own **PDK** if they wish to run full backend flows.

---

## 🚀 Getting Started

### 1. Clone the repository
git clone https://github.com/Samizo-AITL/SemiDevKit.git
cd SemiDevKit/openlane/openlane-lite

---

## 🐳 Option A — Run using Docker (Recommended)

cd docker
./run_in_docker.sh

This launches a clean minimal environment sufficient for educational usage.

---

## 🪟 Option B — Run inside WSL2

See:

docs/wsl2_setup.md

---

## ▶ Running the Flow

Inside Docker or WSL2:

./scripts/run_flow.sh

This performs:

1. RTL import  
2. Minimal synthesis  
3. Floorplan  
4. APR (simplified)  
5. Final layout steps  

---

## 🧪 Example Design: Inverter

designs/example_inv/

Useful for:
- hierarchy understanding  
- verifying RTL → netlist  
- small-scale APR experiments  

---

## 📘 Documentation

Located in the `/docs` directory:

- wsl2_setup.md — Setup instructions for WSL2  
- usage.md — How to run the flow  

More educational materials may be added.

---

## OpenLane-Lite GDS Layout (KLayout View)

The following images show the physical layout generated by the
OpenLane-Lite implementation in SemiDevKit.

---

### ● Full Standard-Cell Layout

<img src="https://samizo-aitl.github.io/SemiDevKit/assets/openlane-lite/layout_full.png" width="80%">

This view shows the full placed-and-routed standard cell array.

---

### ● Diffusion + Poly Layer View

<img src="https://samizo-aitl.github.io/SemiDevKit/assets/openlane-lite/layout_diff_poly.png" width="80%">

This layer view highlights transistor active regions (diffusion) and gate
structures (poly), allowing users to understand MOSFET-level placement
inside the standard cells.

---

### ▶ GTKWave View (RTL Simulation Output)

The following screenshot shows the `inv_tb.vcd` waveform displayed in **GTKWave**,  
generated from the example inverter testbench.

<img src="https://samizo-aitl.github.io/SemiDevKit/assets/openlane-lite/gtkwave.png" width="80%">

---

## 🤝 Acknowledgements

This project draws inspiration from the official **OpenLane** toolchain:  
https://github.com/The-OpenROAD-Project/OpenLane/

OpenLane-Lite is an independent educational project,  
not affiliated with the original authors.

---

## 👤 Author

| Item | Details |
|----|--------|
| 👨‍🔬 Name | **Shinichi Samizo** |
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

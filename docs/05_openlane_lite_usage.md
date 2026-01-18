---
layout: default
title: openlane_lite_usage
---

---

# 🏗 OpenLane-Lite Usage Guide — SemiDevKit

This document explains how to run **OpenLane-Lite**, the minimal **RTL-to-GDSII** backend flow included in **SemiDevKit**.

The goal of OpenLane-Lite is to provide a **lightweight, reproducible, and educational** physical design flow that demonstrates the core concepts of modern digital implementation without requiring a full commercial or production PDK setup.

---

## 📦 1. Requirements

OpenLane-Lite requires the following environment:

- 🐳 **Docker** (Linux or WSL2 recommended)
- 🛠 **make** (optional, but useful)
- 🐍 **Python 3.x** (for helper and analysis scripts)
- 🪟 **WSL2 Ubuntu** (required if running on Windows)

### ✔ Verify Docker installation

```bash
docker --version
docker run hello-world
```

If you see the message **“Hello from Docker!”**, Docker is functioning correctly.

---

## 📁 2. Directory Structure (Simplified)

The OpenLane-Lite module is organized as follows:

```
openlane/openlane-lite/
 ├ docker/
 │   ├ run_in_docker.sh        # Docker execution wrapper
 │   └ Dockerfile              # Minimal OpenLane environment
 ├ scripts/
 │   ├ run_flow.sh             # Main flow script
 │   ├ prepare_design.sh       # Design preparation helper
 │   └ extract_results.py      # Result extraction utility
 ├ designs/
 │   └ example_top/
 │       ├ config.tcl          # Design configuration
 │       ├ src/                # RTL source files
 │       └ runs/               # Generated run results
 ├ pdks/                       # Minimal educational PDK subset
 └ README.md
```

---

## ▶️ 3. Running the Flow

Move into the OpenLane-Lite directory:

```bash
cd openlane/openlane-lite
```

---

### 3.1 Basic Execution

Run the default example flow:

```bash
./docker/run_in_docker.sh ./scripts/run_flow.sh
```

This command executes the following steps:

1. RTL synthesis (Yosys)
2. Floorplanning
3. Placement
4. Clock Tree Synthesis (CTS)
5. Routing
6. GDSII export

📂 Results are generated under:

```
designs/<design-name>/runs/<timestamp>/
```

---

## 🧩 4. Running a Specific Design

To run a specific design directory, pass the design path explicitly.

### Example: bundled sample design

```bash
./docker/run_in_docker.sh ./scripts/run_flow.sh designs/example_top
```

### Example: custom design

```bash
./docker/run_in_docker.sh ./scripts/run_flow.sh ./designs/my_design
```

Each design directory must include:

- `config.tcl`
- `src/` (RTL files)

---

## ⚙️ 5. Editing the Configuration

Each design directory contains a **`config.tcl`** file that controls key physical design parameters, such as:

- Core utilization
- Power grid settings
- Clock period
- Routing layers
- Pin placement constraints

### Example snippet

```tcl
set ::env(DESIGN_NAME) "example_top"
set ::env(CLOCK_PERIOD) "10"
set ::env(FP_CORE_UTIL) "45"
```

After modifying the configuration, simply rerun the flow to apply changes.

---

## 📊 6. Extracting Results

A helper script is provided to summarize key metrics from a completed run.

```bash
python scripts/extract_results.py designs/example_top/runs/<timestamp>
```

This script extracts:

- ⏱ Timing summary
- 🔌 Power estimation
- 📐 Area utilization
- 🚫 DRC violation count
- 📄 GDS output location

---

## 🛠 7. Troubleshooting

### ❌ Docker cannot find device
→ Ensure Docker Desktop (Windows/macOS) or Docker Engine (Linux) is running.

---

### ❌ Permission denied when running scripts

```bash
chmod +x docker/run_in_docker.sh
chmod +x scripts/run_flow.sh
```

---

### ❌ No PDK found

Ensure the directory structure includes:

```
openlane-lite/pdks/
```

OpenLane-Lite ships with a **minimal PDK subset** intended for educational use only.

---

## 📝 8. Notes and Limitations

- Full OpenLane flows require complete PDKs (e.g. Sky130, GF180)
- OpenLane-Lite intentionally uses a **reduced configuration**
- The generated GDS files are compatible with standard viewers such as **KLayout**
- This flow is intended for **learning, experimentation, and prototyping**, not tape-out

---

🎯 **You have now completed the OpenLane-Lite flow**

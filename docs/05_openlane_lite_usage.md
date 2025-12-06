---
layout: default
title: openlane_lite_usage
---

----

# 5_openlane_lite_usage.md

# SemiDevKit — OpenLane‑Lite Usage Guide

This document explains how to run **OpenLane‑Lite**, the minimal RTL‑to‑GDSII flow included in **SemiDevKit**.  
The objective of OpenLane‑Lite is to provide a *lightweight, reproducible* backend flow for educational and research use.

---

# 1. Requirements

OpenLane‑Lite requires:

- **Docker** (Linux or WSL2 recommended)
- **make** (optional but useful)
- **Python 3.x** (for utility scripts)
- **WSL2 Ubuntu** if running on Windows

Verify Docker:

```bash
docker --version
docker run hello-world
```

If you see the “Hello from Docker!” message, Docker is working.

---

# 2. Directory Structure (Simplified)

```
openlane/openlane-lite/
 ├ docker/
 │   ├ run_in_docker.sh
 │   └ Dockerfile
 ├ scripts/
 │   ├ run_flow.sh
 │   ├ prepare_design.sh
 │   └ extract_results.py
 ├ designs/
 │   └ example_top/
 │       ├ config.tcl
 │       ├ src/
 │       └ runs/
 ├ pdks/
 └ README.md
```

---

# 3. Running the Flow

Move into the module:

```bash
cd openlane/openlane-lite
```

## 3.1 Basic execution

```bash
./docker/run_in_docker.sh ./scripts/run_flow.sh
```

This performs:

1. Synthesis (Yosys)
2. Floorplan
3. Placement
4. CTS
5. Routing
6. GDS export

Results appear under:

```
designs/<design-name>/runs/<timestamp>/
```

---

# 4. Running a Specific Design

Example:

```bash
./docker/run_in_docker.sh ./scripts/run_flow.sh designs/example_top
```

To run with a custom top module:

```bash
./docker/run_in_docker.sh ./scripts/run_flow.sh ./designs/my_design
```

---

# 5. Editing the Configuration

Each design folder contains a `config.tcl` that controls:

- Core utilization  
- Power grid  
- Clock periods  
- Routing layers  
- Pin placement  

Example snippet:

```tcl
set ::env(DESIGN_NAME) "example_top"
set ::env(CLOCK_PERIOD) "10"
set ::env(FP_CORE_UTIL) "45"
```

Modify values and rerun the flow.

---

# 6. Extracting Results

A helper script is included:

```bash
python scripts/extract_results.py designs/example_top/runs/<timestamp>
```

This extracts:

- Timing summary  
- Power  
- Area  
- DRC violations  
- GDS location  

---

# 7. Troubleshooting

### Docker cannot find device
→ Ensure Docker Desktop or Docker Engine is running.

### Permission denied on run_in_docker.sh
```bash
chmod +x docker/run_in_docker.sh
chmod +x scripts/run_flow.sh
```

### No PDK found
Ensure the directory structure is:

```
openlane-lite/pdks/...
```

The included flow uses a minimal subset of PDK files for educational use.

---

# 8. Notes

- Real OpenLane requires a complete PDK (Sky130, GF180, etc.)  
- OpenLane‑Lite uses a reduced configuration suitable for conceptual and educational flows  
- GDS output is compatible with common viewers such as KLayout


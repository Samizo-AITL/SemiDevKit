---
layout: default
title: usage
---

---

# ▶️ Usage Guide — SemiDevKit

This document explains how to **run the main tools included in SemiDevKit**, covering:

- 🧪 TCAD Playgrounds  
- 📐 BSIM4 Analyzers  
- 🧮 Paramus Physical Edition  
- 🏗 OpenLane-Lite (RTL → GDSII)

Make sure that **installation and setup are completed** before proceeding.

---

## 🧪 1. Running TCAD Playgrounds

### 1.1 MOSFET / MOSCAP Playground  
(`tcad_playground`)

This playground solves **1D Poisson and drift–diffusion models** for MOS devices.

```bash
cd tcad/tcad_playground
python mosfet_vgid_1d.py
python mosfet_vdid_1d.py
python moscap_cv_1d.py
```

📂 Output figures are saved in:

```
tcad/tcad_playground/fig/
```

---

### 1.2 PZT P–E Loop Playground  
(`tcad_playground_pzt`)

This playground simulates **ferroelectric polarization–electric field (P–E) hysteresis**.

```bash
cd tcad/tcad_playground_pzt
python pzt_pe_hysteresis_1d.py
```

📂 Figures are saved in:

```
tcad/tcad_playground_pzt/fig/
```

---

## 📐 2. Running BSIM4 Analyzers

### 2.1 DC Analyzer (VG–ID / VD–ID)

This analyzer evaluates **DC characteristics** using BSIM4 models and ngspice.

```bash
cd bsim/analyzer_dc
python run/run_vgid.py
python run/run_vdid.py
python plot/plot_vgid.py
python plot/plot_vdid.py
```

📂 Results are generated under:

```
bsim/analyzer_dc/results/
```

---

### 2.2 CV Analyzer (Cgg–Vg)

This analyzer extracts **capacitance–voltage characteristics**.

```bash
cd bsim/analyzer_cv
python run_cv.py
python plot_cv.py
```

📂 Results are stored in:

```
bsim/analyzer_cv/results/<node>/
```

---

### 2.3 DIM Analyzer (L / W Sweep)

This analyzer evaluates **device scaling effects** by sweeping gate length and width.

```bash
cd bsim/analyzer_dim
python run/run_vg_dim.py
python run/run_vd_dim.py
python plot/plot_vg_dim.py
python plot/plot_vd_dim.py
```

📂 Results are stored in:

```
bsim/analyzer_dim/results/<node>/
```

---

### 2.4 Reliability Analyzer (HCI / NBTI)

This analyzer simulates **reliability degradation mechanisms**.

```bash
cd bsim/analyzer_reliability
python run/run_hci_nmos.py
python run/run_nbti_pmos.py
```

📂 Plots and extracted degradation data are saved in:

```
bsim/analyzer_reliability/results/
```

---

## 🧮 3. Paramus Physical Edition

Paramus Physical Edition generates **BSIM4 model cards directly from simplified physical parameters**.

### Example: Modelcard generation

```bash
cd bsim/paramus_physical
python paramus.py --node 130nm --type nmos --out nmos130.sp
python paramus.py --node 130nm --type pmos --out pmos130.sp
```

📂 Preset parameter files are located in:

```
bsim/paramus_physical/presets/
```

📄 Generated `.sp` modelcards appear in the current working directory.

---

## 🏗 4. Running OpenLane-Lite

> ⚠ **Requirements**:  
> - Linux or WSL2  
> - Docker (running)

Execute the minimal RTL → GDSII flow:

```bash
cd openlane/openlane-lite
./docker/run_in_docker.sh ./scripts/run_flow.sh
```

📂 Results (GDS / DEF / logs) are generated in:

```
openlane/openlane-lite/runs/<design-name>/
```

---

## 🛠 5. General Troubleshooting

### ❌ Python cannot find module
→ Ensure that your **virtual environment is activated**.

### ❌ ngspice not found
→ Install ngspice and verify that it is available in PATH.

### ❌ Docker cannot run
- 🐧 Linux: ensure your user belongs to the `docker` group  
- 🪟 Windows: ensure Docker Desktop is running and **WSL2 backend is enabled**

---

## 🧭 6. Next Step

You can now:

- Proceed to **`4_license.md`**  
- Explore each module in more detail  
- Modify scripts and parameters to experiment with device behavior

---

🎯 **You are now ready to use SemiDevKit**

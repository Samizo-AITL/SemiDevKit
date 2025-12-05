# 3_usage.md

# SemiDevKit — Usage Guide

This document explains how to run the major tools included in **SemiDevKit**, including TCAD playgrounds, BSIM4 analyzers, Paramus Physical Edition, and OpenLane-Lite.

---

# 1. Running TCAD Playgrounds

## 1.1 MOSFET / MOSCAP (tcad_playground)

```
cd tcad/tcad_playground
python mosfet_vgid_1d.py
python mosfet_vdid_1d.py
python moscap_cv_1d.py
```

Output figures are stored in:

```
tcad/tcad_playground/fig/
```

## 1.2 PZT P–E Loop Playground (tcad_playground_pzt)

```
cd tcad/tcad_playground_pzt
python pzt_pe_hysteresis_1d.py
```

Figures are stored in:

```
tcad/tcad_playground_pzt/fig/
```

---

# 2. Running BSIM4 Analyzers

## 2.1 DC Analyzer (VG–ID / VD–ID)

```
cd bsim/analyzer_dc
python run/run_vgid.py
python run/run_vdid.py
python plot/plot_vgid.py
python plot/plot_vdid.py
```

Results:

```
bsim/analyzer_dc/results/...
```

---

## 2.2 CV Analyzer (Cgg–Vg)

```
cd bsim/analyzer_cv
python run_cv.py
python plot_cv.py
```

Results are generated under:

```
bsim/analyzer_cv/results/<node>/
```

---

## 2.3 DIM Analyzer (L/W Sweep)

```
cd bsim/analyzer_dim
python run/run_vg_dim.py
python run/run_vd_dim.py
python plot/plot_vg_dim.py
python plot/plot_vd_dim.py
```

Results:

```
bsim/analyzer_dim/results/<node>/
```

---

## 2.4 Reliability Analyzer (HCI / NBTI)

```
cd bsim/analyzer_reliability
python run/run_hci_nmos.py
python run/run_nbti_pmos.py
```

Plots and extracted degradation data:

```
bsim/analyzer_reliability/results/...
```

---

# 3. Paramus Physical Edition

Generate a BSIM4 modelcard from simple physical parameters:

Examples:

```
cd bsim/paramus_physical
python paramus.py --node 130nm --type nmos --out nmos130.sp
python paramus.py --node 130nm --type pmos --out pmos130.sp
```

Presets are located in:

```
bsim/paramus_physical/presets/
```

Generated `.sp` files appear in the working directory.

---

# 4. Running OpenLane-Lite

> Requires: Docker + Linux/WSL2 environment.

```
cd openlane/openlane-lite
./docker/run_in_docker.sh ./scripts/run_flow.sh
```

Results (GDS / DEF / logs) appear in:

```
openlane/openlane-lite/runs/<design-name>/
```

---

# 5. General Troubleshooting

### Python cannot find module
→ Ensure your venv is activated.

### ngspice not found
→ Install ngspice and ensure it is in PATH.

### Docker cannot run
→ Linux: ensure your user is in the `docker` group  
→ Windows: ensure Docker Desktop is running and WSL2 backend is enabled.

---

# 6. Next Step

Proceed to **4_license.md** or continue exploring each module in detail.

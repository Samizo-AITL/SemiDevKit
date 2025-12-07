# 📘 BSIM4 Analyzer Reliability  

---

##  Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/bsim/bsim4_analyzer_reliability/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/bsim4_analyzer_reliability) |

---

**Unified NMOS HCI / PMOS NBTI Reliability Analysis Framework  
(NGSPICE + Python)**

---

## 📌 Overview

**BSIM4 Analyzer Reliability** is an integrated framework for analyzing semiconductor aging mechanisms:  

- **NMOS Hot-Carrier Injection (HCI)**  
- **PMOS Negative Bias Temperature Instability (NBTI)**  

The framework combines:  
- **SPICE-based measurement at t = 0**  
- **Python-based degradation models for t > 0**  
to produce a hybrid, reproducible reliability analysis workflow.

### Key Features
- ✔ Automated **VG–ID sweep** & **DC current extraction**  
- ✔ Computes four degradation quantities:  
  **ΔVtg, ΔVtc, ΔIdlin, ΔIdsat**  
- ✔ Full support for both **NMOS HCI** and **PMOS NBTI**  
- ✔ Structured directory for reproducible results  
- ✔ Suitable for academic research & corporate reliability evaluation  
- ✔ Parameterized degradation models for extensible aging studies  

---

## 📁 Directory Structure

```
bsim4_analyzer_reliability/
├── models/
│    ├── nmos130.sp
│    └── pmos130.sp
│
├── templates/
│    ├── template_hci_nmos.cir
│    ├── template_nmos_vgid.cir
│    ├── template_nbti_pmos.cir
│    ├── template_pmos_vgid.cir
│
├── run/
│    ├── run_hci_nmos.py
│    └── run_nbti_pmos.py
│
├── plot/
│    ├── plot_hci_nmos.py
│    └── plot_nbti_pmos.py
│
└── results/
     ├── 90nm/
     └── 130nm/
          ├── hci_nmos/
          ├── hci_nmos_vgid/
          ├── nbti_pmos/
          └── nbti_pmos_vgid/
```

---

## 🔧 Installation & Requirements

### ■ Python Packages
```
numpy
pandas
matplotlib
```

### ■ NGSPICE
- Verified with **ngspice 33–42**
- Ensure `ngspice` is available in your system PATH

---

## 🔬 Reliability Analysis Workflow

The same conceptual flow applies to both NMOS and PMOS.

```
t = 0
 ├─ VG–ID sweep
 │     ├→ extract Vtg0 (gmmax method)
 │     └→ extract Vtc0 (constant-current method)
 ├─ DC extraction
 │     └→ Idlin0, Idsat0

t > 0  (Python degradation model)
 ├─ ΔVth(t)
 ├─ ΔId_rel(t)
 └─ reconstruct Vtg1, Vtc1, Idlin1, Idsat1

→ Save CSV results
→ Generate degradation plots
→ VG–ID overlay plots
```

---

# 🟥 NMOS HCI (Hot-Carrier Injection)

## ▶ Stress Bias Conditions
```
| Node   | Voltage      |
|--------|--------------|
| Drain  | High Vd (e.g., 1.2 V) |
| Gate   | Stress voltage |
| Source | 0 V |
| Bulk   | 0 V |
```

## ▶ Extracted Quantities
- ΔIdlin  
- ΔIdsat  
- ΔVtg (gmmax-based Vth shift)  
- ΔVtc (constant-current Vth shift)  

## ▶ Run HCI Simulation
```
python run/run_hci_nmos.py
```

---

# 🟦 PMOS NBTI (Negative BTI)

## ▶ Stress Bias Conditions
```
| Node   | Voltage |
|--------|---------|
| Source | +1.2 V |
| Bulk   | +1.2 V |
| Drain  | 0 V |
| Gate   | 0 → −1.2 V |
```

---

## ▶ VG–ID Output Specification (4 columns, fixed)

```
0: Vg
1: Vs
2: Vgs = V(g) − V(s)
3: Id = abs(i(Vd))
```

Python side:
```python
Vgs = arr[:, 2]
Id  = arr[:, 3]
```

---

## ▶ NBTI Degradation Model (PMOS)

### ■ Threshold Voltage Shift
```python
dVth = A_vth * (t ** p_vth)
Vtg1 = Vtg0 - dVth
Vtc1 = Vtc0 - dVth
```

### ■ Drive Current Degradation
```python
dIdrel = -A_id * (t ** p_id)
Idlin1 = Idlin0 * (1 + dIdrel)
Idsat1 = Idsat0 * (1 + dIdrel)
```

---

## ▶ Run NBTI Simulation
```
python run/run_nbti_pmos.py
```

---

# 📊 Output Files

The framework creates structured result sets for each node (90nm / 130nm).

### ■ NMOS HCI
```
results/<node>/hci_nmos/
    dIdlin_vs_time.png
    dIdsat_vs_time.png
    dVtg_vs_time.png
    dVtc_vs_time.png
    hci_summary.csv
```

### ■ PMOS NBTI
```
results/<node>/nbti_pmos/
    dIdlin_vs_time.png
    dIdsat_vs_time.png
    dVtg_vs_time.png
    dVtc_vs_time.png
    nbti_pmos_summary.csv
```

### ■ VG–ID Overlays
```
<device>_vgid/
    vgid_all_linear.png
    vgid_all_log.png
```

---

# 🧠 Internal Degradation Models

### ■ NMOS HCI
```
ΔVth = A_vth * t^p
ΔId  = -A_id * t^p
```

### ■ PMOS NBTI
```
Vtg(t), Vtc(t) = Vth0 − ΔVth
Id(t) = Id(0) * (1 + ΔId)
```

---

# 🧩 Extensible Architecture

Easily extendable to:

- NMOS PBTI (Positive BTI)  
- Arrhenius temperature acceleration  
- Duty-cycle / AC stress  
- BSIM4 parameter aging injection  
- Packaging as a Python library:  
  ```
  pip install aging-model
  ```
---

## 📎 Reliability Analysis — Reference Figures

### ■ NMOS HCI : Vg–Id Degradation (Linear Scale)
![NMOS HCI Vg–Id](/assets/bsim4_analyzer_reliability/nmos_hci_vgid.png)

---

### ■ NMOS HCI : ΔVtg vs Stress Time (gmmax Method)
![HCI dVtg](/assets/bsim4_analyzer_reliability/hci_dvtg.png)

---

### ■ PMOS NBTI : Vg–Id Degradation (Linear Scale)
![PMOS NBTI Vg–Id](/assets/bsim4_analyzer_reliability/pmos_nbti_vgid.png)

---

### ■ PMOS NBTI : ΔVtg vs Stress Time
![NBTI dVtg](/assets/bsim4_analyzer_reliability/nbit_dvtg.png)

---

# 📄 Hybrid License

| Item | License | Description |
|------|---------|-------------|
| **Source Code** | MIT License | Free to use, modify, redistribute |
| **Text Materials** | CC BY 4.0 | Attribution required |
| **Figures / Plots / Generated Data** | CC BY-NC 4.0 | Non-commercial use only |
| **External References** | Original license applies | Cite properly |

---

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

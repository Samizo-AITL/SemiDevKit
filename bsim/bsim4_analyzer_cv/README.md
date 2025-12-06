# MOSFET C–V Extraction Tool (BSIM4, ngspice)

This tool automatically extracts **gate capacitance (Cgg–Vg)** characteristics  
from **BSIM4 NMOS/PMOS models** using ngspice DC analysis.

Key features:
- Per-process-node analysis (e.g., 130nm)
- Independent extraction for NMOS and PMOS
- Temperature sweep (LT = −40°C, RT = 25°C, HT = 125°C)
- Model files separated under `models/`
- Automatic netlist generation → ngspice batch execution → Cgg extraction → PNG output

---

## 📁 Directory Structure

```
BSIM4_ANALYZER_CV/
│
├── models/
│   ├── nmos130.sp
│   └── pmos130.sp
│
├── template_cv.cir
├── run_cv.py
├── plot_cv.py
├── README.md
│
└── results/
    └── 130nm/
        ├── nmos_130nm_RT.cir
        ├── nmos_130nm_RT.log
        ├── nmos_130nm_RT.png
        ├── pmos_130nm_RT.cir
        ├── pmos_130nm_RT.log
        ├── pmos_130nm_RT.png
        └── … (LT / HT also produced)
```

---

## 🧩 1. `template_cv.cir` (Analysis Template)

A voltage sweep template used by Python `.format()` to embed settings.

### NMOS (standard)
- Connections: **S = D = B = 0V**, gate swept
- Sweep: **0V → VDD**

### PMOS (real device behavior)
- Connections: **D = S = B = VDD**, gate swept
- Sweep: **VDD → 0V**  
  → Matches physical ON/OFF behavior  
    (OFF at Vg = VDD → ON at Vg = 0)

**Output: Cgg only**  
```
.print dc V(g) @m1[cgg]
```

---

## ❗ Why Only Cgg Is Extracted (Important)

BSIM4 internal capacitances behave as:

- **Cgg = ∂Qg / ∂Vg**, a physically meaningful *total gate capacitance*
- Cgs, Cgd, Cgb are **partitioned charges** (model-dependent), not physical CV values

Problems with partitioned capacitances:
- Cgs + Cgd + Cgb ≠ Cgg  
- Cgs/Cgd depend heavily on the charge-partition algorithm  
- They may contain unstable values at low Vg

→ Therefore, **this tool extracts Cgg only**, ensuring physical interpretability.

---

## 🚀 2. Netlist Auto-Generation & Batch Execution (`run_cv.py`)

Run:
```
python run_cv.py
```

This performs:
- Auto-generation of **NMOS/PMOS × LT/RT/HT** netlists  
- Automatic batch execution of all 6 cases using ngspice

Update ngspice path if needed:

```python
NGSPICE_CMD = r"C:\Program Files\Spice64\bin\ngspice.exe"
```

---

## 📊 3. Plotting Cgg–Vg (`plot_cv.py`)

Run:
```
python plot_cv.py
```

Processing steps:
1. Read V(g) and Cgg from `.print dc`
2. **Remove index=0** (DC initial non-physical point)
3. **Remove Cgg ≤ 0** (solver startup noise)
4. Save PNG to:

```
results/<node>/<basename>.png
```

---

## 🧪 Example Output Behavior

- **NMOS:** accumulation → depletion → inversion (U-shaped curve)  
- **PMOS:** reversed sweep (VDD → 0), following real device biasing  
- Units: **F (farads)**, matplotlib handles scientific notation automatically

---

## 📦 Model Files (`models/*.sp`)

BSIM4 educational models:
- `nmos130.sp`
- `pmos130.sp`

(Not matched to any foundry process; intended for learning & analysis.)

---

## 🔧 Adding a New Process Node

Add a node definition inside `run_cv.py`:

```python
"90nm": {
    "vdd": 1.0,
    "nmos_model_file": "nmos90.sp",
    "pmos_model_file": "pmos90.sp",
    "nmos_model_name": "nmos90",
    "pmos_model_name": "pmos90",
    "lch": "0.09u",
    "wch": "1u",
    "toxe": "1.8e-9",
},
```

---

## ✔ Environment

- Windows 11  
- ngspice 41 (64-bit)  
- Python 3.9+  
- matplotlib 3.x  

---

## 📘 Summary

This tool provides:

1. **Correct terminal conditions for NMOS/PMOS and physically accurate sweep directions**
2. **Physically meaningful extraction of Cgg only**
3. **Fully automated batch processing for 6 conditions (NMOS/PMOS × 3 temperatures)**
4. **Clean separation of models / template / results for easy scaling**
5. **Complete automation from ngspice → log → PNG**

Ideal for device physics education, compact modeling, and process comparison studies.

Possible extensions:
- dC/dV extraction  
- Cox estimation  
- CV-derived Vth  
- Experimental-research mode for Cgs/Cgd/Cgb  
- Multi-node comparison plots  

---

### ■ NMOS C–V Characteristics (130nm, RT)

![NMOS C–V Example](assets/bsim4_analyzer_cv/nmos_cv.png)

- Device: **NMOS (130nm)**
- Temperature: **RT (Room Temperature)**
- Behavior: Accumulation → Depletion → Inversion
- Extracted Parameter: **Cgg vs. Vg**

---

### ■ PMOS C–V Characteristics (130nm, RT)

![PMOS C–V Example](assets/bsim4_analyzer_cv/pmos_cv.png)

- Device: **PMOS (130nm)**
- Temperature: **RT (Room Temperature)**
- Sweep Direction: **VDD → 0 V** (realistic PMOS biasing)
- Extracted Parameter: **Cgg vs. Vg**

---

# 📄 Hybrid License

This project uses a **Hybrid License**:

| Item | License | Description |
|------|---------|-------------|
| **Source Code** | MIT License | Free to use, modify, redistribute |
| **Documentation / Text Materials** | CC BY 4.0 | Attribution required |
| **Figures / Plots / Generated Images** | CC BY-NC 4.0 | Non-commercial use only |
| **External References** | Original license applies | Cite appropriately |

---

# 🤝 Author

**Shinichi Samizo**  
Samizo-Lab / Device Modeling & TCAD Research

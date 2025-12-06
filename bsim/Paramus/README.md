# ⚙️ Paramus Physical Edition  

---

##  Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/bsim/Paramus/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/Paramus) |

---

### *Generate BSIM4 model cards from five fundamental physical parameters*

Paramus Physical Edition is a Python-based utility that automatically generates  
**BSIM4 SPICE model cards (`.sp`)** from a small set of key MOSFET physical parameters:

**tox / Na / Vfb / μ0 / L/W**

It is designed for device engineers, students, and researchers who want a clean and interpretable  
bridge between **MOSFET physical characteristics** and **compact modeling (BSIM4)**.

---

## 📁 Project Structure

```
Paramus/
│
├── modelcard/
│   ├── build.py               # Inserts parameters into the BSIM4 template
│   ├── template_bsim4.tpl     # BSIM4 model card template
│
├── physical/
│   ├── extract.py             # Loads presets & interprets physical parameters
│   ├── poisson.py             # Surface potential & Vth calculation
│   ├── iv.py                  # Simplified I–V model (Ids, gm)
│   ├── mapping.py             # Physical values → BSIM4 parameter mapping
│
├── presets/
│   ├── nmos_90nm.json
│   ├── nmos_130nm.json
│   ├── pmos_90nm.json
│   ├── pmos_130nm.json
│
├── paramus.py                 # Main entry point
└── README.md
```

---

## 🚀 How to Use

### 1. Move to the Paramus directory
```
cd Path/To/Paramus
```

### 2. Generate a model card

**NMOS 130nm**
```
python paramus.py --node 130nm --type nmos --out model.sp
```

**PMOS 130nm**
```
python paramus.py --node 130nm --type pmos --out pmos130.sp
```

**NMOS 90nm**
```
python paramus.py --node 90nm --type nmos --out nmos90.sp
```

Generated output example:

```
model.sp
```

---

## 🔧 Input Parameters (5 Physical Quantities)

| Parameter | Description |
|----------|-------------|
| **tox** | Gate oxide thickness |
| **Na** | Channel doping concentration |
| **Vfb** | Flat-band voltage |
| **μ0** | Low-field mobility |
| **L/W** | Device geometry (length & width ratio) |

---

## 🧠 Model Generation Flow

```
[ Physical Model ]  physical/
    extract.py   → Load & process physical parameters
    poisson.py   → Compute φs, Vth0, Cox, Es
    iv.py        → Compute Ids, gm
    mapping.py   → Map physical values to BSIM4 parameters

[ Template ]     modelcard/
    template_bsim4.tpl
    build.py     → Embed mapped values into template

[ Execution ]
    paramus.py   → Outputs model.sp
```

---

## 📘 Source Code Overview

### ● `physical/extract.py`
- Loads JSON preset  
- Performs unit normalization  
- Prepares data for Poisson / IV stages  

### ● `physical/poisson.py`
Computes:
- Surface potential **φs**  
- Threshold voltage **Vth0**  
- Oxide capacitance **Cox**  
- Surface electric field **Es**  

### ● `physical/iv.py`
Implements simplified MOSFET I–V behavior:
- Ids(Vgs, Vds)  
- gm, gds  
- Linear / Saturation regions  

### ● `physical/mapping.py`
Maps physical quantities to BSIM4 parameters:
- μ0 → u0, ua, ub  
- tox → tox, epsrox  
- φs → vth0  
- SCE terms → dvt0, dvt1, eta0  

### ● `modelcard/build.py`
- Replaces `{{key}}` placeholders  
- Outputs the final BSIM4 model card  

---

## 🎯 Custom Presets

To use your own MOSFET parameters:

```
python paramus.py --preset presets/my_nmos.json --out my_model.sp
```

---

## 📄 BSIM4 Template (template_bsim4.tpl)

A standard BSIM4 template.  
`{{ parameter }}` entries are filled automatically by `build.py`.

---

# 📄 **Hybrid License**

Paramus Physical Edition adopts a **hybrid licensing model** designed to handle code, documentation, and figures appropriately.

| Item | License | Description |
|------|---------|-------------|
| **Source Code** | MIT License | Free to use, modify, redistribute |
| **Documentation / Text Materials** | CC BY 4.0 | Attribution required |
| **Figures / Diagrams / Generated Plots** | CC BY-NC 4.0 | Non-commercial use only |
| **External References** | Original license applies | Cite sources properly |

---

## 📬 Contact

For requests, improvements, or extensions to the physical modeling,  
please open an Issue in the repository.

---

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

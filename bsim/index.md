---
layout: default
title: bsim
---

----

# 🧠 BSIM4 Compact Modeling & Device Simulation Suite

---

##  Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/bsim/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim) |

---

This directory contains the **BSIM4-based compact modeling and analysis tools** included in **SemiDevKit**.

These modules provide:
- ✔ Automatic BSIM4 parameter extraction  
- ✔ DC / AC / CV circuit simulation  
- ✔ Device geometry scaling analysis  
- ✔ Reliability degradation modeling (NBTI / HCI)

---

## 📁 Directory Contents

```
bsim/
├── Paramus/                    # BSIM4 model parameter extraction engine
│
├── bsim4_analyzer_dc/          # DC characteristics (Vg–Id / Vd–Id)
│
├── bsim4_analyzer_cv/          # AC/CV analysis (Vg–Cgg etc.)
│
├── bsim4_analyzer_dim/         # L/W scaling analysis
│
└── bsim4_analyzer_reliability/ # NBTI / HCI degradation simulation
```

---

### 🧩 BSIM4 / SPICE Analyzer Modules

| No. | Module | Purpose | Input | Output | Pages | Repo |
|----:|--------|---------|-------|--------|-------|------|
| 1 | **Paramus** | BSIM4 parameter extraction engine | Physical parameters<br>tox / Na / Vfb / μ₀ / L / W | BSIM4 model card<br>(.model) | [Pages](https://samizo-aitl.github.io/SemiDevKit/bsim/Paramus/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/Paramus) |
| 2 | **bsim4_analyzer_dc** | DC characteristics analysis | BSIM4 model<br>Vg / Vd sweep | Vg–Id / Vd–Id<br>gm / ro | [Pages](https://samizo-aitl.github.io/SemiDevKit/bsim/bsim4_analyzer_dc/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/bsim4_analyzer_dc) |
| 3 | **bsim4_analyzer_cv** | CV characteristics analysis | BSIM4 model<br>AC / bias conditions | Vg–Cgg / Cgs / Cgd | [Pages](https://samizo-aitl.github.io/SemiDevKit/bsim/bsim4_analyzer_cv/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/bsim4_analyzer_cv) |
| 4 | **bsim4_analyzer_dim** | L/W scaling analysis | BSIM4 model<br>L / W sweep | Geometry scaling trends<br>Short-channel effects | [Pages](https://samizo-aitl.github.io/SemiDevKit/bsim/bsim4_analyzer_dim/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/bsim4_analyzer_dim) |
| 5 | **bsim4_analyzer_reliability** | Reliability & aging simulation | Stress conditions<br>NBTI / HCI | Vth shift<br>Degraded I–V | [Pages](https://samizo-aitl.github.io/SemiDevKit/bsim/bsim4_analyzer_reliability/) | [Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/bsim4_analyzer_reliability) |

---

## 🚀 How to Use

Example: Run DC analysis
```bash
cd bsim4_analyzer_dc/run
python run_vd.py
python run_vg.py
```

Example: Run reliability simulation
```bash
cd bsim4_analyzer_reliability
python run_nbti.py
python run_hci.py
```

---

## 📘 Documentation

Detailed tutorials and formulas are available in:

👉 https://samizo-aitl.github.io/SemiDevKit/

---

## 📄 License

- Code: MIT  
- Documentation: CC BY / CC BY-SA  
- Figures: CC BY-NC  

---

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |


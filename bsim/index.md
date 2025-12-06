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

### 🔸 1. Paramus — BSIM4 Parameter Extraction Engine
[![Pages](https://img.shields.io/badge/GitHub%20Pages-Paramus-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/bsim/Paramus/)
[![Repo](https://img.shields.io/badge/GitHub-Paramus-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/Paramus)

### 🔸 2. bsim4_analyzer_dc — DC Characteristics (Vg–Id / Vd–Id)
[![Pages](https://img.shields.io/badge/GitHub%20Pages-DC%20Analyzer-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/bsim/bsim4_analyzer_dc/)
[![Repo](https://img.shields.io/badge/GitHub-DC%20Analyzer-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/bsim4_analyzer_dc)

### 🔸 3. bsim4_analyzer_cv — CV Characteristics (Vg–Cgg etc.)
[![Pages](https://img.shields.io/badge/GitHub%20Pages-CV%20Analyzer-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/bsim/bsim4_analyzer_cv/)
[![Repo](https://img.shields.io/badge/GitHub-CV%20Analyzer-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/bsim4_analyzer_cv)

### 🔸 4. bsim4_analyzer_dim — L/W Scaling Analysis
[![Pages](https://img.shields.io/badge/GitHub%20Pages-DIM%20Analyzer-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/bsim/bsim4_analyzer_dim/)
[![Repo](https://img.shields.io/badge/GitHub-DIM%20Analyzer-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/bsim4_analyzer_dim)

### 🔸 5. bsim4_analyzer_reliability — NBTI / HCI Aging Simulation
[![Pages](https://img.shields.io/badge/GitHub%20Pages-Reliability%20Analyzer-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/bsim/bsim4_analyzer_reliability/)
[![Repo](https://img.shields.io/badge/GitHub-Reliability%20Analyzer-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/bsim/bsim4_analyzer_reliability)

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


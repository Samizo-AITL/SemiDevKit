# 🎛 OpenLane — Flow Documentation Hub

---

##  Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/openlane/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane) |

---

This directory organizes **OpenLane workflow documentation** inside the SemiDevKit project.  
It provides two structured sub-flows:

- **OpenLane Lite** — minimal, lightweight execution flow  
- **OpenLane Superstable** — full stable flow with complete GDS results

---

## 📦 OpenLane Lite (Lightweight Flow)

### 🔗 Repository / Documentation
[![Page](https://img.shields.io/badge/Pages-Documentation-green.svg)](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-lite/)
[![Repo](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-lite)

### 📘 Description
- Minimal OpenLane environment  
- SKY130A SPM sample flow  
- Generated GDS/DEF/timing reports  
- Verified using OpenROAD GUI  

---

## 🧱 OpenLane Superstable (Full Stable Flow)

### 🔗 Repository / Documentation
[![Page](https://img.shields.io/badge/Pages-Documentation-green.svg)](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-superstable/)
[![Repo](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-superstable)

### 📘 Description
- Complete run of the SPM (Simple Processor Model)  
- Final GDS, DEF/LEF, timing & area reports  
- GUI-verified routing, placement, and filler structures  
- Includes screenshots and analysis  

---

## 📄 Purpose of This README

- Provide a **single unified entry point** for OpenLane resources  
- Clearly distinguish between **Lite** and **Superstable** flows  
- Offer **direct navigation** to GitHub / GitHub Pages documentation  

---

## 📁 Directory Structure

```
openlane/
├── openlane-lite/ # Lightweight OpenLane documentation
├── openlane-superstable/ # Full stable flow with GDS output
└── README.md # ← This file (OpenLane index)
```

---

## 💬 Notes

- Both flows use **SKY130** and were executed in official OpenLane containers  
- Can be adapted for any RTL given suitable configuration  
- Future updates will include IR-drop, power, and DRC documentation  

---

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |



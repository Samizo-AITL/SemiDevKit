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

[Pages](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-lite/) ｜ 
[Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-lite)

### 📘 Description
- Minimal OpenLane environment  
- SKY130A SPM sample flow  
- Generated GDS/DEF/timing reports  
- Verified using OpenROAD GUI  

---

## 🧱 OpenLane Superstable (Full Stable Flow)

[Pages](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-superstable/) ｜ 
[Repo](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-superstable)

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

| Item | Details |
|----|--------|
| 👨‍🔬 Name | **Shinichi Samizo** |
| 💻 GitHub | [Samizo-AITL](https://github.com/Samizo-AITL) |

---

## 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/SemiDevKit/#---license)

| Component | License | Notes |
|---------|---------|------|
| 💻 Source Code | [**MIT License**](https://opensource.org/licenses/MIT) | Free use / modification |
| 📄 Text Materials | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) / [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | Attribution required |
| 🎨 Figures & Diagrams | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | Non-commercial only |
| 🔗 External References | Original license | Proper citation required |


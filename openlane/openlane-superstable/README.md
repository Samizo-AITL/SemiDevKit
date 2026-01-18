# 🚀 OpenLane Superstable — SPM Flow Result  
**Verified Physical Design Flow (GDS → DEF/LEF → OpenROAD Visualization)**

---

##  Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-superstable/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-superstable) |

---

This directory documents a fully verified execution of **OpenLane (superstable branch)** using the example design **SPM (Simple Processor Model)**.

The flow produced the following valid outputs:

- ✔️ Final GDS (`spm.gds`)  
- ✔️ Final DEF / LEF  
- ✔️ Layout visualization validated in **OpenROAD GUI**  
- ✔️ Area report confirmed via OpenROAD (`report_design_area`)  

All results were generated **inside the official OpenLane Docker container**, without any source code modifications.

---

## 📐 1. Generated GDS Result (KLayout View)

### **Full-chip GDS layout**
![spm_gds_full](/assets/openlane-superstable/spm_gds_full.png)

### **Transistor-level detail（poly/diffusion layers）**
![spm_gds_dif_poly](/assets/openlane-superstable/spm_gds_dif_poly.png)

These screenshots confirm that:
- Standard cell placement is correct  
- Routing layers (M1–M5) follow SKY130A design rules  
- No missing polygons / GDS corruption  

---

## 🖥️ 2. OpenROAD GUI — Successfully Loaded LEF/DEF

### **Global layout view**
![openroad_1](/assets/openlane-superstable/openroad_1.png)

### **Detailed routing view**
![openroad_2](/assets/openlane-superstable/openroad_2.png)

In OpenROAD GUI:
- DEF/LEF loads without warnings  
- Layer visibility & routing geometry verified  
- Filler cells / vias / standard cells correctly rendered  

---

## 🧪 3. Commands Used (Inside OpenLane Container)

### **Start OpenROAD**
```tcl
openroad
```

---

### **Load technology (LEF) and placed-and-routed design (DEF)**

```tcl
read_lef designs/spm/runs/<RUN>/tmp/merged.nom.lef
read_def designs/spm/runs/<RUN>/results/final/def/spm.def
```

💡 `<RUN>` is typically auto-generated, e.g.:  
`RUN_2025.12.07_15.21.34`

---

### *(Optional)* Load Liberty for timing analysis

```tcl
read_liberty /openlane/pdks/sky130A/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
```

---

## 📊 4. Example Report Output

### **Design Area Report**
OpenROAD successfully evaluates area after loading LEF/DEF:

```
report_design_area
Design area 4114 u^2 51% utilization.
```

Interpretation:
- **4114 μm²** = total placed cell + routing area  
- **51% utilization** = healthy for SKY130 (target 50–60%)  

---

## 📤 5. Export Options (Optional)

OpenROAD allows saving the database in multiple formats:

```tcl
write_def out.def
write_lef out.lef
write_db out.db
```

Useful for:
- External STA tools  
- KLayout / Magic cross-verification  
- Downstream EDA workflows  

---

## 📝 Notes

- Target design: **SPM (Simple Processor Model)**  
- Environment: **OpenLane “superstable”**, revision `ff5509f`  
- Platform: **SKY130A PDK**  
- Execution environment: **Official OpenLane Docker container**  
- No code changes; only standard OpenLane configs were used  
- All results are reproducible with the provided commands  

---

## ✔️ Summary

This directory shows a **complete, validated RTL-to-GDS physical design run**, including:
- GDS generation  
- DEF/LEF export  
- OpenROAD visualization  
- Area report verification  

It serves as a **reference-quality example** of OpenLane superstable being executed successfully on a real SKY130A design.

---
# 🚀 OpenLane Superstable — SPM Flow Result  
**Verified Physical Design Flow (GDS → DEF/LEF → OpenROAD Visualization)**

---

##  Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-superstable/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-superstable) |

---

This directory documents a fully verified execution of **OpenLane (superstable branch)** using the example design **SPM (Simple Processor Model)**.

The flow produced the following valid outputs:

- ✔️ Final GDS (`spm.gds`)  
- ✔️ Final DEF / LEF  
- ✔️ Layout visualization validated in **OpenROAD GUI**  
- ✔️ Area report confirmed via OpenROAD (`report_design_area`)  

All results were generated **inside the official OpenLane Docker container**, without any source code modifications.

---

## 📐 1. Generated GDS Result (KLayout View)

### **Full-chip GDS layout**
![spm_gds_full](/assets/openlane-superstable/spm_gds_full.png)

### **Transistor-level detail（poly/diffusion layers）**
![spm_gds_dif_poly](/assets/openlane-superstable/spm_gds_dif_poly.png)

These screenshots confirm that:
- Standard cell placement is correct  
- Routing layers (M1–M5) follow SKY130A design rules  
- No missing polygons / GDS corruption  

---

## 🖥️ 2. OpenROAD GUI — Successfully Loaded LEF/DEF

### **Global layout view**
![openroad_1](/assets/openlane-superstable/openroad_1.png)

### **Detailed routing view**
![openroad_2](/assets/openlane-superstable/openroad_2.png)

In OpenROAD GUI:
- DEF/LEF loads without warnings  
- Layer visibility & routing geometry verified  
- Filler cells / vias / standard cells correctly rendered  

---

## 🧪 3. Commands Used (Inside OpenLane Container)

### **Start OpenROAD**
```tcl
openroad
```

---

### **Load technology (LEF) and placed-and-routed design (DEF)**

```tcl
read_lef designs/spm/runs/<RUN>/tmp/merged.nom.lef
read_def designs/spm/runs/<RUN>/results/final/def/spm.def
```

💡 `<RUN>` is typically auto-generated, e.g.:  
`RUN_2025.12.07_15.21.34`

---

### *(Optional)* Load Liberty for timing analysis

```tcl
read_liberty /openlane/pdks/sky130A/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
```

---

## 📊 4. Example Report Output

### **Design Area Report**
OpenROAD successfully evaluates area after loading LEF/DEF:

```
report_design_area
Design area 4114 u^2 51% utilization.
```

Interpretation:
- **4114 μm²** = total placed cell + routing area  
- **51% utilization** = healthy for SKY130 (target 50–60%)  

---

## 📤 5. Export Options (Optional)

OpenROAD allows saving the database in multiple formats:

```tcl
write_def out.def
write_lef out.lef
write_db out.db
```

Useful for:
- External STA tools  
- KLayout / Magic cross-verification  
- Downstream EDA workflows  

---

## 📝 Notes

- Target design: **SPM (Simple Processor Model)**  
- Environment: **OpenLane “superstable”**, revision `ff5509f`  
- Platform: **SKY130A PDK**  
- Execution environment: **Official OpenLane Docker container**  
- No code changes; only standard OpenLane configs were used  
- All results are reproducible with the provided commands  

---

## ✔️ Summary

This directory shows a **complete, validated RTL-to-GDS physical design run**, including:
- GDS generation  
- DEF/LEF export  
- OpenROAD visualization  
- Area report verification  

It serves as a **reference-quality example** of OpenLane superstable being executed successfully on a real SKY130A design.

---

## 🧪 Self-made Minimal RTL Flow

- **Design** : `spm_min_counter`  
- **Intent** :  
  Pre-declared *minimal* RTL design used to verify  
  **OpenLane (superstable) stability with designer-authored RTL**,  
  without relying on reference or example circuits.
- **Result** :  
  ✔ RTL → GDS flow completed successfully  
  ✔ CTS and routing finished without manual intervention  

➡ **Flow details and artifacts**:  
[`spm_min_counter/`](./spm_min_counter/)

---

## 👤 Author

| Item | Details |
|----|--------|
| 👨‍🔬 Name | **Shinichi Samizo** |
| 💻 GitHub | [Samizo-AITL](https://github.com/Samizo-AITL) |

---

## 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-superstable/#---license)

| Component | License | Notes |
|---------|---------|------|
| 💻 Source Code | [**MIT License**](https://opensource.org/licenses/MIT) | Free use / modification |
| 📄 Text Materials | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) / [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | Attribution required |
| 🎨 Figures & Diagrams | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | Non-commercial only |
| 🔗 External References | Original license | Proper citation required |

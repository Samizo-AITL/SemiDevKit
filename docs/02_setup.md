---
layout: default
title: setup
---

---

# ⚙️ Setup Guide — SemiDevKit

This document describes the **post-installation setup steps** required to make  
**SemiDevKit fully operational** after cloning the repository.

After completing this guide, you will be able to run **BSIM analyzers, TCAD playgrounds, and OpenLane-Lite flows**.

---

## 📁 1. Directory Structure

After cloning the repository, the directory structure should look like this:

```
SemiDevKit/
 ├ _includes/        # Jekyll include files
 ├ _layouts/         # Jekyll layouts
 ├ assets/           # CSS / images for GitHub Pages
 ├ bsim/             # BSIM4 analyzers
 ├ docs/             # Documentation (this site)
 ├ openlane/         # OpenLane-Lite flow
 ├ tcad/             # TCAD playgrounds
 ├ README.md         # Project overview
 ├ index.md          # Top page
 └ config.yml        # Jekyll configuration
```

📌 **Note**  
The directories `_includes`, `_layouts`, and `assets` are used only for **GitHub Pages**.  
For simulations and analysis, you will mainly work in:

- `bsim/`
- `tcad/`
- `openlane/`

---

## 🐍 2. Environment Preparation

### 2.1 Python Virtual Environment (Recommended)

SemiDevKit is designed to run inside an **isolated Python virtual environment**.

---

#### 🐧 Linux / 🍎 macOS / 🪟 WSL2

```bash
cd SemiDevKit
python3 -m venv .venv
source .venv/bin/activate
```

---

#### 🪟 Windows PowerShell (Native)

```powershell
cd SemiDevKit
python -m venv .venv
.venv\Scripts\activate
```

---

### 2.2 Common Python Packages

Install the common Python packages used across most modules:

```bash
pip install numpy scipy matplotlib pandas pyyaml
```

📌 Some lightweight tools only require `numpy` and `matplotlib`.

---

## 🧩 3. Module-Specific Setup

SemiDevKit follows a **modular design**.  
Each module may require additional setup steps.

Please refer to the README files inside the following directories:

| Module | Path | Description |
|------|------|-------------|
| 📐 BSIM Analyzer | `bsim/analyzer_*` | DC / CV / DIM / Reliability analysis |
| 🧪 TCAD | `tcad/tcad_playground` | MOSFET TCAD playground |
| ⚡ TCAD (PZT) | `tcad/tcad_playground_pzt` | Ferroelectric device models |
| 🏗 OpenLane | `openlane/openlane-lite` | RTL → GDSII minimal flow |

---

## ⚡ 4. ngspice (Required for BSIM Tools)

The **BSIM analyzers require ngspice** to run device simulations.

---

### 🪟 Windows

Download the installer from:  
https://sourceforge.net/projects/ngspice/

---

### 🐧 Linux (Ubuntu)

```bash
sudo apt install ngspice
```

---

### 🍎 macOS

```bash
brew install ngspice
```

---

### ✔ Verification

Confirm that ngspice is available:

```bash
ngspice -v
```

❌ If the command is not found, check your PATH settings.  
🪟 On Windows, using **WSL2 is strongly recommended** for best compatibility.

---

## 📝 5. Visual Studio Code Setup (Recommended)

For development, simulation, and documentation, **Visual Studio Code** is recommended.

### Recommended Extensions

- 🐍 Python  
- 📊 Jupyter  
- 🧾 Markdown Preview / Markdown All in One  
- 🪟 Remote – WSL (Windows only)

---

## 🧭 6. Next Step

Once setup is complete, proceed to the next guide:

➡ **`3_usage.md`**

This section explains:
- How to run BSIM analyzers  
- How to use the TCAD playgrounds  
- How to execute the OpenLane-Lite flow  

---

🎯 **At this point, SemiDevKit is fully ready for execution**

---
layout: default
title: install
---

---

# 🧰 Installation Guide — SemiDevKit

This document explains the **environment setup, required software, and initial installation steps**  
for using **SemiDevKit**.

Target tools:
- 🧪 TCAD Playground  
- 📐 BSIM4 Analyzer  
- 🏗 OpenLane-Lite (RTL → GDSII)

---

## 🖥 1. System Requirements

### 1.1 Supported OS

| OS | Status | Notes |
|----|--------|-------|
| 🐧 Linux | ✅ Recommended | Ubuntu 20.04 / 22.04 |
| 🪟 Windows | ✅ Recommended | **WSL2 + Ubuntu** |
| 🍎 macOS | ✅ Supported | Intel / Apple Silicon |

> 💡 **Using WSL2 is strongly recommended on Windows environments.**

---

## 📦 2. Required Software

### 🐍 2.1 Python

SemiDevKit supports the following Python versions:

- **Python 3.9 – 3.12**

#### ✔ Check Python version
```bash
python3 --version
```

#### ✔ Install basic packages
```bash
pip install numpy scipy matplotlib pandas pyyaml
```

📌 Some modules run with only `numpy` and `matplotlib`,  
but analysis tools (BSIM / Paramus) require `pandas`.

---

### ⚡ 2.2 ngspice

SemiDevKit uses **ngspice** for SPICE-based simulations.

#### 🐧 Linux (Ubuntu)
```bash
sudo apt update
sudo apt install -y ngspice
```

#### 🍎 macOS
```bash
brew install ngspice
```

#### 🪟 Windows
- ✅ **Recommended**: Use Linux ngspice inside WSL2 Ubuntu  
- ⚠ Alternative: Native Windows binary  
  https://ngspice.sourceforge.io/

#### ✔ Verification
```bash
ngspice --version
```

---

## 🧩 3. Recommended Tools

### 🪟 3.1 WSL2 (Windows Only)

WSL2 is **essential** for stable operation on Windows.

```powershell
wsl --install
```

After installing Ubuntu from the Microsoft Store:

```bash
sudo apt update && sudo apt upgrade -y
```

---

### 🐳 3.2 Docker (for OpenLane-Lite)

Docker is required to run the minimal RTL → GDSII flow.

- Install Docker Desktop:  
  https://www.docker.com/products/docker-desktop/

#### ✔ Required settings
- ✅ WSL2 backend  
- ✅ Linux containers mode  

---

### 📝 3.3 Visual Studio Code

Recommended editor environment.

#### Recommended extensions
- 🐍 Python  
- 🪟 Remote – WSL (Windows)  
- 🧾 Markdown All in One  

---

## 📥 4. Clone the Repository

### 🔐 HTTPS
```bash
git clone https://github.com/Samizo-AITL/SemiDevKit.git
cd SemiDevKit
```

### 🔑 SSH
```bash
git clone git@github.com:Samizo-AITL/SemiDevKit.git
cd SemiDevKit
```

---

## 🐍 5. Python Environment (venv)

SemiDevKit consists of multiple independent tools.

📌 **Using separate virtual environments per tool is recommended.**

---

### 5.1 Create and activate venv  
(Linux / WSL2 / macOS)

```bash
cd SemiDevKit
python3 -m venv .venv
source .venv/bin/activate
```

---

### 5.2 Create and activate venv  
(Windows PowerShell)

```powershell
cd SemiDevKit
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 5.3 Install Python packages

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available (e.g., early releases):

```bash
pip install numpy scipy matplotlib pandas pyyaml
```

---

## 🧭 6. ngspice Path Configuration (Windows Native)

```powershell
setx PATH "$env:PATH;C:\Program Files\Spice64\bin"
```

```bash
ngspice
```

---

## 📁 7. Directory Overview

```
SemiDevKit/
 ├ bsim/        # BSIM4 analyzers (DC / CV / DIM / Reliability / Paramus)
 ├ tcad/        # TCAD playgrounds (MOSFET / PZT)
 ├ openlane/    # OpenLane-Lite (RTL → GDSII)
 ├ docs/        # Documentation
 ├ assets/      # GitHub Pages assets
 ├ README.md
 └ ChangeLog.md
```

---

## 🚀 8. Quick Test

### ✔ ngspice + BSIM Analyzer
```bash
cd bsim/analyzer_dc
python run/run_vgid.py
```

### ✔ Python Plot Test
```bash
python - <<EOF
import numpy as np
import matplotlib.pyplot as plt
plt.plot([0,1],[0,1])
plt.savefig("test.png")
print("OK")
EOF
```

---

## 🛠 9. Troubleshooting

### ❌ ngspice not found
- Verify installation
- Check PATH configuration
- 🪟 On Windows, **use WSL2** for best compatibility

### ❌ venv activation permission error (Windows)
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

## 📜 10. License Notes

SemiDevKit uses a **hybrid license model**.

| Scope | License |
|------|---------|
| 💻 Source Code | MIT License |
| 📘 Documentation / Diagrams | CC BY 4.0 |

---

## 📬 11. Contact

| Item | Details |
|-----|---------|
| 👤 Name | **Shinichi Samizo** |
| 🧑‍💻 GitHub | [Samizo-AITL](https://github.com/Samizo-AITL) |

---

🎉 **After installation, proceed to `docs/UsageGuide`**

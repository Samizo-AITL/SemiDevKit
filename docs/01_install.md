---
layout: default
title: install
---

----

# 1. Installation Guide (SemiDevKit)

This document describes how to install and prepare the environment for **SemiDevKit**, including TCAD playgrounds, BSIM4 analyzers, and OpenLane-Lite.

---

# 1. System Requirements

## 1.1 Supported OS
- Linux (Ubuntu 20.04/22.04 recommended)
- Windows 10/11 + **WSL2 Ubuntu**
- macOS (Intel / Apple Silicon)

---

# 2. Required Software

## 2.1 Python
SemiDevKit requires:

- **Python 3.9 – 3.12**

Check your version:

```bash
python3 --version
```

Install dependencies:

```bash
pip install numpy scipy matplotlib pandas pyyaml
```

Some analyzers use only numpy/matplotlib, others require pandas.

---

## 2.2 ngspice

SemiDevKit uses **ngspice** for SPICE-based device simulations.

### Linux (Ubuntu)

```bash
sudo apt update
sudo apt install -y ngspice
```

### macOS

```bash
brew install ngspice
```

### Windows (native or WSL2)
- Recommended: Install via **WSL2 Ubuntu**, then use Linux ngspice.
- Optional: Install Windows binary  
  https://ngspice.sourceforge.io/

Check installation:

```bash
ngspice --version
```

---

# 3. Recommended Tools

## 3.1 WSL2 (Windows Only)
Strongly recommended when running SemiDevKit on Windows.

Enable WSL2:

```powershell
wsl --install
```

Install Ubuntu from Microsoft Store, then inside Ubuntu:

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 3.2 Docker (for OpenLane-Lite)
Required for executing the full RTL→GDSII minimal flow.

Install Docker Desktop:

https://www.docker.com/products/docker-desktop/

Enable:
- WSL2 backend  
- Linux containers mode

---

## 3.3 Visual Studio Code
Recommended editor environment.

Install extensions:
- **Python**
- **Remote – WSL** (Windows only)
- **Markdown All in One**

---

# 4. Clone the Repository

## HTTPS
```bash
git clone https://github.com/Samizo-AITL/SemiDevKit.git
cd SemiDevKit
```

## SSH
```bash
git clone git@github.com:Samizo-AITL/SemiDevKit.git
cd SemiDevKit
```

---

# 5. Python Environment

SemiDevKit includes multiple tools (TCAD playground, BSIM analyzers, reliability framework).  
Each tool may use different dependencies, so **a dedicated venv per tool is recommended**.

---

## 5.1 Create and activate venv (Linux / WSL2 / macOS)

```bash
cd SemiDevKit
python3 -m venv .venv
source .venv/bin/activate
```

---

## 5.2 Create and activate venv (Windows PowerShell)

```powershell
cd SemiDevKit
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

## 5.3 Install Python packages

```bash
pip install -r requirements.txt
```

If you don’t have a requirements.txt (initial release), install manually:

```bash
pip install numpy scipy matplotlib pandas pyyaml
```

---

# 6. ngspice Path Configuration (Windows Only)

If using Windows native installation, add ngspice path:

```powershell
setx PATH "$env:PATH;C:\Program Files\Spice64\bin"
```

Verify:

```bash
ngspice
```

---

# 7. Directory Overview (Quick Reference)

```
SemiDevKit/
 ├ bsim/                # BSIM4 analyzers (DC / CV / DIM / Reliability / Paramus)
 ├ tcad/                # TCAD playgrounds (MOSFET / PZT)
 ├ openlane/            # OpenLane-Lite RTL → GDSII flow
 ├ docs/                # Documentation files
 ├ assets/              # CSS / web assets for GitHub Pages
 ├ README.md            # Project overview
 └ ChangeLog.md         # Version history
```

---

# 8. Quick Test

## Test ngspice

```bash
cd bsim/analyzer_dc
python run/run_vgid.py
```

## Test Python plotting

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

# 9. Troubleshooting

### ngspice not found
→ Install or add to PATH  
→ On Windows, use **WSL2** for best compatibility.

### Permission denied when activating venv (Windows)
Run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

# 10. License Notes

SemiDevKit uses a **hybrid license model**:

- **Source code → MIT License**  
- **Educational documents / diagrams → CC BY 4.0**

See `LICENSE.md` for details.

---

# 11. Contact

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---
layout: default
title: setup
---

----

# 2_setup.md

# SemiDevKit — Setup Guide

This document describes the setup steps required after installation.

## 1. Directory Structure

After cloning the repository, you should have the following structure:

```
SemiDevKit/
 ├ _includes/
 ├ _layouts/
 ├ assets/
 ├ bsim/
 ├ docs/
 ├ openlane/
 ├ tcad/
 ├ README.md
 ├ index.md
 └ config.yml
```

## 2. Environment Preparation

### Python virtual environment

Linux / macOS / WSL2:
```
cd SemiDevKit
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:
```
cd SemiDevKit
python -m venv .venv
.venv\Scripts\activate
```

### Install common packages

```
pip install numpy scipy matplotlib pandas pyyaml
```

## 3. Module‑Specific Setup

Each module (bsim, tcad, openlane-lite) may require additional setup.
Please refer to each module’s README inside:

- `bsim/analyzer_*`
- `tcad/tcad_playground`
- `tcad/tcad_playground_pzt`
- `openlane/openlane-lite`

## 4. ngspice (Required for BSIM tools)

Install ngspice:

### Windows
Download installer:
https://sourceforge.net/projects/ngspice/

### Linux
```
sudo apt install ngspice
```

### macOS
```
brew install ngspice
```

Ensure the command is available:
```
ngspice -v
```

## 5. VSCode Setup (Recommended)

Recommended extensions:
- Python
- Jupyter
- Markdown Preview
- Remote‑WSL (Windows only)

## 6. Next Step

Proceed to **3_usage.md** for how to run simulations and tools

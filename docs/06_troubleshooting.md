---
layout: default
title: troubleshooting
---

----

# 6_troubleshooting.md

# SemiDevKit — Troubleshooting Guide

This document summarizes common issues encountered when running **SemiDevKit modules**  
(TCAD Playgrounds, BSIM4 Analyzers, Paramus Physical Edition, and OpenLane-Lite)  
and provides recommended solutions.

---

# 1. Python-Related Issues

## 1.1 `ModuleNotFoundError`
Cause: Required Python packages are not installed.

Solution:

```bash
pip install numpy scipy matplotlib pandas pyyaml
```

If your virtual environment is corrupted:

```bash
deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
```

---

## 1.2 Virtual environment cannot be activated (Windows PowerShell)

Example error:
```
execution of scripts is disabled
```

Solution:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

# 2. ngspice Issues

## 2.1 `ngspice: command not found`

Solution (Linux):

```bash
sudo apt install ngspice
```

Solution (Windows native):

- Add ngspice to **PATH**, or  
- Use **WSL2**, which is strongly recommended

---

## 2.2 ngspice cannot open model file

Cause: Incorrect path to `models/*.sp`.

Solution:

- Check `.include "models/...sp"` in your netlist
- On Windows, **DO NOT use backslashes** → always use `/`

---

# 3. BSIM Analyzer Issues

## 3.1 VGID/VDID `.csv` not generated

Possible causes:

- `run/run_*.py` stopped due to an ngspice error  
- `.dat` file is empty

Check ngspice logs:

```bash
cat results/.../*.log
```

Common mistakes:

- Mismatched model name (`nmos` vs `nmos130`)
- Incorrect include path

---

## 3.2 gmmax extraction failure

Example error:
```
ValueError: zero-size array
```

Cause: `.dat` contains only one data line → sweep did not run.

Usually caused by incorrect `.model` parameters → ngspice failed to converge.

---

# 4. TCAD Playground Issues

## 4.1 Matplotlib backend error

Solution:

```bash
pip install matplotlib
sudo apt install python3-tk   # Linux
```

On WSL2:

```bash
export MPLBACKEND=Agg
```

---

## 4.2 Overflow / RuntimeWarning during simulation

Occurs when Poisson or MOSFET 1D model fails to converge.

Mitigation:

- Reduce doping (`Na = 1e16`)
- Increase oxide thickness (`tox = 5e-9`)
- Reduce voltage sweep range

---

# 5. OpenLane-Lite Issues

## 5.1 Docker permission error

Example:
```
permission denied: cannot access /var/run/docker.sock
```

Fix (Linux):

```bash
sudo usermod -aG docker $USER
```

Log out → Log in.

---

## 5.2 `run_in_docker.sh` cannot execute

Fix:

```bash
chmod +x docker/run_in_docker.sh
chmod +x scripts/run_flow.sh
```

---

## 5.3 PDK not found

OpenLane-Lite requires the following minimal PDK structure:

```
openlane-lite/pdks/...
```

Place or symlink your PDK accordingly.

---

# 6. Windows / WSL2 Issues

## 6.1 Cannot access files from Windows Explorer

WSL2 recommended directory access:

WSL Path:
```
/home/<user>/SemiDevKit
```

Windows Explorer:
```
\\wsl$\\Ubuntu\\home\\<user>\\SemiDevKit
```

---

## 6.2 Docker cannot detect WSL backend

Fix:

1. Open Docker Desktop  
2. Settings → General → Enable **Use the WSL2 backend**  
3. Check WSL version:

```powershell
wsl -l -v
```

Ensure Ubuntu is running under **WSL2**.

---

# 7. General Tips

- Always activate venv before running:
  ```bash
  source .venv/bin/activate
  ```
- Run Python scripts from the correct directory  
- Check ngspice `.log` files first when something goes wrong  
- DO NOT break directory structure  
- Linux / WSL2 is strongly recommended over Windows native

---

# 8. Contact

If the problem persists:

GitHub Issues:  
https://github.com/Samizo-AITL/SemiDevKit/issues

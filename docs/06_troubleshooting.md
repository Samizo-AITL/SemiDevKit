---
layout: default
title: troubleshooting
---

---

# 🛠 Troubleshooting Guide — SemiDevKit

This document summarizes **common issues encountered when running SemiDevKit modules**, including:

- 🧪 TCAD Playgrounds  
- 📐 BSIM4 Analyzers  
- 🧮 Paramus Physical Edition  
- 🏗 OpenLane-Lite  

For most problems, the root cause is related to **environment setup, PATH configuration, or execution order**.

---

## 🐍 1. Python-Related Issues

### 1.1 `ModuleNotFoundError`

**Cause**  
Required Python packages are not installed in the active environment.

**Solution**

```bash
pip install numpy scipy matplotlib pandas pyyaml
```

If the virtual environment is corrupted, recreate it:

```bash
deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
```

---

### 1.2 Virtual environment cannot be activated  
(Windows PowerShell)

**Example error**
```
execution of scripts is disabled
```

**Solution**

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

## ⚡ 2. ngspice Issues

### 2.1 `ngspice: command not found`

**Solution (Linux / WSL2)**

```bash
sudo apt install ngspice
```

**Solution (Windows native)**

- Add ngspice to **PATH**, or  
- Use **WSL2**, which is strongly recommended

---

### 2.2 ngspice cannot open model file

**Cause**  
Incorrect path to `models/*.sp`.

**Solution**

- Verify `.include "models/...sp"` in the netlist  
- On Windows, **do not use backslashes (`\`)** — always use `/`

---

## 📐 3. BSIM Analyzer Issues

### 3.1 VG–ID / VD–ID `.csv` not generated

**Possible causes**

- `run/run_*.py` terminated due to an ngspice error  
- Output `.dat` file is empty

**Check ngspice logs**

```bash
cat results/.../*.log
```

**Common mistakes**

- Model name mismatch (`nmos` vs `nmos130`)  
- Incorrect `.include` path

---

### 3.2 gmmax extraction failure

**Example error**
```
ValueError: zero-size array
```

**Cause**  
The `.dat` file contains only one data point → sweep did not execute.

This usually indicates **ngspice convergence failure** due to invalid `.model` parameters.

---

## 🧪 4. TCAD Playground Issues

### 4.1 Matplotlib backend error

**Solution**

```bash
pip install matplotlib
sudo apt install python3-tk   # Linux
```

For WSL2 (headless environment):

```bash
export MPLBACKEND=Agg
```

---

### 4.2 Overflow / RuntimeWarning during simulation

Occurs when the **Poisson or MOSFET 1D solver fails to converge**.

**Mitigation strategies**

- Reduce doping concentration (e.g. `Na = 1e16`)
- Increase oxide thickness (e.g. `tox = 5e-9`)
- Reduce voltage sweep range

---

## 🏗 5. OpenLane-Lite Issues

### 5.1 Docker permission error

**Example**
```
permission denied: cannot access /var/run/docker.sock
```

**Fix (Linux)**

```bash
sudo usermod -aG docker $USER
```

Log out and log back in.

---

### 5.2 `run_in_docker.sh` cannot execute

**Fix**

```bash
chmod +x docker/run_in_docker.sh
chmod +x scripts/run_flow.sh
```

---

### 5.3 PDK not found

OpenLane-Lite expects the following structure:

```
openlane-lite/pdks/...
```

Ensure that the PDK directory exists or is correctly symlinked.

---

## 🪟 6. Windows / WSL2 Issues

### 6.1 Cannot access files from Windows Explorer

**Recommended working directory (WSL2)**

WSL path:
```
/home/<user>/SemiDevKit
```

Access from Windows Explorer:
```
\\wsl$\Ubuntu\home\<user>\SemiDevKit
```

---

### 6.2 Docker cannot detect WSL backend

**Fix**

1. Open **Docker Desktop**  
2. Settings → General → Enable **Use the WSL2 backend**  
3. Verify WSL version:

```powershell
wsl -l -v
```

Ensure Ubuntu is running under **WSL2**.

---

## 💡 7. General Tips

- Always activate the virtual environment before running tools:
  ```bash
  source .venv/bin/activate
  ```
- Execute scripts from the **correct directory**
- Check ngspice `.log` files first when errors occur
- Do **not** modify the directory structure
- 🪟 Windows users should prefer **Linux / WSL2** over native execution

---

## 📬 8. Contact

For unresolved issues or questions:

| Item | Details |
|-----|---------|
| 👤 Name | **Shinichi Samizo** |
| 🧑‍💻 GitHub | https://github.com/Samizo-AITL |

---

🧭 **If a problem persists, isolate the module and verify dependencies step by step**

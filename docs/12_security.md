---
layout: default
title: security
---

---

# 🔐 Security Policy — SemiDevKit

This document defines the **security guidelines and expectations** for maintaining,  
distributing, and using **SemiDevKit**, including:

- 🧪 TCAD tools  
- 📐 BSIM4 analyzers  
- 🧮 Paramus Physical Edition  
- 🏗 OpenLane-Lite–based digital design workflows  

The goal is to ensure **safe, predictable, and reproducible execution** of semiconductor simulations and design flows.

---

## 🚨 1. Reporting Vulnerabilities

If you discover any **security-related issues**, including but not limited to:

- Arbitrary code execution vulnerabilities  
- Unsafe Python dependency usage  
- SPICE netlist injection risks  
- Docker container misconfiguration  
- Access-control or permission weaknesses in scripts  

Please report them via **one of the following private channels**:

🔒 **GitHub Security Advisories**  
https://github.com/Samizo-AITL/SemiDevKit/security/advisories

📧 **Email**  
shin3t72@gmail.com

> ⚠️ **Do not report security issues through public GitHub Issues.**

---

## 🛡 2. Scope of Security Protection

Security considerations apply to all components of SemiDevKit.

---

### 🐍 Python Scripts

- Avoid arbitrary command execution  
- Sanitize file paths used for ngspice batch execution  
- Do not use unsafe constructs such as `eval()`  
- Restrict usage of `subprocess` to controlled commands  

---

### ⚡ SPICE Netlists

- `.include` paths must not reference system-level or sensitive directories  
- Users should **not run untrusted `.cir` or `.sp` files** without inspection  
- Templates should be clearly separated from generated netlists  

---

### 🐳 Docker (OpenLane-Lite)

- Containers must not run with unnecessary root privileges  
- Avoid mounting sensitive host directories into containers  
- Validate environment variables before passing them into Docker  
- Prefer minimal Docker images for educational use  

---

### 📊 Data Files and Outputs

- CSV and DAT outputs must not overwrite unrelated system files  
- Ensure deterministic and predictable file naming under `results/`  
- Avoid writing outside module directories  

---

## 🧬 3. Supported Versions

Security maintenance and fixes are provided for:

- The **main** branch  
- The **latest tagged release**  
- Explicitly announced internal stable versions (if any)

Older branches and experimental forks may not receive security updates.

---

## 📦 4. Dependency Security

SemiDevKit depends on the following external components:

- **Python packages**: `numpy`, `scipy`, `matplotlib`, `pandas`, `pyyaml`  
- **SPICE simulator**: `ngspice`  
- **Docker** (required for OpenLane-Lite)

### Guidelines

- Use the latest stable versions whenever possible  
- Avoid deprecated ngspice commands or directives  
- Periodically review known CVEs for dependencies  
- Pin dependency versions (`requirements.txt`) for reproducibility  

---

## 🧠 5. Best Practices for Users

### Running Untrusted Code

- Do not run external Python or SPICE scripts inside SemiDevKit directories  
- Review scripts before execution, especially from unknown sources  

---

### Docker Safety

When using OpenLane-Lite:

```bash
docker info
```

- Ensure Docker is not running in **privileged mode**  
- Avoid exposing sensitive host paths  

---

### GitHub Token Safety

If interacting with GitHub Actions or APIs:

- Never commit Personal Access Tokens (PATs) to the repository  
- Use **GitHub Secrets** for any credentials  

---

## 🎯 6. Security Goals

SemiDevKit aims to provide:

- Safe and reproducible semiconductor workflows  
- Clear trust boundaries between user input and execution  
- Predictable behavior of TCAD, SPICE, and EDA tools  
- Protection against accidental data loss or system damage  

---

## 📬 7. Contact

For all security-related concerns:

📧 **Email**  
shin3t72@gmail.com  

🔒 **GitHub Security Advisories**  
https://github.com/Samizo-AITL/SemiDevKit/security/advisories

⏱ **Response Time**  
We aim to respond within **72 hours**.

---

© 2025 SemiDevKit Project. All rights reserved.

# 12_security.md
# SemiDevKit — Security Policy

This document defines the security guidelines for maintaining and distributing  
the SemiDevKit project, including TCAD tools, BSIM4 analyzers, Paramus Physical Edition,  
and OpenLane-Lite–based digital design workflows.

---

## 1. Reporting Vulnerabilities

If you discover any security-related issues, such as:

- Code execution vulnerabilities  
- Unsafe Python dependencies  
- SPICE netlist injection risks  
- Docker container misconfiguration  
- Access control weaknesses in scripts  

Please report them through:

🔒 GitHub Private Security Report  
https://github.com/Samizo-AITL/SemiDevKit/security/advisories

or via email:

📧 shin3t72@gmail.com

We do not accept security reports through public Issues.

---

## 2. Scope of Security Protection

Security considerations apply to:

### Python Scripts
- Avoid arbitrary command execution  
- Sanitize file paths for ngspice batch execution  
- Prevent unsafe eval() or subprocess abuse  

### SPICE Netlists
- .include paths must not reference system-level sensitive directories  
- Ensure users do not run untrusted .cir files  

### Docker (OpenLane-Lite)
- Containers must not run with unnecessary root privileges  
- Avoid mounting sensitive host directories  
- Validate environment variables before use  

### Data Files
- CSV output must not overwrite unrelated system files  
- Ensure predictable file naming under results/  

---

## 3. Supported Versions

Security maintenance is provided for:

- Main branch  
- Latest release tag  
- Specific internal stable versions (if announced)

Older branches may not receive fixes.

---

## 4. Dependency Security

SemiDevKit depends on:

- Python: numpy, scipy, matplotlib, pandas, pyyaml  
- SPICE tools: ngspice  
- Docker (for OpenLane-Lite)

Guidelines:

- Use the latest stable versions  
- Avoid deprecated ngspice directives  
- Review dependency CVEs periodically  
- Pin dependency versions for reproducibility (requirements.txt)  

---

## 5. Best Practices for Users

### Running Untrusted Code
Avoid running external SPICE or Python scripts inside SemiDevKit folders.

### Docker Safety
If using OpenLane-Lite:

docker info

Ensure the environment is secure and not running containers in privileged mode.

### GitHub Token Safety
If interacting with GitHub Actions:

- Never store PAT tokens in the repository  
- Use encrypted GitHub Secrets  

---

## 6. Security Goals

SemiDevKit aims to ensure:

- Safe and reproducible semiconductor workflows  
- Clear trust boundaries  
- Predictable execution of TCAD and SPICE tools  
- Protection against accidental data loss  

---

## 7. Contact

For all security issues:

📧 shin3t72@gmail.com  
GitHub Security Advisory  
https://github.com/Samizo-AITL/SemiDevKit/security/advisories

We respond within 72 hours.

---

© 2025 SemiDevKit Project. All Rights Reserved.

---
layout: default
title: contributing
---

---

# 🤝 Contributing Guide — SemiDevKit

Thank you for your interest in contributing to **SemiDevKit**!

SemiDevKit integrates **semiconductor device physics, compact modeling, reliability analysis,  
and physical design workflows**. Contributions that improve **clarity, correctness, usability,  
or educational value** are highly welcome.

---

## 🌱 1. Ways to Contribute

There are multiple ways to contribute to the project:

### ✔ 1. Improve Documentation
- Fix typos or unclear explanations
- Improve structure or wording
- Add diagrams, tables, or figures
- Contribute tutorials or example workflows

---

### ✔ 2. Submit Bug Reports

Please report issues via GitHub:

https://github.com/Samizo-AITL/SemiDevKit/issues

When reporting a bug, include:
- Operating system
- Python version
- ngspice version (if applicable)
- Exact error messages or logs
- Steps to reproduce
- Expected vs. actual behavior

---

### ✔ 3. Add New Features

Examples of welcome feature contributions include:
- New TCAD solvers (e.g. 2D Poisson, DD-lite)
- Additional BSIM4 analyzers
- Extended reliability models
- New PZT material or ferroelectric models
- OpenLane-Lite flow enhancements

---

### ✔ 4. Improve Code Quality
- Refactor existing scripts
- Add comments and docstrings
- Improve modularity and readability
- Reduce duplicated or hard-coded logic

---

## 🔁 2. Contribution Workflow

Please follow this standard GitHub workflow:

### Step 1 — Fork the Repository
```
https://github.com/Samizo-AITL/SemiDevKit
```

---

### Step 2 — Create a Feature Branch
```bash
git checkout -b feature/my-new-feature
```

---

### Step 3 — Make Your Changes
- Follow the coding and style guidelines (see below)
- Test your changes locally before committing

---

### Step 4 — Commit Message Guidelines

Use clear, descriptive commit messages:

```
Add new MOSCAP CV model
Fix ngspice path handling on Windows
Improve PZT hysteresis visualization
```

---

### Step 5 — Push and Open a Pull Request
```bash
git push origin feature/my-new-feature
```

Then open a **Pull Request** on GitHub with a clear description of your changes.

---

## 🧑‍💻 3. Coding Guidelines

### ✔ Python
- Follow **PEP8** style guidelines where practical
- Keep scripts short and readable
- Prefer functions over long procedural code
- Save plots under `fig/` and data under `results/`

---

### ✔ SPICE
- Store templates under `templates/`
- Use `.param` variables instead of hard-coded values
- Keep instance naming consistent (`m1`, `dut`, etc.)

---

### ✔ Documentation
- Use Markdown (`.md`)
- Add tables or diagrams where helpful
- Keep explanations **clear, concise, and technical**

---

## 🧩 4. Module Design Rules

To preserve reproducibility and clarity:

- Each module must be **self-contained**
- Modules must not depend on files outside their directory
- Use consistent subdirectory names:
  - `run/`
  - `plot/`
  - `models/`
  - `templates/`
  - `results/`
  - `fig/`
- Do **not** commit generated results, except for small demonstration examples

---

## 🧪 5. Testing Guidelines

Before submitting a Pull Request, please verify:

### ✔ TCAD Playground
- MOSFET and MOSCAP scripts execute successfully
- PNG figures are generated under `fig/`

---

### ✔ BSIM4 Analyzer
- `.csv`, `.dat`, `.log`, and `.png` files are generated
- Vth, gm, and Id extraction completes without error

---

### ✔ Reliability Analyzer
- HCI / NBTI scripts execute correctly
- ΔVth and ΔId degradation curves are reasonable

---

### ✔ OpenLane-Lite
- Docker-based flow runs successfully
- GDS output is produced for the example design

---

## 🎨 6. Style & Naming Conventions

### ✔ File Naming
- Use `lowercase_with_underscores`
- No spaces in file names

---

### ✔ Variable Naming
- Use `snake_case` for Python variables and functions

---

### ✔ Output Naming

Include the following when applicable:
- Technology node (e.g. `130nm`)
- Device type (`nmos` / `pmos`)
- Analysis mode (`vgid`, `vdid`, `cv`)
- Sweep condition (`LT`, `RT`, `HT`)

**Example:**
```
130nm_nmos_vgid_RT.csv
```

---

## ⚖️ 7. Licensing Rules for Contributions

SemiDevKit uses a **hybrid license model**:

| Component | License |
|---------|---------|
| Source code | MIT License |
| Documentation | CC BY or CC BY-SA |
| Figures | CC BY-NC |

By submitting a contribution, you agree that your work will be released under the same licensing terms.

---

## 🌟 8. Contributor Recognition

Contributors may be acknowledged through:
- GitHub contributor listings
- SemiDevKit documentation pages
- Acknowledgment sections in future release notes

---

## 📬 9. Contact

If you would like to discuss an idea before contributing:

| Item | Details |
|-----|---------|
| 👤 Name | **Shinichi Samizo** |
| 🧑‍💻 GitHub | https://github.com/Samizo-AITL |

---

🙏 **Thank you for helping improve SemiDevKit!**

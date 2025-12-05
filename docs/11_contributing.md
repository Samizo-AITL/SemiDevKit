# 11_contributing.md
# Contributing to SemiDevKit

Thank you for your interest in contributing to **SemiDevKit**!  
This project integrates semiconductor device physics, compact modeling, reliability analysis,  
and physical design flows. High-quality contributions are welcome.

---

# 1. How to Contribute

There are several ways to contribute:

### ✔ 1. Improve documentation
- Fix typos, unclear explanations, missing diagrams
- Add tutorials or examples for any module

### ✔ 2. Submit bug reports
Report issues here:  
https://github.com/Samizo-AITL/SemiDevKit/issues

Include:
- OS, Python version, ngspice version
- Exact error message
- Steps to reproduce
- Expected vs. actual behavior

### ✔ 3. Add new features
Examples:
- New TCAD solvers (2D Poisson, DD-lite)
- New BSIM analyzers
- Additional reliability models
- New PZT material models
- OpenLane-Lite extensions

### ✔ 4. Improve code quality
- Refactor scripts
- Add comments
- Increase modularity
- Reduce duplicated code

---

# 2. Contribution Workflow

Follow this process when making a contribution:

### **Step 1 — Fork the Repository**
```
https://github.com/Samizo-AITL/SemiDevKit
```

### **Step 2 — Create a Feature Branch**
```
git checkout -b feature/my-new-feature
```

### **Step 3 — Make Changes**
- Follow coding guidelines (below)
- Test before committing

### **Step 4 — Commit Message Format**
Use clear and descriptive messages:

```
Added new MOSCAP CV model
Fixed ngspice path handling on Windows
Improved PZT hysteresis visualization
```

### **Step 5 — Push & Create Pull Request**
```
git push origin feature/my-new-feature
```

Then open a Pull Request on GitHub.

---

# 3. Coding Guidelines

### ✔ Python
- Use **PEP8 style** wherever possible
- Keep scripts small and readable
- Prefer functions over long procedural code
- Use `fig/` for images, `results/` for outputs

### ✔ SPICE
- Keep templates under `templates/`
- Use `.param` variables instead of hard-coded values
- Maintain consistency in instance names (`m1`, `dut`, etc.)

### ✔ Documentation
- Use Markdown (`.md`)
- Include diagrams or tables where helpful
- Keep language **clear and concise**

---

# 4. Module Design Rules

### ✔ Each module must be self-contained  
No module should rely on files outside its folder.

### ✔ Use consistent directory names  
- `run/`
- `plot/`
- `models/`
- `templates/`
- `results/`
- `fig/`

### ✔ Do not commit generated results
Except for demonstration examples.

---

# 5. Testing Guidelines

Before submitting a PR:

### ✔ TCAD Playground
- Run MOSFET & MOSCAP scripts
- Verify PNG images are generated

### ✔ BSIM4 Analyzer
- Ensure `.csv`, `.dat`, `.log`, `.png` are produced
- Check Vth/gm/Ids extraction runs without error

### ✔ Reliability Analyzer
- Run HCI/NBTI scripts
- Confirm ΔVth / ΔId curves look correct

### ✔ OpenLane-Lite
- Ensure Docker script runs
- Produce GDS in example design

---

# 6. Style & Naming Rules

### ✔ File naming
Use `lowercase_with_underscores.md`, no spaces.

### ✔ Variable naming
Use `snake_case` for Python.

### ✔ Output naming
Include:
- node (e.g., 130nm)
- device (nmos/pmos)
- mode (vgid/vdid/cv)
- sweep condition (LT/RT/HT)

Example:
```
130nm_nmos_vgid_RT.csv
```

---

# 7. Licensing Rules for Contributions

SemiDevKit uses a **hybrid license**:

| Component | License |
|----------|---------|
| Source code | MIT |
| Documentation | CC BY or CC BY-SA |
| Figures | CC BY-NC |

By contributing, you agree your contribution will be released under the same hybrid licensing.

---

# 8. Contributor Recognition

Contributors will be credited in:

- GitHub contributors list  
- SemiDevKit documentation pages  
- Acknowledgment section in future release notes  

---

# 9. Contact

For discussion before contributing:

GitHub Issues:  
https://github.com/Samizo-AITL/SemiDevKit/issues

Thank you for contributing to SemiDevKit!

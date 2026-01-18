---
layout: default
title: faq
---

---

# ❓ Frequently Asked Questions (FAQ) — SemiDevKit

This FAQ summarizes **commonly asked questions** when using **SemiDevKit**, including:

- 🧪 TCAD Playgrounds  
- 📐 BSIM4 Analyzers  
- 🧮 Paramus Physical Edition  
- 🏗 OpenLane-Lite  
- General semiconductor device simulation workflows  

---

## 🌐 1. General Questions

### Q1. What is SemiDevKit?

**SemiDevKit** is a **modular educational toolkit** covering the full spectrum of semiconductor device and design workflows, including:

- Semiconductor device physics (Poisson equation, MOSFET models)  
- BSIM4 compact modeling and SPICE-based analysis  
- Reliability modeling (HCI, NBTI)  
- Digital physical design (OpenLane-Lite)  
- Ferroelectric (PZT) behavior  
- Physical parameter extraction (Paramus)

---

### Q2. Which operating system is recommended?

**Linux or Windows with WSL2** is strongly recommended.  
Native Windows execution is possible but not preferred.

---

### Q3. Does SemiDevKit require a GPU?

No.  
All simulations are **CPU-based** and do not require GPU acceleration.

---

## 🐍 2. Python & Environment

### Q4. Which Python version should I use?

**Python 3.9 – 3.12** is recommended.

---

### Q5. Should I use a virtual environment?

Yes.  
Using a Python virtual environment (`venv`) is strongly recommended to avoid dependency conflicts.

---

### Q6. I get `ModuleNotFoundError`. What should I do?

Install the required dependencies:

```bash
pip install numpy scipy matplotlib pandas pyyaml
```

Ensure the correct virtual environment is activated before running any scripts.

---

## ⚡ 3. ngspice / SPICE Issues

### Q7. ngspice cannot find a model file.

Ensure that `.include` paths use **forward slashes (`/`)**, not backslashes (`\`), especially on Windows.

---

### Q8. A sweep produced only one data point.

This usually indicates a **simulation failure**.  
Check the ngspice `.log` files for convergence or syntax errors.

---

### Q9. gmmax extraction fails.

This typically means the sweep data is incomplete, often due to invalid or non-converging model parameters.

---

## 🧪 4. TCAD Playground Questions

### Q10. The Poisson solver diverges.

Try the following mitigation steps:

- Reduce doping concentration  
- Increase oxide thickness (`tox`)  
- Reduce the voltage sweep range  

---

### Q11. Why do results differ from commercial TCAD tools?

The TCAD playgrounds use **simplified 1D educational models**.  
They are intended for **conceptual understanding and trend analysis**, not production-level accuracy.

---

## 🧬 5. Reliability (HCI / NBTI)

### Q12. Are the HCI / NBTI models accurate?

They are **simplified models** designed for education and qualitative trend analysis.

---

### Q13. Can I fit the models to real measurement data?

Yes.  
You can adjust fitting parameters such as:

- `A_vth`, `p_vth`  
- `A_id`, `p_id`  

to match experimental degradation data.

---

## 🏗 6. OpenLane-Lite

### Q14. OpenLane-Lite cannot find the PDK.

Ensure the following directory exists:

```
openlane-lite/pdks/
```

---

### Q15. Docker does not work in WSL2.

Verify that the WSL2 backend is enabled in Docker Desktop and check:

```powershell
wsl -l -v
```

Ensure your Linux distribution is running under **WSL2**.

---

## 🤝 7. Contribution

### Q16. How can I contribute to SemiDevKit?

Contributions are welcome via **Issues** or **Pull Requests**:

https://github.com/Samizo-AITL/SemiDevKit

---

## 📜 8. License

### Q17. What license does SemiDevKit use?

SemiDevKit uses a **hybrid license model**:

- **MIT License** — source code  
- **CC BY / CC BY 4.0** — documentation text  
- **CC BY-NC 4.0** — figures and diagrams  

See `license.md` for full details.

---

## 📬 9. Contact

For additional questions or clarifications:

| Item | Details |
|-----|---------|
| 👤 Name | **Shinichi Samizo** |
| 🧑‍💻 GitHub | https://github.com/Samizo-AITL |

---

💡 **If your question is not listed here, feel free to open an Issue on GitHub.**

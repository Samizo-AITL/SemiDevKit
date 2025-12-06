---
layout: default
title: faq
---

----

# 7_faq.md
# SemiDevKit — Frequently Asked Questions (FAQ)

This FAQ summarizes common questions when using **SemiDevKit**, including TCAD Playgrounds,  
BSIM4 Analyzers, Paramus Physical Edition, OpenLane-Lite, and general semiconductor simulation workflows.

---

# 1. General Questions

### Q1. What is SemiDevKit?
SemiDevKit is a modular educational toolkit covering:
- Semiconductor device physics (Poisson, MOSFET models)
- BSIM4 compact modeling and SPICE analysis
- Reliability modeling (HCI, NBTI)
- Physical design (OpenLane-Lite)
- PZT ferroelectric behavior
- Parameter extraction (Paramus)

### Q2. Which OS is recommended?
Linux or WSL2 is strongly recommended.

### Q3. Does SemiDevKit require GPU?
No. All simulations are CPU-based.

---

# 2. Python & Environment

### Q4. Which Python version is required?
Python 3.9–3.12 recommended.

### Q5. Should I use a virtual environment?
Yes, to avoid version conflicts.

### Q6. I get ModuleNotFoundError. What should I do?
Install dependencies:
```
pip install numpy scipy matplotlib pandas pyyaml
```

---

# 3. ngspice / SPICE Issues

### Q7. ngspice cannot find model file.
Use forward slashes `/` in .include paths.

### Q8. Sweep produced only one data point.
Simulation failed — check .log files.

### Q9. gmmax extraction fails.
Sweep data incomplete (usually model error).

---

# 4. TCAD Playground Questions

### Q10. Poisson solver diverges.
Try:
- Reduce doping
- Increase tox
- Reduce sweep range

### Q11. Why different from real TCAD?
These are simplified educational models.

---

# 5. Reliability (HCI/NBTI)

### Q12. Are HCI/NBTI models accurate?
They are simplified, for trend study and education.

### Q13. Can real data be fitted?
Yes — adjust A_vth, p_vth, A_id, p_id.

---

# 6. OpenLane-Lite

### Q14. PDK not found.
Ensure:
```
openlane-lite/pdks/
```

### Q15. Docker issues in WSL2.
Enable WSL2 backend in Docker Desktop:
```
wsl -l -v
```

---

# 7. Contribution

### Q16. How can I contribute?
Submit Issues or PRs:
https://github.com/Samizo-AITL/SemiDevKit

---

# 8. License

### Q17. What is the license?
Hybrid license:
- MIT for code
- CC BY / CC BY-SA for text
- CC BY-NC for figures

---

# 9. Contact
GitHub Issues:
https://github.com/Samizo-AITL/SemiDevKit/issues

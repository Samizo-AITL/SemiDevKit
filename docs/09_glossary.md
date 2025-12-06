---
layout: default
title: glossary
---

----

# 9_glossary.md
# SemiDevKit — Glossary of Technical Terms

This glossary defines key semiconductor, SPICE, TCAD, and physical‑design terms used across **SemiDevKit**.

---

# A

### **AC Analysis**
Small‑signal frequency‑domain analysis used to obtain gain, impedance, or frequency response.

### **Anneal**
Thermal treatment used to activate dopants or modify material properties.

---

# B

### **BSIM4**
A physics‑based MOSFET compact model widely used in SPICE simulators for deep‑submicron CMOS nodes (130 nm → 20 nm).

### **Butterfly Curve (S–E Curve)**
Strain–Electric field curve for ferroelectric or piezoelectric materials.

---

# C

### **Cgg**
Total gate capacitance:  
Cgg = ∂Qg/∂Vg, physically meaningful compared to partitioned Cgs/Cgd/Cgb.

### **CV Curve**
Capacitance–Voltage relation for MOSCAPs or MOSFET gate behavior.

### **Compact Model**
Simplified mathematical representation of device I–V/C–V used in circuit simulators.

---

# D

### **DIBL (Drain-Induced Barrier Lowering)**
Reduction of threshold voltage with increasing drain voltage in short‑channel MOSFETs.

### **DIM (Dimension Sweep)**
L/W sweep used to study short‑channel and narrow‑width effects.

---

# E

### **EOT (Equivalent Oxide Thickness)**
Effective thickness of gate dielectric, accounting for high‑k materials.

### **Extracted Parameters**
Measured or simulated device characteristics such as Vth, gmmax, Idlin, Idsat.

---

# F

### **Ferroelectric**
Material exhibiting spontaneous polarization reversible by electric field (used in PZT analysis).

---

# G

### **gm (Transconductance)**
Derivative of Id w.r.t Vg. gmmax is often used for Vth extraction.

---

# H

### **HCI (Hot-Carrier Injection)**
Reliability degradation mechanism in NMOS due to high‑energy carriers damaging the gate oxide.

---

# I

### **Idsat**
Saturation drain current at high Vd.

### **Idlin**
Linear‑region drain current at low Vd.

---

# L

### **Lateral Electric Field**
Field along the channel direction; strongly influences hot‑carrier effects.

### **Layout**
Geometric representation of circuit shapes for fabrication.

---

# M

### **Mobility (μ)**
Carrier mobility; decreases with vertical field, scattering, and temperature.

### **MOSCAP**
Metal‑Oxide‑Semiconductor capacitor used for CV characterization.

---

# N

### **NBTI (Negative Bias Temperature Instability)**
PMOS reliability degradation mechanism producing negative Vth shift.

---

# O

### **OpenLane**
Open‑source RTL‑to‑GDS flow; OpenLane‑Lite is a reduced version included in SemiDevKit.

---

# P

### **Paramus**
Physical‑to‑BSIM4 model card generator included in SemiDevKit.

### **Poisson Equation**
Governs electrostatic potential inside semiconductor materials; solved in TCAD modules.

### **PZT**
Lead Zirconate Titanate, a ferroelectric/piezoelectric material.

---

# R

### **Results Directory**
Folder storing *.csv, *.dat, *.png, and extracted parameters for reproducibility.

---

# S

### **SCE (Short-Channel Effects)**
Phenomena degrading device behavior as channel length shrinks.

### **SPICE**
Simulation Program with Integrated Circuit Emphasis—industry standard analog simulator.

---

# T

### **TCAD (Technology CAD)**
Device‑level simulation techniques (Poisson, drift‑diffusion, quantum corrections).

### **Template**
SPICE netlist skeleton used by analyzers to generate simulation cases.

---

# V

### **Vth (Threshold Voltage)**
Gate voltage where inversion forms; extracted via gmmax or constant‑current method.

### **Vtg / Vtc**
Threshold values extracted via:
- gmmax peak method (Vtg)
- constant‑current method (Vtc)

---

# W

### **Width (W)**
MOSFET conduction width; strongly impacts current and SCE.

---

# Z

### **Zr/Ti Ratio**
Composition variable in PZT models affecting polarization behavior.

---

# End of Glossary

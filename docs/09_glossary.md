---
layout: default
title: glossary
---

---

# 📘 Glossary of Technical Terms — SemiDevKit

This glossary defines **key semiconductor, SPICE, TCAD, and physical-design terms**  
used throughout **SemiDevKit**.

---

## A

### **AC Analysis**
Small-signal, frequency-domain analysis used to evaluate gain, impedance, and frequency response.

---

### **Anneal**
A thermal process used to activate dopants, repair lattice damage, or modify material properties.

---

## B

### **BSIM4**
A physics-based MOSFET compact model widely used in SPICE simulators for deep-submicron CMOS technologies  
(typically from 130 nm down to ~20 nm nodes).

---

### **Butterfly Curve (S–E Curve)**
Strain–electric-field relationship observed in ferroelectric or piezoelectric materials.

---

## C

### **Cgg**
Total gate capacitance, defined as:

\[
C_{gg} = \frac{\partial Q_g}{\partial V_g}
\]

Physically more meaningful than partitioned capacitances (Cgs, Cgd, Cgb).

---

### **CV Curve**
Capacitance–voltage relationship used to characterize MOS capacitors and MOSFET gate behavior.

---

### **Compact Model**
A simplified mathematical representation of device I–V and C–V characteristics used in circuit simulation.

---

## D

### **DIBL (Drain-Induced Barrier Lowering)**
Reduction of threshold voltage with increasing drain voltage in short-channel MOSFETs.

---

### **DIM (Dimension Sweep)**
A sweep of channel length (L) and width (W) used to study short-channel and narrow-width effects.

---

## E

### **EOT (Equivalent Oxide Thickness)**
Effective oxide thickness that represents the capacitance of a high-k gate dielectric in terms of SiO₂.

---

### **Extracted Parameters**
Device characteristics derived from measurement or simulation, such as Vth, gmmax, Idlin, and Idsat.

---

## F

### **Ferroelectric**
A material exhibiting spontaneous polarization that can be reversed by an applied electric field.

---

## G

### **gm (Transconductance)**
Derivative of drain current with respect to gate voltage:

\[
g_m = \frac{\partial I_d}{\partial V_g}
\]

The peak value (gmmax) is commonly used for threshold voltage extraction.

---

## H

### **HCI (Hot-Carrier Injection)**
A reliability degradation mechanism in NMOS devices caused by high-energy carriers damaging the gate oxide.

---

## I

### **Idsat**
Drain current in the saturation region at high drain voltage.

---

### **Idlin**
Drain current in the linear region at low drain voltage.

---

## L

### **Lateral Electric Field**
Electric field along the channel direction; a major contributor to hot-carrier effects.

---

### **Layout**
Geometric representation of circuit structures used for semiconductor fabrication.

---

## M

### **Mobility (μ)**
Carrier mobility; typically decreases with increasing vertical electric field, scattering, and temperature.

---

### **MOSCAP**
Metal-Oxide-Semiconductor capacitor, commonly used for CV characterization of gate dielectrics.

---

## N

### **NBTI (Negative Bias Temperature Instability)**
A PMOS reliability degradation mechanism that causes a negative shift in threshold voltage over time.

---

## O

### **OpenLane**
An open-source RTL-to-GDSII digital design flow.  
**OpenLane-Lite** is a reduced, educational variant included in SemiDevKit.

---

## P

### **Paramus**
A physical-parameter-based BSIM4 model-card generator included in SemiDevKit.

---

### **Poisson Equation**
A fundamental equation governing electrostatic potential inside semiconductor materials;  
solved numerically in TCAD modules.

---

### **PZT**
Lead Zirconate Titanate, a ferroelectric and piezoelectric material widely used in memory and sensor devices.

---

## R

### **Results Directory**
A directory storing generated `.csv`, `.dat`, `.png`, and extracted parameters to ensure reproducibility.

---

## S

### **SCE (Short-Channel Effects)**
Phenomena that degrade MOSFET behavior as channel length is reduced.

---

### **SPICE**
Simulation Program with Integrated Circuit Emphasis — an industry-standard circuit simulator.

---

## T

### **TCAD (Technology Computer-Aided Design)**
Device-level simulation techniques including Poisson, drift-diffusion, and quantum-corrected models.

---

### **Template**
A SPICE netlist skeleton used by analyzers to automatically generate simulation cases.

---

## V

### **Vth (Threshold Voltage)**
Gate voltage at which strong inversion forms in a MOSFET.

---

### **Vtg / Vtc**
Threshold voltages extracted using:
- **Vtg**: gmmax peak method  
- **Vtc**: constant-current method  

---

## W

### **Width (W)**
MOSFET conduction width; strongly affects drive current and short-channel behavior.

---

## Z

### **Zr/Ti Ratio**
Composition ratio in PZT materials that significantly influences polarization characteristics.

---

📘 **End of Glossary**

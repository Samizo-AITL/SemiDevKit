* ============================================================
*  PMOS 130nm BSIM4 v4.8 Base Model (generated per L/W)
* ============================================================

.model 130nm_pmos_w1000 pmos level=54
+ version      = 4.8
+ capmod       = 2
+ toxm         = 2.3e-9
+ toxe         = 2.3e-9
+ toxp         = 2.3e-9

* ---- Threshold Voltage ----
+ vth0         = -0.382
+ k1           = 0.5
+ k2           = -0.03
+ voff         = 0.05
+ nfactor      = 1.3

* ---- Mobility / Velocity Sat ----
+ u0           = 0.01045
+ ua           = 2e-09
+ ub           = 5e-19
+ uc           = 0.1
+ vsat         = 1500000.0

* ---- Short Channel Effects ----
+ dvt0         = 0.7
+ dvt1         = 0.3
+ dvt2         = 0.0
+ dvt1w        = 5000000.0
+ w0           = 1e-07

* ---- DIBL / Drain Effects ----
+ eta0         = 0.1
+ etab         = -0.05
+ pclm         = 0.25
+ pdiblc1      = 0.02
+ pdiblc2      = 0.005

* ---- Resistances ----
+ rdsw         = 73.8
+ wr           = 1.0

* ---- Capacitances ----
+ cgso         = 2.5e-10
+ cgdo         = 2.5e-10
+ cgbo         = 1e-10
+ xpart        = 0

* ---- Other ----
+ prt          = 1

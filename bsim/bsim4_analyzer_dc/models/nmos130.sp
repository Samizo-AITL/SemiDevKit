* =============================================================
*  NMOS 130nm BSIM4 v4.8 Model  (for ngspice, DC analysis)
* =============================================================

.model nmos130 nmos level=54
+ version      = 4.8
+ capmod       = 2

* ---- Physical / Geometry ----
+ toxm         = 2.3e-9
+ toxe         = 2.3e-9
+ toxp         = 2.3e-9
+ nch          = 1e18

* ---- Threshold Voltage ----
+ vth0         = 0.40
+ k1           = 0.50
+ k2           = -0.03
+ voff         = -0.05
+ nfactor      = 1.3

* ---- Mobility / Velocity Sat ----
+ u0           = 0.0135
+ ua           = 2e-9
+ ub           = 5e-19
+ uc           = 0.1
+ vsat         = 1.5e6

* ---- Short Channel Effects ----
+ dvt0         = 0.70
+ dvt1         = 0.30
+ dvt2         = 0.00
+ dvt1w        = 5e6
+ w0           = 1e-7

* ---- DIBL / Drain Effects ----
+ eta0         = 0.10
+ etab         = -0.05
+ pclm         = 0.25
+ pdiblc1      = 0.02
+ pdiblc2      = 0.005

* ---- Resistances ----
+ rdsw         = 80
+ wr           = 1.0

* ---- Capacitances ----
+ cgso         = 2.5e-10
+ cgdo         = 2.5e-10
+ cgbo         = 1.0e-10
+ xpart        = 0

* ---- Other ----
+ prt          = 1


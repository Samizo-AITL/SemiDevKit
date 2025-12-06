* ============================================================
*  PMOS 130nm BSIM4 v4.8 Base Model (generated per L/W)
* ============================================================

.model 130nm_pmos_{CODE} pmos level=54
+ version      = 4.8
+ capmod       = 2
+ toxm         = 2.3e-9
+ toxe         = 2.3e-9
+ toxp         = 2.3e-9

* ---- Threshold Voltage ----
+ vth0         = {VTH0}
+ k1           = {K1}
+ k2           = {K2}
+ voff         = {VOFF}
+ nfactor      = {NFACTOR}

* ---- Mobility / Velocity Sat ----
+ u0           = {U0}
+ ua           = {UA}
+ ub           = {UB}
+ uc           = {UC}
+ vsat         = {VSAT}

* ---- Short Channel Effects ----
+ dvt0         = {DVT0}
+ dvt1         = {DVT1}
+ dvt2         = {DVT2}
+ dvt1w        = {DVT1W}
+ w0           = {W0}

* ---- DIBL / Drain Effects ----
+ eta0         = {ETA0}
+ etab         = {ETAB}
+ pclm         = {PCLM}
+ pdiblc1      = {PDIBLC1}
+ pdiblc2      = {PDIBLC2}

* ---- Resistances ----
+ rdsw         = {RDSW}
+ wr           = {WR}

* ---- Capacitances ----
+ cgso         = {CGSO}
+ cgdo         = {CGDO}
+ cgbo         = {CGBO}
+ xpart        = {XPART}

* ---- Other ----
+ prt          = 1

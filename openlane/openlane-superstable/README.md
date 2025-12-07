# OpenLane Superstable — SPM Flow Result

This directory records a verified flow execution of **OpenLane (superstable)** using the example design **SPM (Simple Processor Model)**.

The flow successfully produced:
- Final GDS (`spm.gds`)
- Final DEF/LEF
- Timing & area reports
- Verified GUI visualization in **OpenROAD**

---

## ✔️ 1. Generated GDS Result (KLayout View)

### Full-chip layout
![spm_gds_full](/assets/openlane-superstable/spm_gds_full.png)

### Transistor-level detail (poly/diffusion layers)
![spm_gds_dif_poly](/assets/openlane-superstable/spm_gds_dif_poly.png)

---

## ✔️ 2. OpenROAD GUI — LEF/DEF Loaded

### Global view
![openroad_1](/assets/openlane-superstable/openroad_1.png)

### Detailed routing view
![openroad_2](/assets/openlane-superstable/openroad_2.png)

---

## ✔️ 3. Commands Used (Inside OpenLane Container)

### Load technology and design

```tcl
openroad
read_lef designs/spm/runs/<RUN>/tmp/merged.nom.lef
read_def designs/spm/runs/<RUN>/results/final/def/spm.def
Read Liberty (optional for timing view)
read_liberty /openlane/pdks/sky130A/.../sky130_fd_sc_hd__tt_025C_1v80.lib
```

---

## ✔️ 4. Example Report

###  Area report

```
report_design_area
Design area 4114 u^2 51% utilization.
```

---

## ✔️ 5. Export (Optional)

```
write_def out.def
write_lef out.lef
write_db out.db
```

---

## Notes

- This flow corresponds to OpenLane superstable revision ff5509f.
- Verified inside the official OpenLane container.
- No modification to source code; only standard configuration was used.





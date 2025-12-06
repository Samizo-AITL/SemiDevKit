---
layout: default
title: ChangeLog
---

----

# ChangeLog | SemiDevKit

All notable updates to **SemiDevKit** will be documented in this file.  
This project follows a human-readable, developer-friendly update style.

---

## [0.1.1] – 2025-12-07
### Added
- Added **reference example figures** across all major modules:
  - TCAD Playground (MOSCAP, MOSFET, Poisson, PZT modules)
  - BSIM4 analyzers (DC / CV / DIM / Reliability)
  - OpenLane-Lite (GDS layouts, GTKWave simulation output)
- Unified image formatting across GitHub Pages:
  - Absolute URLs for stable rendering
  - `<img>` tags with `width="80%"` for visual consistency
- Improved documentation readability in:
  - `tcad/`  
  - `bsim/`  
  - `openlane/openlane-lite/`  
  - Top-level `README.md`

### Improved
- Enhanced GitHub Pages compatibility for all images and linked assets  
- Added badge-style links for subdirectories, improving navigation  
- Updated Document Index with badge-linked navigation to individual docs

---

## [0.1.0] – 2025-012-06
### Added
- Initial public release of **SemiDevKit**  
- Integrated project structure for:
  - TCAD playground (MOSFET, MOSCAP, Poisson solvers)
  - PZT ferroelectric simulation tools
  - BSIM4 DC/CV analyzers
  - BSIM4 reliability analyzers (NBTI/HCI)
  - BSIM4 DIM (L/W sweep) tools
  - OpenLane-Lite (simplified VLSI physical design environment)
- GitHub Pages site created with:
  - MathJax support
  - Mermaid diagrams
  - Custom CSS (GitHub-style tables & typography)
  - English-only documentation mode

### Improved
- Refined repository layout for clarity and module separation
- Added badges, official links, and project index to `index.md`

### Known Issues
- No automated testing pipeline yet
- OpenLane-Lite documentation planned but incomplete

---

## Future Plans
- Multi-language documentation (English / Japanese)
- Add automated SPICE/Verilog test suites
- Provide example PDK templates for OpenLane-Lite
- Expand BSIM4 model extraction tutorial
- Add interactive notebooks (Jupyter/Python)
- 

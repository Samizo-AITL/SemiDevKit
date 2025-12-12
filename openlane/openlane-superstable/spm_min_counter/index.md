---
layout: default
title: spm_min_counter
---

# spm_min_counter — Minimal RTL Flow

---

##  Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/SemiDevKit/openlane/openlane-superstable/spm_min_counter) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/SemiDevKit/tree/main/openlane/openlane-superstable/spm_min_counter) |

---

## Purpose
- Verify OpenLane superstable with self-authored minimal RTL
- Confirm GDS generation without flow modification

## Design
- Counter only
- Single clock domain
- No macro, no SRAM

## Constraints (planned)
- CLOCK_PERIOD = 10ns
- FP_CORE_UTIL = 30%

## Expected Result
- GDS generation
- Stable CTS

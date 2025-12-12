# spm_min_counter — Minimal RTL Flow

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

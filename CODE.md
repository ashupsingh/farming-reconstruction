# Source entry points

Runnable new implementation: `reconstruction/model.py`; checks: `reconstruction/test_model.py`. Hardware implementation: `reconstruction/firmware/firmware.ino`. Read `CIRCUIT.md` before use.

## Earlier design notes

# Code and implementation record

## Original source status

Historical portfolio description only; original source, measurements and photographs not supplied.

No original code recovered for this project. Exact pin maps, libraries, timings and circuit values are intentionally not invented.

## Reconstructed pseudocode

This is newly written explanatory pseudocode, not executable firmware and not historical evidence.

```text
read sample
attach calibration version
reject invalid values
queue telemetry
display freshness and trend
```

## What is needed before implementation

Confirm actual hardware/software interfaces, units, validation rules and failure states. Follow the separate methodology and its test plan. Do not merge this with Farm monitoring unless they were the same build. Yield or water savings require controlled comparisons.

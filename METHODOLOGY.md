# Connected Farming: methodology

Status: researched reconstruction / proposed evaluation, prepared 23 October 2026. Not a recovered lab notebook.

## Existing account

Combined sensor monitoring and data analytics to support the optimization of agricultural conditions. A personal project exploring connected hardware and practical monitoring workflows.

The account above comes from the existing portfolio and is not independent verification. Listed stack: ESP Modules, IoT Sensors, Cloud Dashboard, Data Analytics. Exact components and versions still need confirmation.

## System architecture

Environmental sensors -> validated telemetry -> historical dashboard -> advisory review

## Proposed engineering workflow

1. Specify which agricultural variables were actually measured.
2. Store raw values alongside calibration and units.
3. Detect offline devices, outliers and changing conditions.
4. Evaluate monitoring quality before claiming agronomic optimization.

## Evaluation plan, not results

Record: Data completeness; calibration error; offline detection delay. Use explicit units, test conditions, a baseline where relevant, repeated observations and a timestamped log. Report failure cases alongside successes. No numerical result is available from this reconstruction.

## Limitations and claim boundaries

Do not merge this with Farm monitoring unless they were the same build. Yield or water savings require controlled comparisons.

## Design questions for an interview

- Explain the input, decision and output paths in the architecture above.
- What concrete fault would invalidate the output, and how would you detect it?
- Which design decision did you personally make, and what evidence do you retain?
- Which part of this proposed workflow differs from what you actually built?

## Research basis

[Espressif ADC calibration](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc/adc_calibration.html) — consulted 23 October 2026. This source supports the underlying engineering topic, not the historical implementation. Workflow and evaluation proposals above are original analysis for this project.

# DFDC

This folder is reserved for the raw DFDC dataset files.

## Role in the script
The pipeline reads original DFDC video files from this directory before:
- format checking
- metadata generation
- quality validation
- compliance routing
- logging

## Config-aligned path
Configured raw path:
`01_raw_data/DFDC/`

Configured output path:
`02_processed/isolation/license/video/DFDC/`

## License and routing note
DFDC is currently treated as:
- `commercial_use: unknown`
- `redistribution: forbidden`
- `pool_assignment: isolation`
- `review_status: pending`

According to the script rules, datasets with `commercial_use = unknown` are not allowed to enter the main processing candidate pool at the current stage.

## Repository note
Actual dataset files are not uploaded to this repository.
Only placeholder structure and documentation are maintained here.

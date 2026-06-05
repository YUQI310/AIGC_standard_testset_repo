# Celeb-DF

This folder is reserved for the raw Celeb-DF dataset files.

## Role in the script
The pipeline reads the original video files from this directory before:
- normalization
- metadata registration
- quality checks
- compliance review
- routing to the appropriate processed directory

## Config-aligned path
Configured raw path:
`01_raw_data/Celeb-DF/`

Configured output path:
`02_processed/isolation/license/video/Celeb-DF/`

## License and routing note
Based on the documented application terms, Celeb-DF is currently treated as:
- `commercial_use: forbidden`
- `redistribution: forbidden`
- `pool_assignment: isolation`
- `review_status: rejected`

The current script logic keeps this dataset in the repository structure for registration, license auditing, and isolation logging only.

## Repository note
Actual dataset files are not uploaded to this repository.
Access to the dataset should follow the official application procedure.

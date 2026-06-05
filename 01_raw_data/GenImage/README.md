# GenImage

This folder is reserved for the raw GenImage dataset files.

## Role in the script
The pipeline reads original image files from this directory as raw inputs for:
- file inspection
- normalization
- metadata generation
- quality checks
- license compliance routing

## Config-aligned path
Configured raw path:
`01_raw_data/GenImage/`

Configured output path:
`02_processed/isolation/license/image/GenImage/`

## License and routing note
GenImage is currently treated as:
- `commercial_use: forbidden`
- `redistribution: restricted`
- `pool_assignment: isolation`
- `review_status: rejected`

Therefore, this dataset is registered for ingestion and audit trail purposes, but it is not included in the current candidate pool.

## Repository note
Actual raw dataset files are not redistributed in this repository.

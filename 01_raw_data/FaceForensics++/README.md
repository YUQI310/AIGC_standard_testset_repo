# FaceForensics++

This folder is reserved for the raw FaceForensics++ dataset files.

## Role in the script
The pipeline reads the original video files from this directory as source inputs for:
- ingestion registration
- file validation
- metadata generation
- compliance routing
- audit logging

## Config-aligned path
Configured raw path:
`01_raw_data/FaceForensics++/`

Configured output path:
`02_processed/isolation/license/video/FaceForensics++/`

## License and routing note
Based on the documented access terms, FaceForensics++ is currently treated as:
- `commercial_use: forbidden`
- `redistribution: restricted`
- `pool_assignment: isolation`
- `review_status: rejected`

It is retained in the repository structure for access registration, compliance audit, and isolation traceability, but it is not included in the current processing candidate pool.

## Repository note
Actual raw dataset content is not uploaded or redistributed in this repository.

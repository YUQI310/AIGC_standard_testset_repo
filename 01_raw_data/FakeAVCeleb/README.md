# FakeAVCeleb

This folder is reserved for the raw FakeAVCeleb dataset files.

## Role in the script
The pipeline reads original files from this directory as raw inputs for:
- dataset ingestion
- metadata generation
- quality validation
- compliance screening
- isolation routing
- audit logging

## Config-aligned path
Configured raw path:
`01_raw_data/FakeAVCeleb/`

Configured output path:
`02_processed/isolation/license/video/FakeAVCeleb/`

## License and routing note
Based on the documented usage restrictions, FakeAVCeleb is currently treated as:
- `commercial_use: forbidden`
- `redistribution: forbidden`
- `pool_assignment: isolation`
- `review_status: rejected`

It is therefore retained only for access registration, compliance review, and traceable isolation under the current pipeline design.

## Repository note
Actual raw dataset content is not uploaded or redistributed in this repository.

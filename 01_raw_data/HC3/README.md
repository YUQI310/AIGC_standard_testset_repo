# HC3

This folder is reserved for the raw HC3 dataset files.

## Role in the script
The pipeline reads HC3 raw text data from this directory before:
- format normalization
- metadata generation
- quality validation
- deduplication
- compliance routing

## Config-aligned path
Configured raw path:
`01_raw_data/HC3/`

Configured output path:
`02_processed/pending_review/text/HC3/`

## License and routing note
HC3 is currently treated as:
- `commercial_use: restricted`
- `redistribution: restricted`
- `pool_assignment: pending_review`
- `review_status: pending`

Therefore, HC3 should not automatically enter the candidate pool unless the restriction terms are manually reviewed and cleared.

## Repository note
Actual raw dataset content is not uploaded to this repository.
Only folder placeholders and documentation are stored here.

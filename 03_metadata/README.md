# Metadata Directory

This directory stores structured metadata files generated during dataset ingestion, normalization, validation, and compliance routing.

## Intended contents
- `text_metadata.jsonl`
- `image_metadata.jsonl`
- `video_metadata.jsonl`
- optional merged metadata files such as `all_metadata.jsonl`

## Design principle
Metadata is stored separately from raw or processed content.
The metadata files are intended to record:
- source dataset
- source path
- standard label
- license status
- routing result
- review status
- quality check result
- audit-related fields

## Repository status
Current files in this directory are placeholders for schema demonstration and repository completeness.
They do not represent actual pipeline outputs yet.
# Metadata Outputs

Expected metadata outputs include:
- `text_metadata.jsonl`
- `image_metadata.jsonl`
- `video_metadata.jsonl`

Additional subdirectories may be used for:
- `manifest/`
- `review_logs/`
- `license_reports/`

This repository currently keeps structure placeholders only.

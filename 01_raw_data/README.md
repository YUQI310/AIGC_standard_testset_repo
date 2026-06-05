# Raw Data Archive

This directory stores the raw datasets before any normalization, cleaning, deduplication, compliance routing, or metadata generation.

## Purpose in the pipeline
According to the script design, this directory is used for:
- raw dataset ingestion
- original file archival
- reproducibility and trace-back
- reprocessing when downstream conversion fails

The pipeline reads dataset files from dataset-specific subfolders under `01_raw_data/`.

## Important repository rule
This repository does **not** upload or redistribute actual raw dataset content.

Reasons:
- some datasets are large and unsuitable for GitHub storage
- some datasets are subject to access restrictions, research-only terms, or redistribution prohibitions
- this repository is designed as a pipeline prototype, compliance-routing framework, and documentation repository rather than a data distribution repository

## Expected folder structure
Each dataset should have its own subfolder, for example:
- `01_raw_data/HC3/`
- `01_raw_data/GenImage/`
- `01_raw_data/DFDC/`
- `01_raw_data/FaceForensics++/`
- `01_raw_data/Celeb-DF/`
- `01_raw_data/FakeAVCeleb/`
- `01_raw_data/DeeperForensics-1.0/`

## Script-related note
Files placed here are treated as the original source inputs of the pipeline.
After ingestion, samples may be routed to:
- `02_processed/candidate_pool/`
- `02_processed/pending_review/`
- `02_processed/isolation/license/`
- `02_processed/isolation/compliance/`
- `02_processed/isolation/corrupted/`

The routing decision depends on license status, review status, file validity, and compliance screening results.

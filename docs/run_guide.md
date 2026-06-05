# Run Guide

## Purpose
This document explains the expected environment, folder structure, configuration file, and example execution flow for the dataset ingestion, normalization, cleaning, metadata generation, compliance routing, and review preparation pipeline.

## Current repository status
This repository currently presents the project structure, configuration design, placeholder scripts, and documentation framework.

Actual execution on full public datasets is expected to be performed locally after dataset download and environment preparation. Raw datasets, processed outputs, runtime logs, and generated reports are not redistributed in this repository.

## Expected environment

### Python
Recommended version:
- Python 3.9 or above

### Suggested Python dependencies
Typical dependencies mentioned in the project design include:
- pandas
- pillow
- numpy
- opencv-python
- pyyaml

Optional or environment-dependent tools may be added later depending on the implementation details of:
- text deduplication
- image validation
- video inspection
- review result merging
- compliance precheck models

### External tools
For video normalization and inspection, the local environment should provide:
- FFmpeg
- FFprobe

## Repository structure expected by the pipeline
The pipeline is designed around the following directory layout:

```text
AIGC_standard_testset/
├── 01_raw_data/
├── 02_processed/
├── 03_metadata/
├── 04_reports/
├── 05_logs/
├── config/
├── docs/
├── examples/
└── src/
Notes
raw_path should match the actual folder under 01_raw_data/
output_path should match the designed routing destination under 02_processed/
commercial_use, review_status, and restriction_cleared should stay consistent with the compliance-routing logic
dataset-specific cleaning thresholds may override global defaults if implemented later
Designed processing flow
The pipeline is designed to perform the following steps:

load dataset configuration
access raw dataset folders
detect data modality and file format
normalize outputs into standard formats
generate sample-level metadata
perform basic quality checks
apply deduplication or deduplication-ready flags
run compliance precheck and license routing
export metadata, logs, and reports
optionally generate review sampling files
optionally merge manual review results if provided
Standardized output targets
Normalized formats
The design expects the following normalized formats:

text → JSONL
image → JPEG
video → MP4
Routing logic
The processed output directory is designed to reflect sample status:

02_processed/candidate_pool/
02_processed/pending_review/
02_processed/isolation/license/
02_processed/isolation/compliance/
02_processed/isolation/corrupted/
Typical modal subfolders include:

text/
image/
video/
Record status design reference
Sample-level metadata is expected to use engineering status values such as:

ingested
normalized
validated
candidate_ready
pending_review
isolated_license
isolated_compliance
isolated_corrupted
rejected
sampled_for_label_review
These values describe processing flow status rather than final legal or policy conclusions.

Example run command
If your executable entry file is:
src/main.py
then the typical local command is:
python src/main.py
If later you add command-line arguments, a possible extended form may look like:
python src/main.py --config config/datasets_config.yaml
At the current repository stage, the exact command-line interface may still be a placeholder depending on how main.py is implemented.

Expected outputs after execution
After a local run, the project may produce outputs such as:

Processed files
Stored under:

02_processed/candidate_pool/
02_processed/pending_review/
02_processed/isolation/
Metadata files
Stored under:

03_metadata/text_metadata.jsonl
03_metadata/image_metadata.jsonl
03_metadata/video_metadata.jsonl
Reports
Possible report-style outputs under 04_reports/:

processing_summary.md
dataset_statistics.csv
label_accuracy_report.csv
filtering_reason_stats.csv
compliance_review_summary.md
Logs
Possible logs under 05_logs/:

pipeline.log
warning.log
error.log
Manual review workflow
If the review modules are implemented, the pipeline may also support:

review sample list generation
label review result merging
dataset-level label accuracy calculation
dataset review status updates
Possible output files include:

review_sample_list.csv
review_result_merged.csv
label_accuracy_report.csv
label_error_type_stats.csv
Common pre-run checklist
Before running locally, check the following:

Python environment is available
required Python packages are installed
FFmpeg and FFprobe are installed if video data is involved
config/datasets_config.yaml exists
raw dataset folders exist under 01_raw_data/
output directories exist or can be created
file paths in the config are consistent with the repository structure
Common execution risks
Typical issues that may interrupt or affect processing include:
missing raw dataset files
incorrect raw_path or output_path
broken image or video files
text encoding errors
missing label mappings
unavailable FFmpeg installation
write failure due to missing directories or permissions
The intended handling strategy is:
catch file-level exceptions
write errors to logs
continue processing other samples or datasets where possible
Scope boundary
This run guide describes the intended execution logic of the repository design.

This repository is not intended to:

redistribute original public datasets
provide pre-generated full processed outputs
provide production-ready compliance judgment
replace dataset-specific license review or formal legal assessment
Recommended local execution order
A practical local order is:
download datasets locally
place them into 01_raw_data/
verify config/datasets_config.yaml
confirm output folders
run python src/main.py
inspect 05_logs/ for runtime issues
inspect 03_metadata/ for generated records
inspect 04_reports/ for summaries and review outputs
manually review pending or isolated samples if required
Future extension note
This guide matches the current repository design stage. If the codebase later adds:
CLI arguments
environment files
dependency lock files
review-result input files
content risk model integration
Label Studio interfaces
then this document should be updated accordingly.

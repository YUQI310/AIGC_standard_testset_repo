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

由于部分公开数据集存在体积较大、下载权限限制、禁止再分发、非商用限制或授权状态不明确等问题，本仓库不直接上传或分发受限原始样本。

## Raw Data Handling Policy- 对许可明确允许公开使用的数据，可保留必要的样本或元数据记录。
- 对许可受限、授权不完整或不适合进入公开仓库的数据集，仅保留元数据、来源链接和处理记录。
- 对视觉类和音视频类受限数据集，当前阶段主要采用 metadata_only 或 isolated_license 状态管理。
- 所有原始数据处理均应保留来源信息、原始路径、标签文件路径和许可状态。

## Dataset Access Status| Dataset | Modality | Raw Data Distribution in This Repository | Status |
|---|---|---|---|
| HC3 | Text | Metadata and processed records can be retained | allowed / kept |
| GenImage | Image | Raw samples are not redistributed | restricted / metadata_only |
| DFDC | Video | Raw samples are not redistributed | restricted / metadata_only |
| FaceForensics++ | Video | Raw samples are not redistributed | restricted or unknown |
| Celeb-DF | Video | Raw samples are not redistributed | restricted or unknown |
| FakeAVCeleb | Audio-Video / Video | Raw samples are not redistributed | restricted or unknown |
| DeeperForensics-1.0 | Video | Raw samples are not redistributed | restricted / metadata_only |

This repository records data governance results rather than redistributing restricted datasets.

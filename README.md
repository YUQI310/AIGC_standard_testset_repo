# AIGC Standard Testset Repository

本项目用于构建一个面向风控合规与评测场景的 AI 生成内容/深伪数据基础库，支持对公开文本、图像、视频数据集进行统一接入、标准化处理、基础清洗、元数据生成、许可合规分流和抽样复核准备。

## 项目目标
- 统一接入公开数据集
- 对文本、图像、视频数据进行标准化处理
- 生成统一元数据
- 执行基础质量校验、去重和内容风险预筛
- 按许可状态与处理策略进行分流
- 形成可复核、可审计的候选样本池

## 当前支持的数据集
- HC3（text）
- GenImage（image）
- DFDC（video）
- FaceForensics++（video，许可隔离）
- Celeb-DF（video，许可隔离）
- FakeAVCeleb（video，许可隔离）

## 处理流程
配置读取 → 数据接入/原始归档 → 格式识别 → 标准化转换 → 元数据生成 → 基础质量校验 → 去重处理 → 内容风险预筛 → 许可合规分流 → 抽样复核清单生成 → 日志记录 → 结果导出

## 目录结构
- `config/` 配置文件
- `docs/` 设计与说明文档
- `examples/` 示例输出
- `src/` 核心脚本
- `tests/` 测试文件
- `01_raw_data/` 原始数据归档
- `02_processed/` 处理结果与分流目录
- `03_metadata/` 元数据输出
- `04_reports/` 处理报告
- `05_logs/` 运行日志

## 处理后目录说明
- `02_processed/normalized/` 已标准化，但不代表已准入
- `02_processed/candidate_pool/` 满足候选池准入条件
- `02_processed/pending_review/` 需人工复核
- `02_processed/isolation/license/` 许可不明或不满足要求
- `02_processed/isolation/compliance/` 内容风险隔离
- `02_processed/isolation/corrupted/` 损坏或不可处理样本

## 状态字段说明
样本主状态 `record_status` 建议包括：
- `ingested`
- `normalized`
- `validated`
- `candidate_ready`
- `pending_review`
- `isolated_license`
- `isolated_compliance`
- `isolated_corrupted`
- `rejected`
- `sampled_for_label_review`

## 说明
本仓库当前以项目结构、配置设计、处理流程和标准化输出规范为主，作为第二阶段“公开
## Current Progress

Current repository progress:
- repository folder structure has been created
- raw-data placeholder directories for target datasets have been added
- dataset registration config has been drafted in `config/datasets_config.yaml`
- compliance-routing and metadata-planning documents have been added under `docs/`
- core script placeholders have been created under `src/`
- report and log directories have been reserved as pipeline output locations

At the current stage, this repository mainly presents the project’s pipeline design, compliance-triage structure, configuration layout, and documentation framework.
Actual dataset downloading, local conversion, metadata generation, and report output are expected to be executed locally rather than inside this GitHub repository.

## Scope

This repository is intended to demonstrate:
- how public datasets are registered and organized before processing
- how different datasets are routed based on license and review status
- how processed outputs are expected to be separated into candidate, pending-review, and isolation paths
- how metadata, reports, and logs are structurally planned for later stages

This repository is not intended to:
- redistribute raw datasets
- provide full processed dataset outputs
- serve as a production-ready data processing platform
- replace local execution environments required for actual conversion and validation



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
  ## 当前进展
当前仓库已完成以下内容：
已建立仓库的基础目录结构
已为目标数据集添加原始数据占位目录
已在 config/datasets_config.yaml 中完成数据集注册配置草案
已在 docs/ 目录下补充合规分流与元数据规划文档
已在 src/ 目录下创建核心脚本占位文件
已预留报告与日志目录，作为后续流程输出位置
在当前阶段，本仓库主要展示项目的流程设计、合规分流结构、配置布局和文档框架。
实际的数据集下载、本地格式转换、元数据生成和报告输出，预计在本地环境中执行，而不是直接在 GitHub 仓库内完成。
## 仓库范围
本仓库主要用于展示以下内容：
公共数据集在处理前如何进行注册与组织
不同数据集如何依据许可状态和复核状态进行分流
处理后输出如何在 candidate、pending-review 和 isolation 路径中分开存放
元数据、报告和日志在后续阶段的结构化规划方式
本仓库不用于：
重新分发原始数据集
提供完整的处理后数据输出
作为可直接投入使用的生产级数据处理平台
替代实际格式转换与验证所需的本地运行环境
## 仓库适配说明
本仓库是在原始脚本设计文档基础上整理形成的结构化实现骨架。原文中配置文件写作 config/datasets_config.json，为便于展示与维护，仓库中采用 config/datasets_config.yaml 进行适配保存。部分分流路径与目录映射属于基于文档流程整理后的仓库实现表达，并非声称对原始脚本文件进行逐字复刻。

当前阶段的重点不是直接产出最终标准测试集，而是对首批核心公开数据集进行统一接入、格式标准化、自动化清洗、许可分流、抽样复核和基础统计分析，判断其是否具备进入基础数据集池或候选池的条件。

## Stage Scope本阶段覆盖的公开数据集包括：

- HC3：文本数据集- GenImage：图像数据集- DFDC：视频数据集- FaceForensics++：视频数据集- Celeb-DF：视频数据集- FakeAVCeleb：音视频/视频数据集- DeeperForensics-1.0：视频数据集需要说明的是，纳入处理范围不等同于纳入基础候选池。数据集是否进入候选池，需要结合标准化结果、自动化清洗结果、抽样复核结果、许可状态和数据集级综合判断确定。

## Current Validation Result当前批次结果显示：

| Dataset | Modality | Sample Count | Current Status | Candidate Pool |
|---|---:|---:|---|---|
| HC3 | Text |400 | kept | Yes |
| GenImage | Image |10000 | isolated_license / metadata_only | No |
| DFDC | Video |10000 | isolated_license / metadata_only | No |
| DeeperForensics-1.0 | Video |10000 | isolated_license / metadata_only | No |
| FaceForensics++ | Video | pending | pending / metadata_only | No |
| Celeb-DF | Video | pending | pending / metadata_only | No |
| FakeAVCeleb | Audio-Video / Video | pending | pending / metadata_only | No |

HC3 已完成标准化、自动化清洗和5% 抽样复核，标注准确率为95%，达到当前阶段90% 的候选池准入参考阈值。

视觉类和音视频类数据集因许可、授权或公开分发限制，在当前公开仓库阶段主要保留元数据、来源记录和处理状态，不直接上传或分发原始样本。

## Repository Structure```text00_docs/ Project reports and documentation01_raw_data/ Raw data source records and access notes02_standardized_data/ Standard schema and standardized metadata design03_quality_validation/ Dataset-level quality validation summaries04_sampling_review/ Sampling review protocol and review records05_statistics/ Statistical summaries and analysis tables06_script/ Scripts or script descriptions07_outputs/ Output tables, figures, and stage deliverables```

## Main Stage Outputs-公开数据集质量验证报告- 数据集状态汇总表- 标准化元数据字段说明- 自动化质量验证规则说明- 抽样复核协议与记录模板- 基础候选池与隔离池状态记录## Important NotesDue to dataset size, license restrictions, and redistribution limitations, this repository does not directly redistribute restricted raw datasets. For restricted or unclear-license datasets, the repository only keeps metadata, source information, validation status, and processing records.

标准化完成不代表质量验证通过；质量验证通过也不代表最终测试集已经形成。当前仓库记录的是第二阶段公开数据集质量验证成果。

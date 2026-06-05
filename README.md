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

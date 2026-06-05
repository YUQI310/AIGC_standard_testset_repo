# Pipeline Design

本项目采用模块化处理流程，对公开文本、图像、视频数据集进行统一接入、标准化转换、基础清洗、元数据生成、许可合规分流和抽样复核准备。

## 总体流程
配置读取 → 数据接入/原始归档 → 格式识别 → 标准化转换 → 元数据生成 → 基础质量校验 → 去重处理 → 内容风险预筛 → 许可合规分流 → 抽样复核清单生成 → 日志记录 → 结果导出

## 各阶段说明

### 1. 配置读取
读取数据集名称、原始路径、输出路径、许可信息、标签映射规则、清洗阈值、抽样参数等配置。

### 2. 数据接入与原始归档
将已下载的数据集接入统一处理入口，保留原始目录结构和原始文件，便于回溯。

### 3. 格式识别
识别文本、图像、视频模态及其原始文件格式，检查是否满足处理条件。

### 4. 标准化转换
- 文本统一转为 JSONL
- 图像统一转为 JPEG
- 视频统一转为 MP4

### 5. 元数据生成
为每条样本补充统一字段，包括：
- data_id
- source_dataset
- source_sample_id
- content_type
- raw_label
- standard_label
- license_type
- commercial_use
- review_status
- record_status

### 6. 基础质量校验
执行空白过滤、损坏文件过滤、缺失字段检查、低质量样本初筛等。

### 7. 去重处理
进行同数据集内去重，并为跨数据集去重预留接口。

### 8. 内容风险预筛
对可能涉及色情、暴力等高风险内容进行预筛标记，仅用于风险提示和后续人工复核。

### 9. 许可合规分流
根据 commercial_use、restriction_cleared 和风险状态将样本路由到 candidate_pool、pending_review 或 isolation。

### 10. 抽样复核
生成供人工复核使用的样本清单，并为后续标签准确率统计预留接口。

## 输出目录分层
- `01_raw_data/` 原始数据
- `02_processed/normalized/` 标准化结果
- `02_processed/candidate_pool/` 候选池
- `02_processed/pending_review/` 待复核
- `02_processed/isolation/` 隔离区
- `03_metadata/` 元数据
- `04_reports/` 报告
- `05_logs/` 日志

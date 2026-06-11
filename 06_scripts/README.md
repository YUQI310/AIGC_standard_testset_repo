# Scripts

本文件夹用于存放公开数据集质量验证阶段的自动化脚本或脚本说明。

当前阶段脚本功能包括：

1. 数据集接入登记；
2. 格式标准化；
3. 元数据生成；
4. 自动化质量验证；
5. 许可状态分流；
6. 重复与近重复检测；
7. 抽样复核清单生成；
8. 基础统计分析。

## Planned Script Files

建议后续补充以下脚本：

```text
format_standardization.py
quality_validation.py
sampling_review.py
statistics_analysis.py

Processing Logic
raw data access
→ dataset registration
→ format standardization
→ metadata generation
→ quality validation
→ license routing
→ sampling review
→ dataset-level statistics
→ candidate pool / isolated pool / pending pool
Status Definition
normalized：已完成标准化，待进一步验证；
kept：已通过当前阶段规则验证，保留在候选流程中；
isolated_quality：因样本质量问题被隔离；
isolated_license：因许可限制、授权不完整或不适合公开分发而被隔离；
pending_review：当前规则无法稳定判断，需要人工进一步确认；
failed_label_quality：因数据集级标注质量未达到阈值而不予保留；
dropped：已明确剔除；
metadata_only：不保留或不分发原始样本，仅保留元数据、来源链接和处理记录。

# Metadata Schema

为保证不同模态、不同来源数据集能够在同一套处理链路中统一管理，本项目采用统一元数据字段设计。

## 基础字段
- `data_id`：统一样本ID
- `content_type`：样本模态，text/image/video
- `source_dataset`：来源数据集名称
- `source_split`：来源划分，如 train/test
- `source_sample_id`：原始样本ID
- `source_uri`：原始样本路径或来源位置

## 标签字段
- `raw_label`：原始标签
- `standard_label`：标准化标签
- `label_mapping_rule`：标签映射规则
- `label_mapping_confidence`：映射置信度

## 质量字段
- `quality_status`：质量校验结果
- `quality_reasons`：质量问题原因
- `quality_score`：质量评分
- `file_hash_sha256`：文件哈希

## 合规字段
- `license_type`：许可证类型
- `license_source`：许可证来源
- `commercial_use`：商用许可状态
- `redistribution`：再分发状态
- `derivative_obligation`：衍生作品义务
- `content_compliance_status`：内容合规状态
- `content_risk_tags`：风险标签
- `restriction_cleared`：限制条件是否已确认满足

## 流转与复核字段
- `record_status`：当前工程状态
- `review_status`：人工复核状态
- `isolation_reason`：隔离原因
- `remark`：备注说明

## 审计字段
- `ingest_batch_id`：处理批次ID
- `ingest_time`：接入时间
- `processor_version`：脚本版本号

## 建议状态值
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

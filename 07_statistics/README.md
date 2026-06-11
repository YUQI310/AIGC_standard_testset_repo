 统计目录说明：`05_statistics/README.md

md
# Statistics

本文件夹用于存放公开数据集质量验证阶段的统计分析结果。

## Current Statistics

当前阶段已形成以下核心统计结论：

1. HC3 文本数据集进入基础候选池；
2. HC3 当前样本数量为 400；
3. HC3 完成 5% 抽样复核，抽样数量为 20；
4. HC3 标注准确率为 95%，达到 90% 准入参考阈值；
5. GenImage、DFDC、DeeperForensics-1.0 等视觉类数据集因许可、授权或公开分发限制被记录为 isolated_license / metadata_only；
6. 当前视觉类数据集不进入公开基础候选池；
7. 后续需要通过授权数据、宽松协议数据或内部生成数据补充图像、视频和音视频候选数据。

## Suggested Statistical Files

后续可补充以下统计文件：
text
dataset_distribution.csv
label_distribution.csv
filter_reason_statistics.csv
sampling_accuracy_summary.csv
candidate_pool_statistics.csv

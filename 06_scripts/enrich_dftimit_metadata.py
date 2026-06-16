import json
from pathlib import Path

BASE_DIR = Path(r"C:\Users\ASUS\Desktop\DF-TIMIT")
META_FILE = BASE_DIR / "03_metadata" / "video_metadata.jsonl"
OUT_FILE  = BASE_DIR / "03_metadata" / "video_metadata_enriched.jsonl"

records = []
with open(META_FILE, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        r = json.loads(line.strip())

        # 基础字段
        r["data_id"]                  = f"DFTIMIT_{i:06d}"
        r["content_type"]             = "video"
        r["source_dataset"]           = "DF-TIMIT"
        r["source_split"]             = "unknown"
        r["source_sample_id"]         = r.get("filename", "")
        r["source_uri"]               = r.get("absolute_path", "")

        # 标签字段
        r["raw_label"]                = "fake"
        r["standard_label"]           = "fake"
        r["label_mapping_rule"]       = "DF-TIMIT全集均为deepfake样本，直接映射为fake"
        r["label_mapping_confidence"] = "high"

        # 生成信息
        r["generation_model"]         = "GAN-based face swap (DF-TIMIT)"
        r["manipulation_type"]        = "face_swap"

        # 合规字段
        r["commercial_use"]           = "forbidden"
        r["license"]                  = "research_only"
        r["restriction_cleared"]      = False

        # 质量字段（占位，后续视频探针脚本填充）
        r["duration_sec"]             = None
        r["resolution"]               = None
        r["fps"]                      = None
        r["codec"]                    = None
        r["has_audio"]                = None
        r["file_size_bytes"]          = None

        # 审计字段
        r["ingest_stage"]             = "01_metadata_built"
        r["review_status"]            = "pending"

        records.append(r)

with open(OUT_FILE, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"完成：共写入 {len(records)} 条记录")
print(f"输出：{OUT_FILE}")

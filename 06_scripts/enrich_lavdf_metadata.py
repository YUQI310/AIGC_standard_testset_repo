import json
import csv
import os
from pathlib import Path

# ── 路径配置 ──────────────────────────────────────────
METADATA_PATH = r"C:\Users\ASUS\Desktop\metadata.json"
OUTPUT_JSONL   = r"C:\Users\ASUS\Desktop\DF-TIMIT\06_scripts\lavdf_enriched.jsonl"
OUTPUT_STATS   = r"C:\Users\ASUS\Desktop\DF-TIMIT\06_scripts\lavdf_stats.csv"
SOURCE_DATASET = "LAV-DF"

# ── 标签映射 ──────────────────────────────────────────
def get_standard_label(record):
    if record["n_fakes"] == 0:
        return "real"
    elif record["modify_video"] and record["modify_audio"]:
        return "fake_av"        # 音视频均伪造
    elif record["modify_video"]:
        return "fake_video"     # 仅视频伪造
    elif record["modify_audio"]:
        return "fake_audio"     # 仅音频伪造
    else:
        return "fake_unknown"

def get_manipulation_type(record):
    if record["n_fakes"] == 0:
        return ""
    parts = []
    if record["modify_video"]:
        parts.append("video_manipulation")
    if record["modify_audio"]:
        parts.append("audio_manipulation")
    return "+".join(parts) if parts else "unknown"

# ── 主处理 ────────────────────────────────────────────
def main():
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"总样本数：{len(data)}")

    stats = {"train": {"real":0,"fake":0}, 
             "dev":   {"real":0,"fake":0}, 
             "test":  {"real":0,"fake":0}}

    os.makedirs(os.path.dirname(OUTPUT_JSONL), exist_ok=True)

    with open(OUTPUT_JSONL, "w", encoding="utf-8") as out:
        for idx, record in enumerate(data):
            split  = record.get("split", "unknown")
            std_label = get_standard_label(record)
            raw_label = "real" if record["n_fakes"] == 0 else "fake"

            enriched = {
                # 基础字段
                "data_id"               : f"LAVDF_{idx+1:06d}",
                "content_type"          : "video",
                "source_dataset"        : SOURCE_DATASET,
                "source_split"          : split,
                "source_sample_id"      : record["file"],
                "source_uri"            : record["file"],
                "raw_label"             : raw_label,
                "standard_label"        : std_label,
                "label_mapping_rule"    : "n_fakes==0→real; modify_video/audio→fake type",
                "label_mapping_confidence": "high",
                "generation_model"      : "",
                "manipulation_type"     : get_manipulation_type(record),

                # LAV-DF 专有字段
                "duration_sec"          : record.get("duration"),
                "video_frames"          : record.get("video_frames"),
                "audio_channels"        : record.get("audio_channels"),
                "audio_frames"          : record.get("audio_frames"),
                "n_fakes"               : record.get("n_fakes"),
                "fake_periods"          : record.get("fake_periods"),
                "modify_video"          : record.get("modify_video"),
                "modify_audio"          : record.get("modify_audio"),
                "transcript"            : record.get("transcript", ""),
                "original_file"         : record.get("original"),
            }

            out.write(json.dumps(enriched, ensure_ascii=False) + "\n")

            # 统计
            if split in stats:
                stats[split][raw_label] += 1

    # ── 输出统计 CSV ──────────────────────────────────
    with open(OUTPUT_STATS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["split", "real", "fake", "total"])
        total_real = total_fake = 0
        for sp, cnt in stats.items():
            writer.writerow([sp, cnt["real"], cnt["fake"], cnt["real"]+cnt["fake"]])
            total_real += cnt["real"]
            total_fake += cnt["fake"]
        writer.writerow(["ALL", total_real, total_fake, total_real+total_fake])

    print(f"enriched JSONL → {OUTPUT_JSONL}")
    print(f"统计 CSV       → {OUTPUT_STATS}")
    print("\n各划分统计：")
    for sp, cnt in stats.items():
        print(f"  {sp:6s}  real={cnt['real']:6d}  fake={cnt['fake']:6d}")

if __name__ == "__main__":
    main()

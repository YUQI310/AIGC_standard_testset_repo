# -*- coding: utf-8 -*-
import json, os
from pathlib import Path

# ========== 配置区 ==========
INPUT_FILES = {
    "finance":  r"C:\Users\ASUS\Desktop\HC3原始数据\HC3标准化输出\finance_标准化.jsonl",
    "medicine": r"C:\Users\ASUS\Desktop\HC3原始数据\HC3标准化输出\medicine_标准化.jsonl",
    "open_qa":  r"C:\Users\ASUS\Desktop\HC3原始数据\HC3标准化输出\open_qa_标准化.jsonl",
}

OUTPUT_JSONL = r"C:\Users\ASUS\Desktop\HC3原始数据\08_outputs\hc3_merged_standard.jsonl"
STATS_JSON   = r"C:\Users\ASUS\Desktop\HC3原始数据\04_reports\hc3_merge_stats.json"
# ============================

os.makedirs(os.path.dirname(OUTPUT_JSONL), exist_ok=True)
os.makedirs(os.path.dirname(STATS_JSON), exist_ok=True)

stats = {}
total = 0

with open(OUTPUT_JSONL, "w", encoding="utf-8") as out:
    for domain, filepath in INPUT_FILES.items():
        with open(filepath, "r", encoding="utf-8") as f:
            lines = [l for l in f if l.strip()]
        for line in lines:
            out.write(line if line.endswith("\n") else line + "\n")
        stats[domain] = len(lines)
        total += len(lines)
        print(f"[{domain}]  写入 {len(lines):,} 条")

# 验证行数
with open(OUTPUT_JSONL, "r", encoding="utf-8") as f:
    actual = sum(1 for l in f if l.strip())

stats["total_expected"] = total
stats["total_actual"]   = actual
stats["verify_pass"]    = (actual == total)

with open(STATS_JSON, "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

print("=" * 50)
print(f"✅ 合并完成：{OUTPUT_JSONL}")
print(f"实际行数：{actual:,} 条")
if actual == total:
    print("✅ 行数验证通过，合并文件完整")
else:
    print(f"⚠️ 行数不一致！预期 {total}，实际 {actual}")

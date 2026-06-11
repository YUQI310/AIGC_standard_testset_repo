# -*- coding: utf-8 -*-
import json, random, csv, os

INPUT_FILES = {
    "finance":  r"C:\Users\ASUS\Desktop\HC3原始数据\HC3标准化输出\finance_标准化.jsonl",
    "medicine": r"C:\Users\ASUS\Desktop\HC3原始数据\HC3标准化输出\medicine_标准化.jsonl",
    "open_qa":  r"C:\Users\ASUS\Desktop\HC3原始数据\HC3标准化输出\open_qa_标准化.jsonl",
}

OUTPUT_CSV = r"C:\Users\ASUS\Desktop\HC3原始数据\examples\sampling_review_records.csv"
SAMPLE_RATE = 0.05
MIN_SAMPLE = 30
MAX_SAMPLE = 400
RANDOM_SEED = 42

random.seed(RANDOM_SEED)
os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

rows = []
for domain, filepath in INPUT_FILES.items():
    with open(filepath, "r", encoding="utf-8") as f:
        records = [json.loads(l) for l in f if l.strip()]
    total = len(records)
    n = min(MAX_SAMPLE, max(MIN_SAMPLE, int(total * SAMPLE_RATE)))
    sampled = random.sample(records, n)
    print(f"[{domain}]  总量 {total:,} 条 → 抽取 {n} 条 ({n/total*100:.1f}%)")
    for r in sampled:
        rows.append({
            "domain":        domain,
            "sample_id":     r.get("sample_id", ""),
            "question":      str(r.get("question", ""))[:200],
            "human_answer":  str(r.get("human_answers", [""])[0])[:200],
            "chatgpt_answer":str(r.get("chatgpt_answers", [""])[0])[:200],
            "standard_label":r.get("standard_label", ""),
            "review_result": "",
            "notes":         "",
        })

with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("=" * 50)
print(f"✅ 抽样复核清单已生成：{OUTPUT_CSV}")

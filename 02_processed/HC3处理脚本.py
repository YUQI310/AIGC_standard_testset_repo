import json
import uuid
import os

# ========== 配置 ==========
文件夹路径 = r"C:\Users\ASUS\Desktop\HC3原始数据"
输出路径 = r"C:\Users\ASUS\Desktop\HC3标准化输出"

文件列表 = [
    ("finance",  文件夹路径 + r"\finance.jsonl"),
    ("medicine", 文件夹路径 + r"\medicine.jsonl"),
    ("open_qa",  文件夹路径 + r"\open_qa.jsonl"),
]

# ========== 创建输出文件夹 ==========
os.makedirs(输出路径, exist_ok=True)

# ========== 处理每个数据集 ==========
全部统计 = []

for 数据集名称, 路径 in 文件列表:
    print(f"\n{'='*40}")
    print(f"正在处理：{数据集名称}")
    print(f"{'='*40}")

    输出文件 = os.path.join(输出路径, f"{数据集名称}_标准化.jsonl")

    总数 = 0
    保留数 = 0
    跳过数 = 0
    跳过原因统计 = {}

    with open(路径, "r", encoding="utf-8") as f_in, \
         open(输出文件, "w", encoding="utf-8") as f_out:

        for 行 in f_in:
            行 = 行.strip()
            if not 行:
                continue

            总数 += 1

            try:
                原始 = json.loads(行)
            except json.JSONDecodeError:
                跳过数 += 1
                跳过原因统计["JSON解析失败"] = 跳过原因统计.get("JSON解析失败", 0) + 1
                continue

            # ===== 字段提取 =====
            问题 = 原始.get("question", "").strip()
            人类回答列表 = 原始.get("human_answers", [])
            AI回答列表  = 原始.get("chatgpt_answers", [])

            # ===== 过滤：空问题 =====
            if not 问题:
                跳过数 += 1
                跳过原因统计["问题为空"] = 跳过原因统计.get("问题为空", 0) + 1
                continue

            # ===== 展开：每条human_answer生成一条记录(label=human) =====
            for 回答 in 人类回答列表:
                回答 = 回答.strip() if isinstance(回答, str) else ""
                if not 回答:
                    跳过数 += 1
                    跳过原因统计["回答为空"] = 跳过原因统计.get("回答为空", 0) + 1
                    continue

                记录 = {
                    "sample_id":      str(uuid.uuid4()),
                    "dataset_name":   f"HC3_{数据集名称}",
                    "modality":       "text",
                    "question":       问题,
                    "answer":         回答,
                    "raw_label":      "human",
                    "standard_label": "human",
                    "aigc_label":     "human",
                    "risk_type":      "none",
                    "license_status": "allowed",
                    "record_status":  "kept",
                    "source_dataset": 数据集名称,
                    "notes":          ""
                }
                f_out.write(json.dumps(记录, ensure_ascii=False) + "\n")
                保留数 += 1

            # ===== 展开：每条chatgpt_answer生成一条记录(label=ai_generated) =====
            for 回答 in AI回答列表:
                回答 = 回答.strip() if isinstance(回答, str) else ""
                if not 回答:
                    跳过数 += 1
                    跳过原因统计["回答为空"] = 跳过原因统计.get("回答为空", 0) + 1
                    continue

                记录 = {
                    "sample_id":      str(uuid.uuid4()),
                    "dataset_name":   f"HC3_{数据集名称}",
                    "modality":       "text",
                    "question":       问题,
                    "answer":         回答,
                    "raw_label":      "chatgpt",
                    "standard_label": "ai_generated",
                    "aigc_label":     "ai_generated",
                    "risk_type":      "none",
                    "license_status": "allowed",
                    "record_status":  "kept",
                    "source_dataset": 数据集名称,
                    "notes":          ""
                }
                f_out.write(json.dumps(记录, ensure_ascii=False) + "\n")
                保留数 += 1

    # ===== 统计输出 =====
    print(f"原始条目数：{总数}")
    print(f"输出样本数：{保留数}（每条问题展开为多条answer记录）")
    print(f"跳过数：{跳过数}")
    if 跳过原因统计:
        print(f"跳过原因：{跳过原因统计}")
    print(f"输出文件：{输出文件}")

    全部统计.append({
        "数据集": 数据集名称,
        "原始条目": 总数,
        "输出样本": 保留数,
        "跳过": 跳过数
    })

# ========== 汇总 ==========
print(f"\n{'='*40}")
print("全部处理完成，汇总如下：")
print(f"{'='*40}")
for s in 全部统计:
    print(f"{s['数据集']:12} | 原始条目:{s['原始条目']:6} | 输出样本:{s['输出样本']:6} | 跳过:{s['跳过']}")

input("\n按回车键关闭...")

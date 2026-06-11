import json

文件夹路径 = r"C:\Users\ASUS\Desktop\HC3原始数据"

文件列表 = [
    ("finance",   文件夹路径 + r"\finance.jsonl",  "jsonl"),
    ("medicine",  文件夹路径 + r"\medicine.jsonl", "jsonl"),
    ("open_qa",   文件夹路径 + r"\open_qa.jsonl",  "jsonl"),
]

for 名称, 路径, 格式 in 文件列表:
    print(f"\n{'='*40}")
    print(f"数据集：{名称}")
    print(f"{'='*40}")
    
    try:
        with open(路径, "r", encoding="utf-8") as f:
            if 格式 == "jsonl":
                第一条 = json.loads(f.readline().strip())
            else:
                数据 = json.load(f)
                第一条 = 数据[0] if isinstance(数据, list) else 数据
        
        print(f"字段名列表：{list(第一条.keys())}")
        print(f"\n第一条完整内容：")
        print(json.dumps(第一条, ensure_ascii=False, indent=2))
    
    except Exception as e:
        print(f"读取失败：{e}")

input("\n按回车键关闭...")

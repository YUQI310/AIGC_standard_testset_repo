import pandas as pd
import random

df = pd.read_csv('sampling_review_records.csv')
print(f"读取成功，共 {len(df)} 条记录")
print(f"列名：{list(df.columns)}")

results = []
for _, row in df.iterrows():
    label = str(row.get('standard_label', '')).strip()
    human_ans = str(row.get('human_answer', '')).strip()
    chatgpt_ans = str(row.get('chatgpt_answer', '')).strip()

    if label not in ['human', 'ai_generated']:
        results.append('错误')
    elif label == 'human' and human_ans:
        results.append('正确')
    elif label == 'ai_generated' and chatgpt_ans:
        results.append('正确')
    else:
        results.append('错误')

df['review_result'] = results

correct = results.count('正确')
total = len(results)
accuracy = correct / total * 100

print(f"\n========== 预检结果 ==========")
print(f"总条数：{total}")
print(f"正确：{correct}")
print(f"错误：{total - correct}")
print(f"脚本准确率：{accuracy:.1f}%")

df.to_csv('sampling_review_checked.csv', index=False, encoding='utf-8-sig')
print(f"\n结果已保存至：sampling_review_checked.csv")

print(f"\n========== 报告填写数字 ==========")
print(f"抽样总数：{total}")
print(f"正确条数：{correct}")
print(f"准确率：{accuracy:.1f}%")

"""
DF-TIMIT 元数据生成脚本
输出：03_metadata/dftimit_metadata.jsonl
      02_processed/pending_review/video/ 下生成同名占位记录（不移动原文件）
运行方式：在项目根目录执行
    python 06_scripts/build_dftimit_metadata.py
"""

import os
import json
import hashlib
import datetime

# ─────────────────────────────────────────────
# 配置区：根据实际情况修改这里
# ─────────────────────────────────────────────
PROJECT_ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_BASE        = os.path.join(PROJECT_ROOT, "01_raw_data", "DF-TIMIT")
METADATA_OUT    = os.path.join(PROJECT_ROOT, "03_metadata", "dftimit_metadata.jsonl")
PENDING_OUT     = os.path.join(PROJECT_ROOT, "02_processed", "pending_review", "video")
LOG_OUT         = os.path.join(PROJECT_ROOT, "05_logs", "build_dftimit_metadata.log")

# 扫描的文件后缀（小写）
TARGET_EXTS = {".avi", ".mov", ".mp4", ".mkv"}

# ─────────────────────────────────────────────
# 工具函数
# ─────────────────────────────────────────────

def make_data_id(rel_path: str) -> str:
    """用相对路径生成唯一 ID：DFTIMIT_xxxxxxxx"""
    h = hashlib.md5(rel_path.encode()).hexdigest()[:8].upper()
    return f"DFTIMIT_{h}"


def parse_speaker(parts: list) -> str:
    """
    从路径片段中识别说话人 ID。
    higher_quality/fadg0/xxx.avi → fadg0
    lower_quality/fadg0/xxx.avi → fadg0
    根目录文件 fadg0-original.mov → fadg0（从文件名前缀）
    """
    # parts 示例: ['higher_quality', 'fadg0', 'sa2-video-fram1.avi']
    quality_dirs = {"higher_quality", "lower_quality"}
    for i, p in enumerate(parts):
        if p in quality_dirs and i + 1 < len(parts):
            return parts[i + 1]
    # 根目录文件：从文件名 fadg0-xxx 中提取
    filename = parts[-1]
    prefix = filename.split("-")[0]
    if len(prefix) >= 4:          # fadg0 长度为5，至少4位才认为是说话人ID
        return prefix
    return "unknown"


def parse_quality(parts: list) -> str:
    if "higher_quality" in parts:
        return "higher"
    if "lower_quality" in parts:
        return "lower"
    return "unknown"


def parse_manipulation_type(filename: str) -> str:
    """根据文件名关键词判断操作类型"""
    fn = filename.lower()
    if "original" in fn:
        return "none"          # 原始真实视频
    if "roi" in fn or "fram" in fn or "video" in fn:
        return "face_reenactment"
    return "deepfake"


def parse_standard_label(filename: str) -> str:
    """original 文件标记为 real，其余为 fake"""
    if "original" in filename.lower():
        return "real"
    return "fake"


def get_file_size_mb(filepath: str) -> float:
    try:
        return round(os.path.getsize(filepath) / (1024 * 1024), 3)
    except Exception:
        return -1


def log(msg: str, log_lines: list):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    log_lines.append(line)


# ─────────────────────────────────────────────
# 主逻辑
# ─────────────────────────────────────────────

def scan_files(base_dir: str) -> list:
    """递归扫描 base_dir 下所有目标格式文件，返回绝对路径列表"""
    found = []
    for root, dirs, files in os.walk(base_dir):
        # 跳过隐藏目录
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fname in files:
            if os.path.splitext(fname)[1].lower() in TARGET_EXTS:
                found.append(os.path.join(root, fname))
    return sorted(found)


def build_record(filepath: str) -> dict:
    rel_path   = os.path.relpath(filepath, PROJECT_ROOT)   # 相对项目根的路径
    rel_parts  = rel_path.replace("\\", "/").split("/")    # 兼容 Windows
    # rel_parts 示例: ['01_raw_data','DF-TIMIT','higher_quality','fadg0','sa2-video-fram1.avi']
    # 取 DF-TIMIT 之后的部分用于解析
    try:
        dftimit_idx = rel_parts.index("DF-TIMIT")
        inner_parts = rel_parts[dftimit_idx + 1:]          # ['higher_quality','fadg0','xxx.avi']
    except ValueError:
        inner_parts = rel_parts

    filename   = os.path.basename(filepath)
    speaker_id = parse_speaker(inner_parts)
    quality    = parse_quality(inner_parts)
    std_label  = parse_standard_label(filename)
    manip_type = parse_manipulation_type(filename)
    data_id    = make_data_id(rel_path.replace("\\", "/"))

    # pending_review 里的"记录路径"（不移动文件，仅记录将来应放的位置）
    normalized_name = data_id + os.path.splitext(filename)[1].lower()
    normalized_path = os.path.join("02_processed", "pending_review", "video", normalized_name)

    record = {
        "data_id"              : data_id,
        "content_type"         : "video",
        "source_dataset"       : "DF-TIMIT",
        "source_sample_id"     : os.path.splitext(filename)[0],
        "raw_path"             : rel_path.replace("\\", "/"),
        "normalized_path"      : normalized_path.replace("\\", "/"),
        "original_format"      : os.path.splitext(filename)[1].lower().lstrip("."),
        "file_size_mb"         : get_file_size_mb(filepath),
        "speaker_id"           : speaker_id,
        "quality"              : quality,
        "standard_label"       : std_label,
        "aigc_label"           : "manipulated" if std_label == "fake" else "authentic",
        "risk_type"            : "deepfake"    if std_label == "fake" else "none",
        "manipulation_type"    : manip_type,
        "license_status"       : "restricted",
        "record_status"        : "pending_review",
        "label_mapping_rule"   : "filename_keyword: 'original'→real; others→fake",
        "label_mapping_confidence": "high",
        "notes"                : "",
        "created_at"           : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return record


def main():
    log_lines = []
    log(f"=== DF-TIMIT 元数据生成开始 ===", log_lines)
    log(f"扫描目录：{RAW_BASE}", log_lines)

    # 确保输出目录存在
    os.makedirs(os.path.dirname(METADATA_OUT), exist_ok=True)
    os.makedirs(PENDING_OUT, exist_ok=True)
    os.makedirs(os.path.dirname(LOG_OUT), exist_ok=True)

    # 扫描文件
    files = scan_files(RAW_BASE)
    log(f"共发现文件：{len(files)} 个", log_lines)

    if not files:
        log("未找到任何视频文件，请检查 RAW_BASE 路径是否正确", log_lines)
        return

    # 生成元数据
    records  = []
    ok_count = 0
    err_count = 0

    for fp in files:
        try:
            rec = build_record(fp)
            records.append(rec)
            ok_count += 1
            log(f"  [OK] {rec['data_id']} | {rec['raw_path']}", log_lines)
        except Exception as e:
            err_count += 1
            log(f"  [ERR] {fp} → {e}", log_lines)

    # 写入 JSONL
    with open(METADATA_OUT, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # 写日志
    log(f"=== 完成：成功 {ok_count} 条，失败 {err_count} 条 ===", log_lines)
    log(f"元数据输出：{METADATA_OUT}", log_lines)

    with open(LOG_OUT, "w", encoding="utf-8") as lf:
        lf.write("\n".join(log_lines))


if __name__ == "__main__":
    main()



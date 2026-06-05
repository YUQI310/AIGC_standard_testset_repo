from datetime import datetime
import hashlib


def make_data_id(dataset_name, index):
    return f"{dataset_name}_{index:06d}"


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def now_iso():
    return datetime.utcnow().isoformat() + "Z"

def route_by_license(commercial_use, restriction_cleared=False):
    """
    根据许可状态决定样本输出目录类型。
    """
    if commercial_use == "allowed":
        return "candidate_pool"
    if commercial_use == "restricted":
        return "candidate_pool" if restriction_cleared else "pending_review"
    if commercial_use in ["forbidden", "unknown"]:
        return "isolation/license"
    return "pending_review"

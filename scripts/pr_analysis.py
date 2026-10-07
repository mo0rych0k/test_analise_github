"""PR analysis rules, kept independent from GitHub transport for Rebbit reuse."""

from __future__ import annotations

from datetime import datetime
import re

FLAGGED_COMMENT = re.compile(r"\b(block(?:er|ing)?|bug|fix|must|todo|nit)\b", re.I)


def hours_between(start: str, end: str | None) -> float | None:
    if not end:
        return None
    parse = lambda value: datetime.fromisoformat(value.replace("Z", "+00:00"))
    return round((parse(end) - parse(start)).total_seconds() / 3600, 2)


def summarize_pr(pr: dict, discussion: list[dict], review_comments: list[dict], density_limit: float) -> dict:
    comments = discussion + review_comments
    flagged = [comment for comment in comments if FLAGGED_COMMENT.search(comment.get("body", ""))]
    changed_files = pr.get("changed_files", 0)
    density = round(len(comments) / max(changed_files, 1), 2)
    return {
        "number": pr["number"],
        "title": pr["title"],
        "url": pr["html_url"],
        "state": pr["state"],
        "created_at": pr["created_at"],
        "closed_at": pr.get("closed_at"),
        "lifecycle_hours": hours_between(pr["created_at"], pr.get("closed_at")),
        "code_changes": {key: pr.get(key, 0) for key in ("changed_files", "additions", "deletions")},
        "comments": {
            "discussion": discussion,
            "review": review_comments,
            "total": len(comments),
            "density_per_changed_file": density,
            "flagged": flagged,
        },
        "rebbit_signal": {
            "has_code_changes": bool(pr.get("additions", 0) or pr.get("deletions", 0)),
            "human_comment_count": len(comments),
        },
        "needs_attention": density >= density_limit or bool(flagged),
    }

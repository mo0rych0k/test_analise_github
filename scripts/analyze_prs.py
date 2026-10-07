#!/usr/bin/env python3
"""Fetch GitHub pull requests and write a JSON audit report."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from github_api import GitHubClient
from pr_analysis import summarize_pr


def load_env(path: Path = Path(".env")) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", help="OWNER/REPO, for example mo0rych0k/test_analise_github")
    parser.add_argument("--state", choices=("open", "closed", "all"), default="all")
    parser.add_argument("--limit", type=int, default=50, help="maximum PRs to analyze")
    parser.add_argument("--density-limit", type=float, default=2.0)
    parser.add_argument("--output", default="pr-analysis.json")
    args = parser.parse_args()

    owner, repo = args.repository.split("/", 1)
    load_env()
    client = GitHubClient(os.getenv("GITHUB_TOKEN", ""))
    pulls = client.paged_get(f"/repos/{owner}/{repo}/pulls", state=args.state)[: args.limit]
    report = []
    for pull in pulls:
        number = pull["number"]
        detail = client.get(f"/repos/{owner}/{repo}/pulls/{number}")
        discussion = client.paged_get(f"/repos/{owner}/{repo}/issues/{number}/comments")
        review_comments = client.paged_get(f"/repos/{owner}/{repo}/pulls/{number}/comments")
        report.append(summarize_pr(detail, discussion, review_comments, args.density_limit))

    Path(args.output).write_text(json.dumps(report, indent=2) + "\n")
    print(f"Analyzed {len(report)} PRs -> {args.output}")


if __name__ == "__main__":
    main()

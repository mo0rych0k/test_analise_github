"""Small authenticated GitHub REST client for read-only PR analysis."""

from __future__ import annotations

import json
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class GitHubClient:
    def __init__(self, token: str) -> None:
        if not token:
            raise ValueError("GITHUB_TOKEN is required")
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get(self, path: str, **params: str | int) -> list | dict:
        query = urlencode(params)
        url = f"https://api.github.com{path}{'?' + query if query else ''}"
        try:
            with urlopen(Request(url, headers=self.headers), timeout=30) as response:
                return json.load(response)
        except HTTPError as error:
            detail = error.read().decode("utf-8", "replace")
            raise RuntimeError(f"GitHub API {error.code}: {detail}") from error

    def paged_get(self, path: str, **params: str | int) -> list[dict]:
        results: list[dict] = []
        page = 1
        while True:
            batch = self.get(path, **params, per_page=100, page=page)
            results.extend(batch)
            if len(batch) < 100:
                return results
            page += 1

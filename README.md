# GitHub PR analysis proof of concept

This standard-library Python tool retrieves pull requests, general discussion comments, and inline review comments. It writes a JSON report with lifecycle time, comment density, keyword flags, and a small `rebbit_signal` object for future checker integration.

## Setup

Add a fine-grained, read-only PAT to `.env`:

```env
GITHUB_TOKEN=github_pat_...
```

The token needs **Pull requests: Read-only**. Add **Issues: Read-only** to collect PR discussion comments. Scope the token to the target repository.

## Run

```sh
python3 scripts/analyze_prs.py mo0rych0k/test_analise_github
python3 scripts/analyze_prs.py OWNER/REPO --state closed --limit 100 --output report.json
python3 -m unittest discover -s tests
```

PRs are flagged when comment density reaches `2.0` comments per changed file or a comment includes `block`, `bug`, `fix`, `must`, `todo`, or `nit`. Adjust the density rule with `--density-limit`.

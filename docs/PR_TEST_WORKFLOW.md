# Rebbit PR Test Workflow

## Purpose

These fixtures create predictable pull-request data for validating the GitHub export scripts and the future Rebbit checker. They separate code changes, discussion comments, inline review comments, and lifecycle outcomes so the audit can prove what it detects.

## What will be created

Each scenario is a small branch and pull request against the repository default branch. The changes only add files beneath `fixtures/rebbit_pr_tests/`; production code is untouched.

- `positive-small-change`: a simple code change with a normal review.
- `negative-dense-review`: a small code change intended to receive several inline review comments.
- `negative-closed-unmerged`: a fixture PR closed without merging.

The PR description will state the expected result. Review comments must be added through GitHub after opening the PR, because API analysis needs real GitHub comment records.

## Data flow

1. Open and review each test PR.
2. Run `scripts/export_prs.py` after it is added; it stores raw API responses under `data/raw/`.
3. Run `scripts/analyze_exports.py`; it reads only exported files and writes summaries under `data/derived/`.
4. Compare the summaries with each PR's expected result. Add Rebbit's result later as `rebbit_signal` without changing raw export files.

## Safety

Use the repository-scoped, read-only PAT only for export. Creating branches and pull requests uses the authenticated GitHub account, not the PAT stored in `.env`. Do not include tokens in commits, PR text, or fixture files.

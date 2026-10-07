import unittest

from scripts.pr_analysis import summarize_pr


class PRAnalysisTest(unittest.TestCase):
    def test_flags_dense_review_and_calculates_lifecycle(self):
        summary = summarize_pr(
            {"number": 1, "title": "Test", "html_url": "url", "state": "closed", "created_at": "2026-01-01T00:00:00Z", "closed_at": "2026-01-02T12:00:00Z", "changed_files": 1, "additions": 2, "deletions": 0},
            [{"body": "Please fix this bug"}], [], 2.0,
        )
        self.assertEqual(summary["lifecycle_hours"], 36.0)
        self.assertTrue(summary["needs_attention"])


if __name__ == "__main__":
    unittest.main()

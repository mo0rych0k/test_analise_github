import unittest

from fixtures.rebbit_pr_tests.review_target import normalize_name


class ReviewTargetTest(unittest.TestCase):
    def test_normalize_name(self):
        self.assertEqual(normalize_name("  rebbit   test  "), "Rebbit Test")


if __name__ == "__main__":
    unittest.main()

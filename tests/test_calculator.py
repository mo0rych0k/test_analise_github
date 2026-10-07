import unittest

from fixtures.rebbit_pr_tests.calculator import add


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()

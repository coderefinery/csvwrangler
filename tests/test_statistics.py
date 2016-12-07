import unittest

from csvwrangler.statistics import mean, median


class TestMathFunctions(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(mean([1, 3]), 2)

    def test_median(self):
        self.assertEqual(median([1, 2, 3]), 2)

if __name__ == "__main__":
    unittest.main()

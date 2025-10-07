import unittest
from main import sort

class TestPackageSorting(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(90, 100, 100, 10), "STANDARD")

    def test_special_bulky(self):
        self.assertEqual(sort(200, 50, 50, 10), "SPECIAL")

    def test_special_heavy(self):
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

if __name__ == "__main__":
    unittest.main()

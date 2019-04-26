import unittest
import chapter6

class TestChapter6(unittest.TestCase):

    def test_is_leap(self):
        self.assertEqual(chapter6.is_leap(1944), True)
        self.assertEqual(chapter6.is_leap(2011), False)
        self.assertEqual(chapter6.is_leap(1986), False)
        self.assertEqual(chapter6.is_leap(1956), True)
        self.assertEqual(chapter6.is_leap(1957), False)
        self.assertEqual(chapter6.is_leap(1800), False)
        self.assertEqual(chapter6.is_leap(1900), False)
        self.assertEqual(chapter6.is_leap(1600), True)
        self.assertEqual(chapter6.is_leap(2056), True)

if __name__ == '__main__':
    unittest.main()

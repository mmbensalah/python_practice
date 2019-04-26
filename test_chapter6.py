import unittest
import chapter6

class TestChapter6(unittest.TestCase):

    def test_is_leap(self):
        self.assertEqual(chapter6.is_leap(1944), True)

if __name__ == '__main__':
    unittest.main()

import unittest
import chapter8


class TestChapter8(unittest.TestCase):
    def test_course_grader(self):
        # self.assertEqual(chapter8.course_grader([100,75,5]), "fail")
        # self.assertEqual(chapter8.course_grader([100,70,85]), "pass")
        # self.assertEqual(chapter8.course_grader([80,60,60]), "fail")
        self.assertEqual(chapter8.course_grader([80,80,90,30,80]), "fail")
        # self.assertEqual(chapter8.course_grader([70,70,70,70,70]), "pass")
        # self.assertEqual(chapter8.course_grader([60,80,80,70,70]), "pass")

if __name__ == '__main__':
    unittest.main()

import unittest
from solution import solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(907), 790)
        self.assertEqual(solution(531), 513)
        self.assertEqual(solution(135), -1)
        self.assertEqual(solution(2071), 2017)
        self.assertEqual(solution(414), 144)
        self.assertEqual(solution(123456798), 123456789)
        self.assertEqual(solution(123456789), -1)
        self.assertEqual(solution(1234567908), 1234567890)
        self.assertEqual(solution(1027), -1)
        self.assertEqual(solution(1207), 1072)

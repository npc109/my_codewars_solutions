import unittest
from solution import solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(2), 2)
        self.assertEqual(solution(3), 3)
        self.assertEqual(solution(4), 4)
        self.assertEqual(solution(5), 5)
        self.assertEqual(solution(6), 6)
        self.assertEqual(solution(7), 8)
        self.assertEqual(solution(8), 9)
        self.assertEqual(solution(9), 10)
        self.assertEqual(solution(10), 12)
        self.assertEqual(solution(11), 15)
        self.assertEqual(solution(12), 16)
        self.assertEqual(solution(13), 18)
        self.assertEqual(solution(14), 20)
        self.assertEqual(solution(15), 24)
        self.assertEqual(solution(16), 25)
        self.assertEqual(solution(17), 27)
        self.assertEqual(solution(18), 30)
        self.assertEqual(solution(5000), 50837316566580)

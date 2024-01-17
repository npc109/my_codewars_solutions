import unittest
from solution import solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([0]), 0)
        self.assertEqual(solution([2, 3, 1, 1, 4]), 2)
        self.assertEqual(solution([2, 3, 0, 1, 4]), 2)

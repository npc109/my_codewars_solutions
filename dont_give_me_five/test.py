import unittest
from dont_give_me_five.solution import solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(-17, 9), 24)
        self.assertEqual(solution(1, 9), 8)
        self.assertEqual(solution(4, 17), 12)
        self.assertEqual(solution(-17, -4), 12)
        self.assertEqual(solution(984, 4304), 2449)
        self.assertEqual(solution(2313, 2317), 4)
        self.assertEqual(solution(40076, 2151514229639903569), 326131553237897713)

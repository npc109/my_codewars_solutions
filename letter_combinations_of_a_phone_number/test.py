import unittest
from solution import solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(""), [])
        self.assertEqual(solution("2"), ['a','b','c'])
        self.assertEqual(solution("23"), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])

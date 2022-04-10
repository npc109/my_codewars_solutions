import unittest
from Probabilities_for_Sums_in_Rolling_Cubic_Dice.solution import rolldice_sum_prob


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        self.assertAlmostEqual(rolldice_sum_prob(11, 2), 0.0555555555)
        self.assertAlmostEqual(rolldice_sum_prob(8, 2), 0.13888888889)
        self.assertAlmostEqual(rolldice_sum_prob(8, 3), 0.0972222222222)

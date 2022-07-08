import unittest
from probabilities_for_sums_in_rolling_cubic_dice.solution import rolldice_sum_prob


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        self.assertAlmostEqual(rolldice_sum_prob(11, 2), 0.0555555555)
        self.assertAlmostEqual(rolldice_sum_prob(8, 2), 0.13888888889)
        self.assertAlmostEqual(rolldice_sum_prob(8, 3), 0.0972222222222)

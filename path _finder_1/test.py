import unittest
from path_finder_1.solution import path_finder


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        self.assertAlmostEqual(path_finder("\n".join([
            ".W...",
            ".W...",
            ".W.W.",
            "...W.",
            "...W."])), True)
        self.assertAlmostEqual(path_finder("\n".join([
            ".W...",
            ".W...",
            ".W.W.",
            "...WW",
            "...W."])), False)

import unittest
from three_sum.solution import Solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        solution = sol.threeSum
        self.assertEqual(solution([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(solution([3, 0, -2, -1, 1, 2]), [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
                         )

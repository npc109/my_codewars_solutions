import unittest

from rotate_image.solution import Solution


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        s.rotate(matrix)
        self.assertListEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        s.rotate(matrix)
        self.assertListEqual(matrix, [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])
        matrix = [[1]]
        s.rotate(matrix)
        self.assertListEqual(matrix, [[1]])

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def r(matrix, rem=0):
            ll = len(matrix[0]) - 1 - 2 * rem
            l = len(matrix) - 1 - rem
            for i in range(ll):
                x = i + rem
                init = matrix[rem][x]
                cur = matrix[x][l]
                matrix[x][l] = init
                init = cur
                cur = matrix[l][l - i]
                matrix[l][l - i] = init
                init = cur
                cur = matrix[l - i][rem]
                matrix[l - i][rem] = init
                init = cur
                matrix[rem][x] = init

        r(matrix)
        l = len(matrix)
        rem = 0
        while l > 3:
            l -= 1
            rem += 1
            r(matrix, rem)
        return matrix

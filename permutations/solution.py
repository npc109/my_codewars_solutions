from copy import copy
from typing import List


def close(val: str):
    n = 0
    for i in val:
        if i == '(':
            n += 1
        else:
            n -= 1
    return val + ')' * n


def check(val):
    n = 0
    print(val)
    for i in val:
        if i == "(":
            n -= 1
        else:
            n += 1
    return n <= 0


def validate(val: str):
    n = 0
    for i in val:
        if i == ')':
            n += 1
        else:
            n -= 1
    return n == 0


def generate(n: int, ):
    def dfs(l, r, s):
        if len(s) == n * 2:
            res.append(s)
            return
        if (l < n):
            dfs(l + 1, r, s + '(')
        if (r < l):
            dfs(l, r + 1, s + ')')

    res = []
    dfs(0, 0, '')
    return res


def findTheLongestBalancedSubstring(s):
    res = 0
    i = 0
    while i < len(s):
        cur = 0
        if s[i] == '0':
            w = 0
            while w + i < len(s) and s[w + i] == '0':
                w += 1
            for x in range(w):
                if i + w + x < len(s) and s[i + w + x] == '1':
                    cur += 2
                else:
                    break
            i = i + w + x
            res = max(res, cur)
        else:
            i += 1
    return res


def miceAndCheese(reward1: List[int], reward2: List[int], k: int) -> int:
    result = 0
    if not (reward1):
        return result
    if k == len(reward1):
        return sum(reward1)
    res = {1: [], 2: []}
    for i in range(len(reward1)):
        res[1].append({'diff': reward1[i] - reward2[i], 'val': reward1[i]})
        res[2].append({'diff': reward2[i] - reward1[i], 'val': reward2[i]})
    res[1].sort(key=lambda x: (x['diff'], x['val']))
    res[2].sort(key=lambda x: (x['diff'], x['val'] * -1))
    res[1].reverse()
    res[2].reverse()
    print(res[1])
    print(res[2])
    used = 0
    z = 0
    while z < len(reward1) and (k > 0):
        print(res[1][z]['val'])
        result += res[1][z]['val']
        k -= 1
        used += 1
        z += 1
    print(result, "!!!")
    for x in range(len(reward1) - used):
        print(res[2][x]['val'])
        result += res[2][x]['val']
    return result


# print(miceAndCheese([3,3,4,1],
#                     [4,4,4,2],2))

def removeDuplicates(nums: List[int]) -> int:
    size = len(nums)
    index = 1
    for i in range(1, size):
        if nums[i - 1] != nums[i]:
            nums[index] = nums[i]
            index += 1
    return index


a = [1,1,2]
print(removeDuplicates(a), a)

# if len(res[1]) > k:
#     for i in res[1]:
#         result += i.val
#     for i in res[2]:
#         result += i.val
# else:
#     res[1].sort(key=lambda x: x['diff'])

# print(findTheLongestBalancedSubstring("0000"))
# x = generate(3)
# y = ["((((()))))", "(((()())))", "(((())()))", "(((()))())", "(((())))()", "((()(())))", "((()()()))", "((()())())",
#      "((()()))()", "((())(()))", "((())()())", "((())())()", "((()))(())", "((()))()()", "(()((())))", "(()(()()))",
#      "(()(())())", "(()(()))()", "(()()(()))", "(()()()())", "(()()())()", "(()())(())", "(()())()()", "(())((()))",
#      "(())(()())", "(())(())()", "(())()(())", "(())()()()", "()(((())))", "()((()()))", "()((())())", "()((()))()",
#      "()(()(()))", "()(()()())", "()(()())()", "()(())(())", "()(())()()", "()()((()))", "()()(()())", "()()(())()",
#      "()()()(())", "()()()()()"]
# print(x)
# print(y)
# print([i for i in y if i not in x])

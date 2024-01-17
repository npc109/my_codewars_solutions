from typing import List


def solution(nums: List[int], pos=0, j=0, b=False):
    dest = len(nums)
    val = nums[pos]
    if pos >= dest - 1:
        return j
    else:
        max_v = 0
        new_pos = 0
        for i in range(pos + 1, pos + 1 + val):
            if i >= dest - 1:
                new_pos = i
                break
            if nums[i] + i >= max_v:
                max_v = nums[i] + i
                new_pos = i
        return solution(nums, pos=new_pos, j=j + 1, b=True)

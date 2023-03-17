from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        n = len(nums)
        unique = set()
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                print(nums[i], nums[j], nums[k])
                if s == 0:
                    if (nums[i], nums[j], nums[k]) not in unique:
                        unique.add((nums[i], nums[j], nums[k]))
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return res

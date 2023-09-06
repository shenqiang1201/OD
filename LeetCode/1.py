# 两数之和
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1 = []
        for l_index in range(len(nums)):
            for r_index in range(l_index + 1, len(nums)):
                if nums[l_index] + nums[r_index] == target:
                    list1.append(l_index)
                    list1.append(r_index)
                    return list1

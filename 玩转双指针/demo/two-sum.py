# -*- coding: UTF-8 -*-
"""
https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/submissions/
"""

from typing import List

class Solution:
    # 左右指针同向遍历, 直到left >= right
    def twoSum(self, numbers: List[int], target: int):
        left,right = 0, len(numbers)-1
        while left < right:
            s = numbers[left] +numbers[right]
            if s == target:
                return [left+1,right+1]
            elif s > target:
                right -= 1
            else:
                left += 1
        return []

    # hash的做法
    def twoSum2(self, numbers: List[int], target: int):
        hash_map = {}
        for i,number in enumerate(numbers):
            if (target-number) in hash_map:
                return [hash_map[target-number],i+1]
            hash_map[number] = i+1
# -*- coding: UTF-8 -*-

"""
https://leetcode-cn.com/problems/sort-colors/
"""

from typing import List

class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: x)
        return

class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i],nums[ptr] = nums[ptr],nums[i] 
                ptr += 1
        
        j = ptr
        for i in range(j,n):
            if nums[i] == 1:
                nums[i],nums[ptr] = nums[ptr],nums[i]
                ptr += 1
        return

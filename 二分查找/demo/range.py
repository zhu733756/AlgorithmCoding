"""
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""

# -*- coding: UTF-8 -*-
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        for index, num in enumerate(nums):
            if num == target:
                if ans[0] == -1:
                    ans = [index,index]
                else:
                    ans[-1] = index
        return ans

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 可以将题意进行拆解：返回最小和最大等于target的索引区间。
        # 注意边界条件
        
        if len(nums) == 0:
            return [-1,-1]

        def get_bound(nums, method="left"):
            l,r =0 , len(nums)-1
            while l <= r:
                mid = (l+r) //2
                if nums[mid] == target:
                    if method == "left":
                        r = mid-1
                    else:
                        l = mid+1
                elif nums[mid] > target:
                    r = mid -1
                else:
                    l = mid + 1
            
            if l < len(nums) and method == "left" and nums[l] == target:
                return l

            if r >= 0 and method == "right" and nums[r] == target:
                return r

            return -1
        
        return [get_bound(nums, "left"), get_bound(nums, "right")]
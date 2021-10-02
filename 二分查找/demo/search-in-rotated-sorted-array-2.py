"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/
"""

# -*- coding: UTF-8 -*-
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 局部有序，可以构建两个有序范围，分别是 [left, mid], 以及[mid, right]
        # 当target落在这两个范围内，必定是可以确定是否存在的这样的target的
        # 先给定一个有序的范围进行二分查找，否则将结果驱使到另一个有序的范围
        # 需要考虑特殊情况[1,0,1,1,1]

        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] == target:
                return True
            # 处理特殊情况，就是左右同时往里缩小一个step
            if nums[mid] == nums[r] == nums[l]:
                l += 1
                r -= 1
            elif nums[mid] >= nums[l]:
                if nums[mid] >= target >= nums[l]:
                    r = mid -1
                else:
                    l = mid +1
            elif nums[mid] <= nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1

        return False


# -*- coding: UTF-8 -*-

"""
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/submissions/
"""

# -*- coding: UTF-8 -*-
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1 
        target = len(nums)-k
        while left <= right:
            # 获取分区索引，便于下一次查询
            pindex = self.partional(nums, left, right)
            if pindex == target:
                return nums[pindex]
            elif pindex < target:
                left = pindex + 1
            else:
                right = pindex -1
        return nums[left]
        
    def partional(self, nums, left, right):
        """
        获取分区的索引
        """
        pindex, pivot = right, nums[right]
        for i in range(right-1, left-1, -1):
            if nums[i] >= pivot:
                pindex = pindex-1
                nums[i],nums[pindex] = nums[pindex],nums[i]
        nums[pindex],nums[right] = nums[right],nums[pindex]
        return pindex

if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4))
    
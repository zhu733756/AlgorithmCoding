# -*- coding: UTF-8 -*-
"""
https://leetcode-cn.com/problems/merge-sorted-array/
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 两个数组分别使用一个指针
        # 从后往前遍历有利于减少nums1的元素拷贝
        # 考虑一个指针遍历完毕后，另外一个还有元素的情况

        left,right = m-1,n-1
        while left >= 0 and right >= 0:
            if nums1[left] >= nums2[right]:
                nums1[left+right+1] = nums1[left]
                left -= 1
            else:
                nums1[left+right+1] = nums2[right]
                right -= 1
        
        if right >= 0:
            nums1[:right+1] = nums2[:right+1]

if __name__ == '__main__':
    Solution().merge([0],0,[1],1)
    
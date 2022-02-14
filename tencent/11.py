# https://leetcode-cn.com/problems/container-with-most-water/

"""
给定一个长度为 n 的整数数组height。有n条垂线，第 i 条线的两个端点是(i, 0)和(i, height[i])。

找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height)-1
        while left < right:
            if height[left] >= height[right]:
                area = max(area, (right-left) * height[right])
                right -= 1
            else:
                area = max(area, (right-left) * height[left])
                left += 1
        return area



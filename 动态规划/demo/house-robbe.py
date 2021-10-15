#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     house-robbe.py
@Time    :     Fri Oct 15 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Fri Oct 15 2021
Modified By:   zhu733756
@Desc    :     打家劫舍，不能偷邻居
@link    :     https://leetcode-cn.com/problems/house-robbe/submissions/
'''

from  typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        i 偷最大值： nums[i]+dp[i-1][0]
        i 不偷最大值： max(dp[i-1][1], dp[i-1][0])
        """
        length = len(nums)
        if length <= 1:
            return sum(nums)

        dp = [[j for j in range(2)] for i in range(length)]
        dp[0][0] = 0 
        dp[0][1] = nums[0]
        for i in range(1,length):
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
            dp[i][1] = dp[i-1][0]+ nums[i]

        return max(dp[length-1])


class Solution2:
    def rob(self, nums: List[int]) -> int:
        """
        前i个房间最大可获得金额数值为dp
        """
        length = len(nums)
        if length <= 1:
            return sum(nums)
 
        dp = [0] * (length+1)
        dp[1] = nums[0]
        for i in range(2,length+1):
           dp[i] = max(dp[i-1], dp[i-2]+ nums[i-1])

        return dp[length]


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        状态压缩
        """
        length = len(nums)
        if length <= 1:
            return sum(nums)
 
        prev, cur = 0, nums[0]
        for i in range(1,length):
           prev, cur = cur, max(prev+nums[i],cur)

        return cur
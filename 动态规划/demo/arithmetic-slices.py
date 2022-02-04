#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     arithmetic-slices.py
@Time    :     Mon Oct 18 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 18 2021
Modified By:   zhu733756
@Desc    :     相邻等差数列
@link    :     https://leetcode-cn.com/problems/arithmetic-slices/submissions/
'''

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        if nums[i]-nums[i-1] == nums[i-1]- nums[i-2]:
            dp[i] = dp[i-1]+1
        """
        length = len(nums)
        if length < 3:
            return 0

        dp = [0] *length
        for i in range(2, length):
            if nums[i]-nums[i-1] == nums[i-1]- nums[i-2]:
                dp[i] = dp[i-1]+1

        return  sum(dp)
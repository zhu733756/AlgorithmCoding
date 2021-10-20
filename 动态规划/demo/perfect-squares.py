#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     perfect-squares.py
@Time    :     Wed Oct 20 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Wed Oct 20 2021
Modified By:   zhu733756
@Desc    :     给定一个数，返回等于该值得平方数的个数
@link    :     https://leetcode-cn.com/problems/perfect-squares/submissions/
'''

class Solution:
    def numSquares(self, n: int) -> int:
        """
        dp[i]表示下标为i的最少平方数个数
        前一个平方数个数与当前平方数差值为1
        """
        if n <= 1:
            return 1
        dp = [float("inf")]* (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            j = 1
            while j *j <= i:
                dp[i] = min(dp[i- j*j]+1, dp[i])
                j += 1
        return dp[n]


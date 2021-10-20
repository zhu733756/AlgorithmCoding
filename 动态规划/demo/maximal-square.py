#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     maximal-square.py
@Time    :     Wed Oct 20 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Wed Oct 20 2021
Modified By:   zhu733756
@Desc    :     矩阵中最大平方面积
@link    :     https://leetcode.com/problems/maximal-square.py/submissions/
'''
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m,n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n) for i in range(n)]]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans = max(ans, dp[i][j])
        return ans
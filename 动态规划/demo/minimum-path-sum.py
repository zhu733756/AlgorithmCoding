#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     minimum-path-sum.py
@Time    :     Mon Oct 18 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 18 2021
Modified By:   zhu733756
@Desc    :     动态规划向右向下走，注意处理边界
@link    :     https://leetcode-cn.com/problems/minimum-path-sum/submissions/
'''

from  typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        状态转移方程：
        dp[i][j] = min(dp[i][j-1], dp[i-1][j]]) + grid[i][j] 
        """

        m,n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,n): 
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j] 

        return dp[-1][-1]
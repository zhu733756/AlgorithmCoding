#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     ones-and-zeroes.py
@Time    :     Mon Oct 18 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 18 2021
Modified By:   zhu733756
@Desc    :     给你一个二进制字符串数组 strs 和两个整数 m 和 n 。请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
@link    :     https://leetcode-cn.com/problems/ones-and-zeroes/
'''

import re
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        0-1背包问题, dp[i][j] 表示i个0和j个1的背包的最大子集长度
        """
        if m <= 0 or n <= 0:
          return 0

        dp = [[0] * (n+1) for _ in range(m+1)]

        for str in strs:
          count0 = sum([1 for e in str if e == "0"])
          count1 = len(str) - count0
          for i in range(m, count0-1, -1):
            for j in range(n, count1-1, -1):
              dp[i][j] = max(dp[i][j], 1 + dp[i-count0][j-count1])

        return dp[m][n]
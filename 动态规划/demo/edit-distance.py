#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     edit-distance.py
@Time    :     Mon Oct 18 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 18 2021
Modified By:   zhu733756
@Desc    :     给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
@link    :     https://leetcode-cn.com/problems/edit-distance/submissions/
'''

from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j] word1 前i个以及word2前j个字符需要编辑的最少次数
        """
        if word1 == word2:
            return 0

        m,n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] =  dp[i-1][j-1]
                else:
                    dp[i][j] =  min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

        return dp[m][n]
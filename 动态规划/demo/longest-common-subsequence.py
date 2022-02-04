#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     longest-common-subsequence.py
@Time    :     Mon Oct 18 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 18 2022
Modified By:   zhu733756
@Desc    :     给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
@link    :     https://leetcode-cn.com/problems/longest-common-subsequence/
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp[i][j] 表示text1中下标为i，text2中下标为j的最长公共子序列长度
        """
        m, n = len(text1), len(text2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else: 
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        return dp[m][n]
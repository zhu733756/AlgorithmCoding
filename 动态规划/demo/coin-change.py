#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     coin-change.py
@Time    :     Mon Oct 18 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 18 2021
Modified By:   zhu733756
@Desc    :     给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
@link    :     https://leetcode-cn.com/problems/coin-change/submissions/
'''

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        完全背包，dp[i]表示接受面值为i时候的最少硬币个数
        """
        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]
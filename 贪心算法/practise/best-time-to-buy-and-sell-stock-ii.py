# -*- coding: UTF-8 -*-
"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只要今天比昨天的股票高，就把差值累加。
        # 昨天买今天卖
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                ans +=  prices[i]- prices[i-1]

        return ans
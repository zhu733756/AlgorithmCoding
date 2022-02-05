#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     2-keys-keyboard.py
@Time    :     Mon Oct 18 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 18 2021
Modified By:   zhu733756
@Desc    :     给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数
@link    :     https://leetcode-cn.com/problems/2-keys-keyboard/submissions/
'''

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for _ in range(n+1)] 
        for i in range(2, n+1):
            dp[i] = i
            for j in range(2, n//2 +1):
                if i % j == 0:
                    dp[i] = dp[j] + dp[i//j]
                    break
        return dp[n]
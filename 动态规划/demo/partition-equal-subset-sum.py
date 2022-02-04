#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     partition-equal-subset-sum.py
@Time    :     Mon Oct 18 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 18 2021
Modified By:   zhu733756
@Desc    :     给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
@link    :     https://leetcode-cn.com/problems/partition-equal-subset-sum/
'''

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
      """
      目标是选取一部分物品，使得它们的总和为 sum/2, 0-1 背包问题
      dp[i][j] 表示 第i个物品选择后能保证总和为 sum/2
      """
      s = sum(nums)
      if s % 2:
        return False
      
      target, n = s // 2, len(nums)
      dp = [[False for j in range(target+1)] for i in range(n+1)]

      for i in range(n+1):
        dp[i][0] = True

      for i in range(1, n+1):
        for j in range(1, target+1):
          if j >= nums[i-1]:
            dp[i][j] =  dp[i-1][j] | dp[i-1][j-nums[i-1]] #注意完全背包，也就是可以重复拿，这里的写法
          else:
            dp[i][j] =  dp[i-1][j]
      
      return dp[n][target]
      

class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
      """
      目标是选取一部分物品，使得它们的总和为 sum/2, 0-1 背包问题
      dp[i] 表示 第i个物品选择后能保证总和为 sum/2
      空间压缩
      """
      s = sum(nums)
      if s % 2:
        return False
      
      target, n = s // 2, len(nums)
      dp = [False for j in range(target+1)]
      dp[0] = True

      for i in range(1, len(nums)+1):
        for j in range(target, nums[i-1]-1, -1):  #注意0-1背包，也就是可以重复拿，这里的写法是逆序
          dp[j] =  dp[j] or dp[j-nums[i-1]]
      
      return dp[target]
      
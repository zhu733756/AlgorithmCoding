#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     longest-increasing-subsequence.py
@Time    :     Mon Oct 18 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 18 2022
Modified By:   zhu733756
@Desc    :     找到其中最长严格递增子序列的长度
@link    :     https://leetcode-cn.com/problems/longest-increasing-subsequence/
'''
from  typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      """
      以i结尾的最长递增子序列的长度为dp，只要保证j -> (0, i)有序数增加一个，dp[i] = max(dp[j] +1, dp[i])
      n**2
      """
      dp = [0] *len(nums)
      max_value = float("-inf")
      for i in range(0, len(nums)):
        for j in range(0, i):
          if nums[j] < nums[i]:
            dp[i] = max(dp[j] +1, dp[i])
        max_value = max(max_value, dp[i])
      
      return max_value

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
      """
      求解最长子序列，保证二分法数值的值单调递增，每次取出x在数组中第l大的数，如果未超出数组length，则更新，否则加入最后
      n*log(n)
      """
      import bisect
      d = [] 
      for i in range(0, len(nums)):
        l = bisect.bisect_left(d, nums[i])
        if l < len(d) :
          d[l] = nums[i]
        else:
          d.append(nums[i])
      
      return len(d)
        
          


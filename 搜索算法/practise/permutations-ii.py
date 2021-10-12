#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     permutations-ii.py
@Time    :     Tue Oct 12 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Tue Oct 12 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/permutations-ii/submissions/
'''

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, path):
            if len(nums) == 0:
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                # 排序后可通过一下条件去重
                if i >0 and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                # 每次递归将当前元素剔除
                dfs(nums[:i]+nums[i+1:], path)
                path.pop()

        nums.sort()
        ans = []
        dfs(nums, [])
        return ans
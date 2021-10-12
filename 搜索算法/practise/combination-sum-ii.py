#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     combination-sum-ii.py
@Time    :     Tue Oct 12 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Tue Oct 12 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/combination-sum-ii/submissions/
'''
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(index, n, path, s):
            if s > target:
                return

            if s == target:
                ans.append(path[:])
                return 
                
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                s += candidates[i]
                dfs(i+1, n, path, s)
                path.pop()
                s -= candidates[i]

        candidates.sort()
        ans = []
        dfs(0, len(candidates), [], 0)
        return ans
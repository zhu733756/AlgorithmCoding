#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     permutations.py
@Time    :     Thu Oct 07 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Thu Oct 07 2021
Modified By:   zhu733756
@Desc    :     回溯时，全排列可以从只要不是当前index值的集合中筛选
@link    :     https://leetcode-cn.com/problems/permutations/submissions/
'''

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def track_back(n, path):
            if len(path) == n:
                ans.append(path[:])
                return

            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                track_back(n, path)
                path.pop()
        
        ans=[]
        track_back(len(nums),[])
        return ans

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def track_back(index, n, path):
            if index == n-1:
                ans.append(path[:])
                return

            for i in range(index, n):
                path[i], path[index] = path[index], path[i]
                track_back(index+1, n, path)
                path[index], path[i] = path[i], path[index]
                
        ans=[]
        track_back(0, len(nums), nums)
        return ans


if __name__ == '__main__':
    Solution2().permute([1,2,3])
    
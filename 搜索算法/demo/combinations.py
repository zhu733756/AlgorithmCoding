#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     combinations.py
@Time    :     Thu Oct 07 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Thu Oct 07 2021
Modified By:   zhu733756
@Desc    :     组合可以用index加快回溯
@link    :     https://leetcode-cn.com/problems/combinations/submissions/
'''
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def track_back(index, length, path, k):
            if len(path) == k:
                ans.append(path[:])
                return

            for i in range(index,length):
                path.append(nums[i])
                track_back(i+1, length, path, k)
                path.pop()

        ans = []
        nums = list(range(1,n+1))
        track_back(0, n, [], k)
        return ans

if __name__ == '__main__':
    Solution().combine(4, 2)
    
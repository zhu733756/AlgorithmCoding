#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     number-of-provinces.py
@Time    :     yyyy/Oct/Tu
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Tue Oct 05 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/number-of-provinces/submissions/  
'''

from typing import Deque, List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # stack, dfs
        ans = 0
        m = len(isConnected)
        visited = set()
        for i in range(m):
            if i not in visited: # 注意边的数量，本题的边有无数条
                ans += 1
                stack = [i]
                while stack:
                    x = stack.pop()
                    visited.add(i)
                    for y in range(m):
                        if isConnected[x][y] == 1 and y not in visited:
                            visited.add(y)
                            stack.append(y)

        return ans


from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # queue, bfs
        ans = 0
        m = len(isConnected)
        visited = set()
        for i in range(m):
            if i not in visited: # 注意边的数量，本题的边有无数条
                ans += 1
                q = deque([i])
                while q:
                    x = q.popleft()
                    visited.add(i)
                    for y in range(m):
                        if isConnected[x][y] == 1 and y not in visited:
                            visited.add(y)
                            q.append(y)

        return ans

class Solution3:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # recursive
        def recursive(x): 
            visieted.add(x)
            for y in range(n):
                if y not in visieted and isConnected[x][y] == 1:
                    recursive(y)

        ans = 0
        n = len(isConnected)
        visieted = set()

        for i in range(n):
            if i not in visieted:
                recursive(i)
                ans += 1

        return ans
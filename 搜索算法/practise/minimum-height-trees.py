#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     minimum-height-trees.py
@Time    :     Thu Oct 14 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Thu Oct 14 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/minimum-height-trees/submissions/
'''

from collections import defaultdict,deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 2:
            return [0,1]
        if n == 1:
            return [0]

        boards = defaultdict(set)
        for i,j in edges:
            boards[i].add(j)
            boards[j].add(i)

        queue = deque()
        for key,value in boards.items():
            if len(value) == 1: # 入度为1的叶子节点
                queue.append(key)

        while queue:
            size = len(queue)
            n = n - size

            for _ in range(size):
                # 弹出入度为1的节点
                u = queue.popleft()
                for v in boards[u]:
                    # 去掉链接
                    boards[v].remove(u)
                    if len(boards[v]) == 1:
                        queue.append(v)
            
            if n == 1:
                return [queue.popleft()]
            if n == 2:
                return [queue.popleft(), queue.popleft()]



if __name__ == '__main__':

    Solution().findMinHeightTrees(n=4, edges=[[1,0],[1,2],[1,3]])
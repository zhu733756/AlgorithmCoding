#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     shortest-bridge.py
@Time    :     Sat Oct 09 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Sat Oct 09 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/shortest-bridge/submissions/
'''
from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # dfs找到第一个岛屿，把1全部设置为2, 找到第一个为0的点进行跳出
        # bfs遍历，将出现的0设置为2，直到碰到内层的1立即返回

        def dfs(r, c, m, n):
            if r <0 or r >= m or c<0 or c>=n or grid[r][c] == 2:
                return 

            if grid[r][c] == 0:
                points.append((r,c))
                return
                
            grid[r][c] = 2 

            for dx,dy in directions:
                x,y = r+dx, c+dy
                dfs(x,y,m,n)

        points = []
        m,n = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        flag = False
        for i in range(m):
            if flag:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, m, n)
                    flag = True
                    break

        queue = deque(points)
        level = 0
        while queue:
            level += 1
            size = len(queue)
            while size > 0:
                r,c = queue.popleft()
                grid[r][c] = 2
                for dx,dy in directions:
                    x,y = r+dx, c+dy
                    if x>=0 and x <m and y >=0 and y<n:
                        if grid[x][y] == 2:
                            continue
                        if grid[x][y] == 1:
                            return level
                        grid[x][y] = 2
                        queue.append((x,y))
                size -= 1
            
        return 0
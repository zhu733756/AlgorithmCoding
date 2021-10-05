#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :     max-area-of-island.py
@Time    :     Tue Oct 05 2021
@Author  :     zhu33756
@Contact :     1079333812@qq.com
Last Modified: Tue Oct 05 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/max-area-of-island/ 
'''

from typing import List

class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.set = set()
        max_area = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                max_area = max(max_area, self.dfs(grid, i, j, m, n))
        return max_area

    def recursive(self, grid, x, y, nx, ny):
        # 使用递归来进行dfs
        if x <0 or x >= nx or y <0 or y >= ny or grid[x][y] == 0:
            # 终止条件
            return 0

        area =  1
        self.set.add((x,y))
        # 也可以使用grid[x][y] = 0

        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if (x+dx,y+dy) not in self.set:
                area += self.dfs(grid, x+dx, y+dy, nx, ny)

        return area


class Solution2:
    # 使用stack进行dfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = [(i,j)]
                    grid[i][j] = 0
                    local_area = 1
                    while len(stack) > 0:
                        x,y = stack.pop()
                        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                            x1,y1 = x+dx,y+dy
                            if x1 <0 or x1 >= m or y1 <0 or y1 >= n or grid[x1][y1] == 0:
                                continue
                            grid[x1][y1] = 0
                            local_area += 1
                            stack.append((x1,y1))

                    max_area = max(max_area, local_area)
        return max_area

from collections import deque

class Solution3:
    # 使用deque进行bfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        max_area = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q = deque([(i,j)])
                    grid[i][j] = 0
                    local_area = 1
                    while len(q) > 0:
                        x,y = q.pop()
                        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                            x1,y1 = x+dx,y+dy
                            if x1 <0 or x1 >= m or y1 <0 or y1 >= n or grid[x1][y1] == 0:
                                continue
                            grid[x1][y1] = 0
                            local_area += 1
                            q.appendleft((x1,y1))

                    max_area = max(max_area, local_area)
        return max_area
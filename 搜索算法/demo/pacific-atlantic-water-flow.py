#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     pacific-atlantic-water-flow.py
@Time    :     Tu Oct 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Tue Oct 05 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/pacific-atlantic-water-flow/submissions/
'''

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs 

        directions= [(-1,0),(1,0),(0,-1),(0,1)]

        def recursive(visited, r, c, m, n):
            visited.add((r,c))
            for dx,dy in directions:
                x,y = r+dx, c+dy
                if x >= 0 and x <m and y >= 0 and y<n and heights[r][c] <= heights[x][y] and (x,y) not in visited:
                    recursive(visited, x, y, m, n)


        visited_a, visited_b = set(),set()
        m,n = len(heights), len(heights[0])
        ans =[]

        # 从四个角进行dfs搜索，两个集合的交集就是ans

        for i in range(m):
            recursive(visited_a, i, 0, m, n)
            recursive(visited_b, i, n-1, m, n)
        
        for j in range(n):
            recursive(visited_a, 0, j, m, n)
            recursive(visited_b, m-1, j, m, n)
        
        can_flows = visited_a.intersection(visited_b)

        for i in range(m):
            for j in range(n):
                if (i,j) in can_flows:
                    ans.append([i,j])
        return ans


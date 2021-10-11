#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     surrounded-regions.py
@Time    :     Mon Oct 11 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 11 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/surrounded-regions/submissions/
'''
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs_neighbors(r, c, m ,n):
            if r < 0 or r >= m or c <0 or c >=n or board[r][c] == "X" or (r,c) in blocks:
                 return
            
            blocks.add((r,c))
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x,y = r+dx, c+dy
                dfs_neighbors(x,y,m,n)
        
        #  从边界开始遍历不可选的points，把跟他们相邻的点标记出来
        blocks = set()
        m,n  = len(board),len(board[0])
        for i in range(m):
            if board[i][0] == "O":
                dfs_neighbors(i, 0, m, n)
            if  board[i][n-1] == "O":
                dfs_neighbors(i,n-1, m, n)
        for j in range(n):
            if board[0][j] == "O":
                dfs_neighbors(0, j, m, n)
            if  board[m-1][j] == "O":
                dfs_neighbors(m-1, j, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in blocks:
                    board[i][j] = "X"


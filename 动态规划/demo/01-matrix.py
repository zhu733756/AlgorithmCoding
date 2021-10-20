#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     01-matrix.py
@Time    :     Wed Oct 20 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Wed Oct 20 2021
Modified By:   zhu733756
@Desc    :     两个相邻元素间的距离为 1 , 需要从四个方向搜索
@link    :     https://leetcode-cn.com/problems/01-matrix/submissions/
'''

from typing import List

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[float("inf")] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向左移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i < m-1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j < n-1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m-1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j  < n-1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist
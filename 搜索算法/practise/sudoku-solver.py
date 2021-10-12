#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     sudoku-solver.py
@Time    :     Thu Oct 14 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Thu Oct 14 2021
Modified By:   zhu733756
@Desc    :     解数独
@link    :     https://leetcode-cn.com/problems/sudoku-solver/submissions/
'''

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        数独的解法需 遵循如下规则：
        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
        """
        l = [str(i) for i in range(1,10)]

        # 每行每列每块可用数值
        rows_set = [set(l) for i in range(9)]
        cols_set = [set(l) for j in range(9)]
        buckets_set = [set(l) for k in range(9)]
        
        # 需要补充的缺口
        points = []
        
        # 已经使用的数，剔除
        # 将需要填入的坐标1填入points数组
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows_set[i].remove(board[i][j])
                    cols_set[j].remove(board[i][j])
                    buckets_set[i//3*3 + j // 3 ].remove(board[i][j])
                else:
                    points.append((i,j))
            
        def back_tracking(index, total):
            if index == total:
                return True

            r,c = points[index]
            k = r//3 * 3  + c // 3 
            for no in (rows_set[r] & cols_set[c] & buckets_set[k]):
                # rows_set[r] & cols_set[c] & buckets_set[k] 当前可用数集合
                rows_set[r].remove(no)
                cols_set[c].remove(no)
                buckets_set[k].remove(no)
                board[r][c] = no
                if back_tracking(index+1, total):
                    return True
                rows_set[r].add(no)
                cols_set[c].add(no)
                buckets_set[k].add(no)
                board[r][c] = "."
                
            return False

        back_tracking(0, len(points))
        return
                    
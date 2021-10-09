#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     word-search.py
@Time    :     Thu Oct 07 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Sat Oct 09 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/word-search/submissions/
'''
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def back_tracking(r, c, index):
            if index == word_length:
                return True
            
            for dx,dy in directions:
                x,y = r+ dx, c+dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == word[index]:
                    board[x][y] = "#"
                    if back_tracking(x,y,index+1):
                        return True
                    board[x][y] = word[index]
            
            return False

        m,n = len(board),len(board[0])
        word_length = len(word)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    board[i][j] = "#"
                    if back_tracking(i,j,1):
                        return True
                    board[i][j] = word[0]
        
        return False
        
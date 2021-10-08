#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     n-queens.py
@Time    :     Fri Oct 08 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Fri Oct 08 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/n-queens/submissions/
'''

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def back_tracking(buckets, r, n):
            if r ==n:
                ans.append(["".join(x) for x in buckets[:]])
                return

            for c in range(n):
                if c not in up and (r-c) not in na and (r+c) not in pie:
                    buckets[r][c] = "Q"
                    up.add(c)
                    na.add(r-c)
                    pie.add(r+c)
                    back_tracking(buckets, r+1, n)
                    up.remove(c)
                    na.remove(r-c)
                    pie.remove(r+c)
                    buckets[r][c] = "."

        buckets = [["." for j in range(n)] for i in range(n)]
        ans = []
        up,pie,na = set(), set(), set()
        back_tracking(buckets, 0, n)
        
        return ans
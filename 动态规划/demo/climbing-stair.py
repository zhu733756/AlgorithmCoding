#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     climbing-stair.py
@Time    :     Fri Oct 15 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Fri Oct 15 2021
Modified By:   zhu733756
@Desc    :     爬楼梯
@link    :     https://leetcode-cn.com/problems/climbing-stair/submissions/
'''

# 递推公式： f(n) = f(n-1) + f(n-2)

# 递归超时

class Solution1:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairs(n-2) + self.climbStairs(n-1)


# 存储局部解

class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        ans = [0]*n
        ans[0] = 1
        ans[1] = 2
        for i in range(2, n):
            ans[i] = ans[i-1] + ans[i-2]

        return ans[n-1]

# 保存f(i-1)和f(i-2)的状态值, 对动态规划进行空间压缩

class Solution3:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev, cur = 1, 2 
        for _ in range(2, n):
            prev, cur = cur, prev+cur

        return cur
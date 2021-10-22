#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     decode-ways.py
@Time    :     Fri Oct 22 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Fri Oct 22 2021
Modified By:   zhu733756
@Desc    :     使用1-26之间的字母来解码数字型字符串
@link    :     https://leetcode-cn.com/problems/decode-ways/submissions/
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0]*n
        for i in range(1, n+1):
            if s[i-1] != "0":
                # 一个字符解码
                f[i] += f[i-1]
            if i > 1 and s[i-2] != "0" and int(s[i-2:i]) <= 26:
                # 两个字符解码
                f[i] += f[i-2]
        return f[n]
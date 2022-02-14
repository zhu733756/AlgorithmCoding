# https://leetcode-cn.com/problems/longest-common-prefix/
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_strs, max_strs = min(strs), max(strs)
        if len(max_strs) == 0:
            return ""
        
        for i in range(len(min_strs)):
            if min_strs[i] != max_strs[i]:
                return min_strs[:i]
        
        return min_strs
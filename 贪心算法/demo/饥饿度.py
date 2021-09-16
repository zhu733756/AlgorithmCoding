# -*- coding: UTF-8 -*-
from typing import List

# 可读性强
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        p,q = 0,0
        while p < len(g) and q < len(s):
            if g[p] <= s[q]:
                child += 1
                p += 1
                q += 1
            else:
                q += 1
        return child
    
# 精简参数
class Solution2:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p,q = 0,0
        while p < len(g) and q < len(s):
            if g[p] <= s[q]:
                p += 1
            q += 1
        return p
    
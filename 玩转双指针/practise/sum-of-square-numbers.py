"""
https://leetcode-cn.com/problems/sum-of-square-numbers/
"""

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 1:
            return True
        l, r = 0, int(math.sqrt(c))+1
        while l < r:
            div = c - l * l
            if int(math.sqrt(div))**2 == div:
                return True
            l += 1
        return False
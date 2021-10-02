"""
https://leetcode-cn.com/problems/sqrtx/
"""

# -*- coding: UTF-8 -*-
from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l,r = 0, x 

        while l <=r:
            mid = (l+r) >> 1
            s = mid ** 2
            if s > x:
                r = mid-1
            else:
                l = mid+1
        # 不知道返回哪个，可以采用特例验证：
        # 例如 x =8, 最终应该返回2， 循环体内 (l,r): => (0,8) => (0,3) => (2,3) => (3,3) => (3,2)，所以return r
        # 另外，既然是向下取整，不满足的条件是l > r ，此时l 必然是大于r的，所以应该返回较小值。
        return r
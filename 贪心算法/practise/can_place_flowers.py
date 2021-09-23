# -*- coding: UTF-8 -*-
"""
https://leetcode-cn.com/problems/can-place-flowers/
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count, num, prev = 0, len(flowerbed), -1
        for i in range(num):
            # 分段计算两个1之间最多可以放多少个1
            if flowerbed[i] == 1:
                # 最后一个是1，其他都是0
                if prev < 0:
                    count += i // 2
                else:
                    count += (i-prev-2) // 2
                prev = i

        if prev < 0:
            #全是0, [0,0,0]
            count += (num+1) // 2
        else:
            # 1之后全是0,[1,0,0,0,0]
            count += (num-prev-1) //2

        return count >= n



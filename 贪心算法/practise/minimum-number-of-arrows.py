# -*- coding: UTF-8 -*-
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return  0
        count = 1
        points = sorted(points, key=lambda x: x[1])
        prev = points[0][1]
        for i in range(1,len(points)):
            # 计算非重叠区间的数量
            if points[i][0] > prev:
                count += 1
                prev = points[i][1]
        # 每多一个非重叠区间就需要多打一枪
        return count

class Solution2:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        points = sorted(points, key=lambda x: x[1])
        for i in range(1,len(points)):
            # 计算重叠区间的数量
            if points[i][0] <= points[i-1][1]:
                count += 1
                points[i][1] = points[i-1][1]
        #总数减去最大重叠区间的数量
        return len(points) -count
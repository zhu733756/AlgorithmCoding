# -*- coding: UTF-8 -*-
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        # 按照区间的最大值排序
        intervals = sorted(intervals, key = lambda x: x[1])
        for i in range(1, len(intervals)):
            # 如果有重叠区间发生时，也就是当前区间的最小值小于前一个区间的最大值
            # 这时候，当前区间要丢弃，计数加一，并且把区间最大值替换为前一个区间的最大值。
            # 这样保证，剩余区间与之前空间重叠的概率大大降低。
            if intervals[i][0] < intervals[i-1][1]:
                intervals[i][1] = intervals[i-1][1]
                ans += 1
        return ans


class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        ans = 0
        # 按照区间的最大值排序
        intervals = sorted(intervals, key = lambda x: x[1])
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            # 如果有重叠区间发生时，也就是当前区间的最小值小于前一个区间的最大值
            # 这时候，当前区间要丢弃，计数加一，并且把区间最大值替换为前一个区间的最大值。
            # 这样保证，剩余区间与之前空间重叠的概率大大降低。
            if intervals[i][0] < prev:
                ans += 1
            else:
                prev = intervals[i][1]
        return ans
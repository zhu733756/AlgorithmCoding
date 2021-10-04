# -*- coding: UTF-8 -*-

"""
https://leetcode-cn.com/problems/sort-characters-by-frequency/submissions/
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        buckets ={}
        for i in s:
            buckets[i] = buckets.get(i,0)+1

        buckets = sorted(buckets.items(), key=lambda x: -x[1])
        return "".join([j[0]*j[1] for j in buckets])
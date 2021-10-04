# -*- coding: UTF-8 -*-

"""
https://leetcode-cn.com/problems/top-k-frequent-elements/submissions/
"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        也可以进行堆排序
        """
        # 先进行桶计数
        buckets = {}
        for num in nums:
            buckets[num] = buckets.get(num,0)+1
        
        # 根据频次进行逆序快排
        counts_od= sorted(buckets.items(), key= lambda x:-x[1])
        ans = []
        for i in range(k):
            ans.append(counts_od[i][0])
        return ans
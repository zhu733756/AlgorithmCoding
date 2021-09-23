"""
https://leetcode-cn.com/problems/queue-reconstruction-by-height/
https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/xian-pai-xu-zai-cha-dui-dong-hua-yan-shi-suan-fa-g/
"""

# -*- coding: UTF-8 -*-
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按照身高hi逆序、前面身高大于或等于 hi 的人数量ki升序
        people = sorted(people, key= lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            if len(ans) <= p[1]:
                ans.append(p)
            else:
                ans.insert(p[1],p )
        return ans


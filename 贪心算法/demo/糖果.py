# -*- coding: UTF-8 -*-
from typing import List

class Solution:
    def candy(self, ratings: List[int]):
        s = [1] * len(ratings)
        # 正向遍历
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                s[i] = s[i-1] +1
        # 反向遍历
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                s[j] = max(s[j+1] +1,s[j])
        return sum(s)

if __name__ == '__main__':
    print(Solution().candy([1,3,2,2,1]))
    
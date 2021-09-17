# -*- coding: UTF-8 -*-
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 按照字母顺序存入字母最后一次出现的位置
        last=[0]*26
        for i,c in enumerate(s):
            last[ord(c)-ord("a")] = i

        start,end = 0,0 # 表示上一个和本次划分范围的间隔点
        ans = [] #接收结果
        for i in range(len(s)):
            end = max(end, last[ord(s[i])-ord("a")])
            if end == i:
                ans.append(end+1-start)
                start = end+1 
        return ans
    
if __name__ == '__main__':
    Solution().partitionLabels("ababcbacadefegdehijhklij")
    
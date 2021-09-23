
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 使用滑动窗口，先固定右边界，在右移收缩左边界
        l,r,N = 0, 0,len(s)
        targets= Counter(t)
        window = Counter()
        min_len = float("inf")
        ans = ""
        # 比较滑动窗口的值是否满足要求
        check = lambda: all(map(lambda x: window[x] >= targets[x], targets.keys()))
        while r < N:
            if s[r] in targets:
                window[s[r]] += 1
            
            while check() and l <= r:
                # 包括了所有值，但不满足最小字符串要求
                if min_len > r-l +1:
                    min_len = min(min_len, r-l+1)
                    ans =  s[l: r+1]
                window[s[l]] -=1 
                l += 1
            r +=1
        return ans


if __name__ == '__main__':
    Solution().minWindow(s="ADOBECODEBANC",t="ABC")
    
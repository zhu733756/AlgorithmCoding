# https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/submissions/
# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
# 动态规划： 1. 当 i < 0i<0 ，即 s[j]s[j] 左边无相同字符，则 dp[j] = dp[j-1] + 1dp[j]=dp[j−1]+1 
# 2、当 dp[j - 1] < j - i ，说明字符 s[i]s[i] 在子字符串 dp[j-1]dp[j−1] 区间之外 ，则 dp[j] = dp[j - 1] + 1dp[j]=dp[j−1]+1 
# 3、当 dp[j - 1] >= j - i ，说明字符 s[i]s[i] 在子字符串 dp[j-1]dp[j−1] 区间之中 ，则 dp[j]dp[j] 的左边界由 s[i]s[i] 决定，即 dp[j] = j - idp[j]=j−i ；

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i
            dic[s[j]] = j # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        哈希表统计字符 s[j] 最后一次出现的索引 。
        """
        length = len(s)
        if length <= 1:
            return length
        
        left = -1
        max_length = 1
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                left = max(dic.get(s[i], 0), left)
            dic[s[i]] = i
            max_length = max(max_length, i-left)
        return max_length            


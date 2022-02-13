# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

class Solution:
    def translateNum(self, num: int) -> int:
        arr = str(num)
        if len(arr) <= 1:
            return 1

        dp = [0] * (len(arr)+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(arr)+1):
            if 10 <= int(arr[i-2:i]) <= 25:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]

        return dp[len(arr)]


class Solution2:
      def translateNum(self, num: int) -> int:
        arr = str(num)
        if len(arr) == 1:
            return 1

        prev, next = 1, 1
        for i in range(1, len(arr)):
            prev, next = next, (prev + next) if 10 <= int(arr[i-1:i+1]) <= 25 else next
        
        return next
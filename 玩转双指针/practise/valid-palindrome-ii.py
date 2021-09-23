"""
https://leetcode-cn.com/problems/valid-palindrome-ii
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        l,r = 0, len(s) -1
        while l <= r:
            if s[l] !=  s[r]:
                return self.isPalindrome(s,l-1,r) or self.isPalindrome(s,l,r-1)
            l += 1
            r -= 1
        return True

    def isPalindrome(self, s, low, high) -> bool:
        return s[low:high+1] == s[high+1:low:-1]

class Solution2:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        l,r = 0, len(s) -1
        while l <= r:
            if s[l] !=  s[r]:
                return self.isPalindrome(s[l+1:r+1]) or self.isPalindrome(s[l:r])
            l += 1
            r -= 1
        return True

    def isPalindrome(self, s) -> bool:
        return s == s[::-1]
                
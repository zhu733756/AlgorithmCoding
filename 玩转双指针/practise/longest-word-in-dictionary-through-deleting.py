"""
https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting
"""
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary, key = lambda x: (-len(x), x))
        for d in dictionary:
            i,j = 0,0
            while i < len(s) and j < len(d):
                if s[i] == d[j]:
                    j += 1
                i += 1    
            if j == len(d):
                return d 
        return ""


if __name__ == '__main__':

    Solution().findLongestWord("abpcplea",["ale","apple","monkey","plea"])
                
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        ans = 0
        se = {}
        l = 0
        for r in range(len(s)): 
            se[s[r]] = se.get(s[r],0) +1
            while len(se) > k:
                se[s[l]] -= 1
                if se[s[l]] == 0:
                    del se[s[l]]
                l += 1
            ans = max(ans, r-l+1)
        return ans
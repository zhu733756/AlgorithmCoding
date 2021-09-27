class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l,r = 0, x 

        while l <=r:
            mid = (l+r) >> 1
            s = mid ** 2
            if s > x:
                r = mid-1
            else:
                l = mid+1

        return r
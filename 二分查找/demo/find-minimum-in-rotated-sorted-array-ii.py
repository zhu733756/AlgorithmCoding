"""
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left +right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] == nums[right]:
                right = right -1
            else:
                left = mid +1
        return nums[left]
                

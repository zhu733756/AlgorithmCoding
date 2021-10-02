"""
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left +right) // 2
            if nums[mid] < nums[right]:
                # [3,1,3] 有可能mid就是最小值，所以不能使用mid-1
                right = mid
            elif nums[mid] == nums[right]:
                # mid可能就是最小值，只能往左逼近一步
                right = right -1
            else:
                left = mid +1
        return nums[left]
                

"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''二分查找'''
        left,right =0,len(nums)-1
        while left<=right:
            mid = (left+right) //2
            if nums[mid] == target:
                return True
            # 考虑到左右两边相等，如[1,0,1,1]
            if nums[mid] == nums[left] == nums[right]:
                left +=1
                right -= 1
            elif nums[mid] >= nums[left]:
                # [left, mid] 有序
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid+1
            elif nums[mid] <= nums[right]:
                # [mid, right] 有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return False
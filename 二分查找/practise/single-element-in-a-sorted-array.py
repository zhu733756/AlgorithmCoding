"""
https://leetcode.com/problems/single-element-in-a-sorted-array/
"""
# 异或
class Solution1:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1,len(nums)):
            ans = ans ^ nums[i]
        return ans

class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        while left < right:
            # 如果left == right了，说明该退出了。因为每次都会跳过偶数个数，剩余区间包含那个只有一个的元素，当左右所以相等时，就是那个目标元素了。
            mid = (left+right) //2
            flag = (right - mid) % 2 == 0
            if nums[mid] == nums[mid+1]:
                if flag:
                    left = mid +2
                else:
                    right = mid -1
            elif nums[mid] == nums[mid-1]:
                if flag:
                    right = mid-2
                else:
                    left = mid +1
            else:
                return nums[mid]
        return nums[left]


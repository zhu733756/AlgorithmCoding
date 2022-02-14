# https://leetcode-cn.com/problems/3sum/solution/
# 三数之和

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []

        for i in range(length-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            left,right =i+1, length-1
            target = -nums[i]
            while left < right:
                cal = nums[left] + nums[right]
                if cal == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left <right and nums[left] == nums[left+1]:
                        left += 1
                    while left <right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cal < target:
                    left = left +1
                else:
                    right = right-1

        return ans

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash = {}
        ans = []

        nums.sort()
        
        for i in range(len(nums)):
            hash[nums[i]] = i

        for i in range(len(nums)-1):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                s = nums[i]+nums[j]
                if -s in hash and hash.get(-s) > j:
                    ans.append([nums[i], nums[j], -s])

        return ans
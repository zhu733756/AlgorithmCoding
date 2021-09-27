class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        for index, num in enumerate(nums):
            if num == target:
                if ans[0] == -1:
                    ans = [index,index]
                else:
                    ans[-1] = index
        return ans

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]

        left,right = 0,len(nums)-1
        
        def get_bound(left,right,target,method="left"):
            while left <= right:
                mid = (left+right) //2
                if target == nums[mid]:
                    if method == "left":
                        right = mid-1
                    else:
                        left = mid+1
                elif target > nums[mid]:
                    left = mid+1
                else:
                    right = mid -1

            if method == "left":
                if left <= len(nums)-1 and nums[left] == target:
                    return left
                else:
                    return -1
            else:
                if right >= 0 and nums[right] == target:
                    return right
                else:
                    return -1


        return [get_bound(left,right,target,"left"),get_bound(left,right,target,"right")]
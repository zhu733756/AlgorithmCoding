# -*- coding: UTF-8 -*-

"""
这是一个归并排序的demo
时间复杂度 o(n*log(n)) -> o(n*n)
空间复杂度 o(n)
原地排序算法，稳定排序
"""

class solution():

    def mergesort(self, nums):

        def _merge_sort(nums, left, right):
            if left >= right:
                return

            mid = (left + right) >> 1
            # 分割
            _merge_sort(nums, left, mid)
            _merge_sort(nums, mid+1, right)
            # 合并
            _merge(nums, left, mid, right)
            return

        def _merge(nums, left, mid, right):
            temp = [0]*(right-left+1)
            i = 0
            l, r = left, mid+1
            while l <= mid and r <= right:
                if nums[l] <= nums[r]:
                    temp[i] = nums[l]
                    l += 1
                else:
                    temp[i] = nums[r]
                    r += 1
                i += 1

            if l == mid +1:
                temp[i:] = nums[r:right+1] 
            
            if r == right+1:
                temp[i:] = nums[l:mid+1]

            nums[left:right+1] = temp[:]
            return

        _merge_sort(nums, 0, len(nums)-1)
        return nums


if __name__=="__main__":
    arr = solution().mergesort([30,24,5,58,18,36,12,42,39])
    print(arr)
  

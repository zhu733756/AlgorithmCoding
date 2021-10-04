# -*- coding: UTF-8 -*-

"""
这是一个快速排序的demo
时间复杂度 o(n*log(n)) -> o(n*n)
空间复杂度 o(1)
原地排序算法，不稳定排序，基于选择排序的思想
"""
from copy import deepcopy

class solution():

    def quicksort(self, nums):

        def partition(nums, left, right):
            """
            返回分区的索引，也就是数组第k大的索引位置，更大的数往右边丢
            """
            pivot, pindex = nums[right], right
            for i in range(right-1, left-1, -1):
                if nums[i] >= pivot:
                    # 每出现要给比pivot大的数, pindex应该减1
                    pindex = pindex -1
                    # 将更大的数往后交换
                    nums[i], nums[pindex] = nums[pindex], nums[i]
            
            # 将第k位索引所在位置的数与pivot交换
            nums[pindex], nums[right] = nums[right], nums[pindex]
            return pindex
        
        def _quick_sort(nums, left, right):
            if left >= right:
                return 
            
            pivot = partition(nums, left, right)
            _quick_sort(nums, left, pivot-1)
            _quick_sort(nums, pivot+1, right)

        _quick_sort(nums, 0, len(nums)-1)
        return nums


if __name__=="__main__":
    arr = solution().quicksort([30,24,5,58,18,36,12,42,39])
    print(arr)
  

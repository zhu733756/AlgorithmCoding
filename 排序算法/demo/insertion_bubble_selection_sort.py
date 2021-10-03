# -*- coding: UTF-8 -*-

"""
这是一个插入、冒泡、选择排序的demo
时间复杂度 o(n*n)
都是原地排序算法，不申请额外空间
冒泡和插入是稳定算法，选择和快排不是稳定算法
"""

def insertion_sort(nums):
    """
    将nums[i]插入到[0,i]处正确的位置上，从后往前遍历不需要考虑[k,i]序列之前拷贝位置的问题
    """
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j-1],nums[j] =  nums[j],nums[j-1]
    return nums


def bubble_sort(nums):
    """
    [len(nums)-i-1, len(nums)-1] 为已经排序好的区间
    每次从前面的区间取一个该区间最大数给最后长度为i的区间
    """
    for i in range(1, len(nums)):
        swapped = False
        for j in range(1, len(nums)-i+1):
            if nums[j] < nums[j-1]:
                nums[j-1],nums[j] =  nums[j],nums[j-1]
                swapped = True
        if swapped:
            break
            
    return nums

def selection_sort(nums):
    """
    排序区：[0,i]
    未排序区：[i+1, length-1]
    从未排序区找小于排序区最后一个数，进行交换
    """
    for i in range(0, len(nums)-1):
        p =i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[p]:
                p =j
        nums[p], nums[i] = nums[i], nums[p]
    return nums



if __name__ == '__main__':
    print(insertion_sort([30,24,5,58,18,36,12,42,39]))
    print(bubble_sort([30,24,5,58,18,36,12,42,39]))
    print(selection_sort([30,24,5,58,18,36,12,42,39]))
    
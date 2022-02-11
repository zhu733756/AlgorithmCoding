# https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
# 给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为1。

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i,j = 0, len(numbers)-1
        while i < j:
            mid = (i+j) >> 1
            if numbers[mid] > numbers[j]:
                i = mid+1
            elif numbers[mid] < numbers[j]:
                j = mid
            else:
                j = j-1
        return numbers[i]
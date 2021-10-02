"""
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/submissions/
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 这题使用双指针技巧，假设两个数组已经按照要求排好序合并为一个数组，长度分别是m,n，只需要遍历一半长度，也就是(m+n)/2 +1
        # 如果总长度为奇数，求取这个范围的最大值，如果总长度为偶数，则要求取这个范围最大值和次最大值，求平均值
        # 有几处边界：如果其中一个数组遍历完，怎么处理？如果总长度为偶数，怎么保留次最大值？
        m,n = len(nums1),len(nums2)
        length = m+n
        l,r = 0,0
        half_max_left, half_max_right = -1, -1
        for i in range(length//2+1):
            #进行值传递，解决偶数长度下的问题
            half_max_left = half_max_right
            if l < m and r < n:
                if nums1[l] <= nums2[r]:
                    half_max_right = nums1[l]
                    l += 1
                else:
                    half_max_right = nums2[r]
                    r += 1
            elif l == m:
                half_max_right = nums2[r]
                r += 1
            else:
                half_max_right = nums1[l]
                l += 1
        if length %2 == 0:
            return (half_max_left + half_max_right) / 2
        else:
            return half_max_right
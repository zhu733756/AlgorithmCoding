# https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
# 剑指 Offer 52. 两个链表的第一个公共节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        p = a + c
        q = b + c
        if p is None:
            p + headB = a + c + b + c
        if q is None:
            q+ headA = b +c + a+ c 
        """
        p,q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

# https://leetcode-cn.com/problems/add-two-numbers/
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy = ListNode(1)
        p = dummy

        prev = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            p.next = ListNode((x+y+prev) % 10)
            prev = (x+y+prev) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            p = p.next

        if prev:
            p.next = ListNode(prev)

        return dummy.next
            
# -*- coding: UTF-8 -*-
"""
https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 快慢指针，快指针一次走两步，慢指针一次走一步，如果会和了，表示有环
        # 第一次相遇，fast走了两倍的路程，slow走了一倍的路程，
        # 这时，将fast移动到head位置，步长保持相同，则可以到达有环的位置

        fast, slow = head, head
        #判断是否有环
        while 1:
            if fast is None or fast.next is None:
                # 没有环，直接返回
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        # 第二次相遇
        fast = head
        while fast != slow :
            fast = fast.next
            slow = slow.next
        return fast
# https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/submissions/
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        root = head
        while root:
            stack.append(root.val)
            root = root.next

        l = ListNode(None)
        if len(stack) > 0:
            tail = ListNode(stack.pop())
            l.next = tail
            while stack:
                tail.next = ListNode(stack.pop())
                tail = tail.next
        return l.next

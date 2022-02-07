# https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        root = head
        while root:
            res.append(root.val)
            root = root.next
        return res[::-1]
# https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/submissions/
# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

# Definition for a Node.
class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
      self.val = int(x)
      self.next = next
      self.random = random

class Solution:
  """
  缓存所有node，再进行组装。
  """
  def copyRandomList(self, head: 'Node') -> 'Node':
      p = head
      nodes = {}
      while p:
          nodes[p] = Node(p.val)
          p = p.next
      
      p = head
      while p:
          nodes.get(p).random = nodes.get(p.random, None)
          nodes.get(p).next = nodes.get(p.next, None)
          p = p.next
      
      return nodes.get(head)
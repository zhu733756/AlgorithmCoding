# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        stack = [(root, 0)]
        combined = []
        while stack:
            node, level = stack.pop()
            if node is None:
                continue
            if level >= len(combined):
              combined.append([node.val])
            else:
              combined[level].append(node.val)
 
            stack.append((node.right, level+1))
            stack.append((node.left, level+1))
        
        ans = []
        for c in combined:
          ans.extend(c)
        
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        combined = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node is None:
                continue
            
            if level >= len(combined) :
                combined.append([node.val])
            else:
                combined[level].append(node.val)
            
            stack.append((node.right, level+1))
            stack.append((node.left, level+1))
        
        return combined

            
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        combined = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node is None:
                continue
            
            if level >= len(combined):
                combined.append([node.val])
            else:
                combined[level].append(node.val)

            stack.append((node.left, level+1))
            stack.append((node.right, level+1)) 
        
        ans = []
        for i, c in enumerate(combined):
            if i % 2:
                ans.append(c)
            else:
                ans.append(c[::-1])
                  
        return ans

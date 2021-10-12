#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     binary-tree-paths.py
@Time    :     Mon Oct 11 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Mon Oct 11 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/binary-tree-paths/submissions/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def dfs(path, root):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                ans.append("->".join(str(i) for i in path[:]))
            if root.left:
                dfs(path, root.left)
            if root.right:
                dfs(path, root.right)
            path.pop()
        
        ans = [] 
        dfs([], root)
        return ans
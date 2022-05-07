#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/13 9:38 
# @Author : Eden.hu
# @description :

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 路径：等于边数 也等于共有父节点的左节点深度+右节点深度之和
        # 只需要计算所有节点 左节点深度和右节点深度  求其最大
        # 题变成了求深度，并记录左右深度之和的最大

        def getDepth(root):
            if not root:
                return 0
            left_depth = getDepth(root.left)
            right_depth = getDepth(root.right)
            self.max_depth = max(self.max_depth,left_depth+right_depth)
            return max(left_depth,right_depth)+1
        getDepth(root)
        return self.max_depth

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/24 1:48 下午 
# @Author : huxiaoliang
# @description :
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        result = []
        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            result.append(root.val)
            traversal(root.right)

        traversal(root)
        return result

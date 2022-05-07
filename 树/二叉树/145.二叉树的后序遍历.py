#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/24 1:47 下午 
# @Author : huxiaoliang
# @description :
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        result = []
        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            traversal(root.right)
            result.append(root.val)

        traversal(root)
        return result

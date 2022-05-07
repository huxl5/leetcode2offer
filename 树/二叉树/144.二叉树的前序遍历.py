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
    def preorderTraversal(self, root):
        # 前序:父左右,递归
        # 保存结果
        result = []
        def traversal(root):
            if root == None:
                return
            result.append(root.val) # 前序
            traversal(root.left)    # 左
            traversal(root.right)   # 右

        traversal(root)
        return result



    # 迭代：后进先出  # list中 append 放在最后，pop()取出最后的,pop(0)取出最前的
    # 递归替换,一般用stack迭代
    def preorderTraversal2(self, root):
        # 迭代
        result = []
        if not root:
            return result
        stack = [root] # 后进先出
        while stack:
            cur_node = stack.pop() # 尾部
            result.append(cur_node.val)
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left: # 后进先出
                stack.append(cur_node.left)

        return result
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/12 19:14 
# @Author : Eden.hu
# @description :
# attention：简单的中序遍历不可，会进行多次翻转
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 相当于遍历二叉树,此处用层序遍历
        if not root:
            return root
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                cur_node = queue.pop(0)
                # 交换
                cur_node.left,cur_node.right = cur_node.right,cur_node.left
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return root
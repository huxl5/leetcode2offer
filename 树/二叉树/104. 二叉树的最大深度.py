#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/12 22:35 
# @Author : Eden.hu
# @description :
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 1、层序遍历迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 层次遍历的最后一层，先进先出，队列
        level_num = 0
        if not root:
            return level_num
        queue = [root]
        while queue:
            level_num +=1
            size  = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return level_num

# 2、递归，后序，左右中。求每个节点的最大高度，左右节点的最大值即为最大深度
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 递归：左右节点高度 最大值+1
        def getDepth(root):
            if not root:
                return 0
            left_depth = getDepth(root.left) # 左
            right_depth = getDepth(root.right) # 右
            depth = 1 + max(left_depth,right_depth) # 中
            return depth

        return getDepth(root)

# 3、递归，前序，中左右，回溯。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0 # 非引用变量
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 递归：回溯，中左右
        def backtrack(root,depth):
            self.max_depth = max(self.max_depth,depth) # 中 ，位置，收集结果
            if not root:
                return
            if root.left:
                backtrack(root.left,depth+1) # 处理，递归，回溯
            if root.right:
                backtrack(root.right,depth+1)
        if not root: # 边界值
            return self.max_depth
        backtrack(root,1)
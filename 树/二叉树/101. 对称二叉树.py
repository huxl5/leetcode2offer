#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/12 19:24 
# @Author : Eden.hu
# @description :
# 思路
# 首先想清楚，判断对称二叉树要比较的是哪两个节点，要比较的可不是左右节点！
# 对于二叉树是否对称，要比较的是根节点的左子树与右子树是不是相互翻转的，
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        # 左树和右树遍历比较：父左右 父右左遍历
        # 递归：参考代码随想录
        def helper(left, right):
            if left == None and right == None:
                return True
            elif left == None and right != None:
                return False
            elif left != None and right == None:
                return False
            elif left.val != right.val:
                return False
            else:
                return helper(left.left, right.right) and helper(left.right, right.left)

        if not root:
            return True
        return helper(root.left, root.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        # 迭代，栈
        # 参考代码随想录：哪个放数据的图
        if not root:
            return True
        stack = [root.left,root.right]
        while stack:
            right = stack.pop()
            left = stack.pop()
            if not left and not right:
                continue
            if not left or not right or left.val!=right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
            # if left ==None and right !=None:
            #     return False
            # elif left != None and right == None:
            #     return False
            # elif left != None and right !=None and left.val != right.val:
            #     return False
            # elif left == None and right == None:
            #     continue
            # else:
            #     stack.append(left.left)
            #     stack.append(right.right)
            #     stack.append(left.right)
            #     stack.append(right.left)
        return True
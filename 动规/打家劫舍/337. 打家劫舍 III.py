#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/24 14:36 
# @Author : Eden.hu
# @description :
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 方法一：递归，一定是后序遍历，因为要根据返回结果处理
    def rob(self, root: TreeNode) -> int:
        # 递归出口
        if not root:  # 无节点
            return 0
        if not root.left and not root.right:  # 只有一个节点
            return root.val
        # 关键：是否偷当前节点
        # 1 偷当前节点
        ans1 = root.val
        if root.left:
            ans1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            ans1 += self.rob(root.right.left) + self.rob(root.right.right)

        # 2 不偷当前节点
        ans2 = self.rob(root.left) + self.rob(root.right)
        return max(ans1, ans2)

class Solution:
    def __init__(self):
        self.memory = {}

    def rob(self, root: TreeNode) -> int:
        # 递归出口
        if not root:  # 无节点
            return 0
        if not root.left and not root.right:  # 只有一个节点
            return root.val
        # 递归优化：记忆化递推，通过记录计算过程，减少重复计算
        if root in self.memory:
            return self.memory[root]

        # 关键：是否偷当前节点
        # 1 偷当前节点
        ans1 = root.val
        if root.left:
            ans1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            ans1 += self.rob(root.right.left) + self.rob(root.right.right)

        # 2 不偷当前节点
        ans2 = self.rob(root.left) + self.rob(root.right)
        self.memory[root] = max(ans1, ans2)
        return self.memory[root]

# 动归
class Solution:
    def rob(self, root: TreeNode) -> int:
        ans = self.robAction(root)
        return max(ans[0],ans[1])
    def robAction(root):
        # 递归出口，同时也是dp初始化
        if not root:
            return (0,0) #偷，不偷
        left = self.robAction(root.left)
        right = self.robAction(root.right)
        # 1 偷当前节点
        ans1 = root.val + left[1] + right[1]
        # 2 不偷当前节点
        ans2 = max(left[0],left[1])+max(right[0],right[1])
        return (ans1,ans2)

class Solution:
    def rob(self, root: TreeNode) -> int:
        def robAction(root):
            # 递归出口，同时也是dp初始化
            if not root:
                return (0,0) #偷，不偷
            left = robAction(root.left)
            right = robAction(root.right)
            # 1 偷当前节点
            ans1 = root.val + left[1] + right[1]
            # 2 不偷当前节点
            ans2 = max(left[0],left[1])+max(right[0],right[1])
            return (ans1,ans2)
        ans = robAction(root)
        return max(ans[0],ans[1])
        # TODO：写到方法里，不需要用self；写到方法外，要用self


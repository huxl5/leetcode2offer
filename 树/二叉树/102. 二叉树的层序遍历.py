#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/24 12:51 下午 
# @Author : huxiaoliang
# @description :


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs:
class Solution:
    def levelOrder(self, root):
        results = []
        if root is None:
            return results
        queue = [root]
        while queue:  # 每迭代一次就是一层
            size = len(queue)
            result = []
            for _ in range(size):
                cur_node = queue.pop(0)  # 先进先出
                result.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            results.append(result)
        return results





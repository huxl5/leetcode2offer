#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/25 4:16 下午 
# @Author : huxiaoliang
# @description :
class Solution:
    def combine(self, n: int, k: int):
        # 组合-》回溯 回溯就是递归后回撤操作
        paths = []
        path = []
        def backtrack(n, k, start_index):
            # 递归出口
            if len(path) == k:
                # 结果收集
                paths.append(path[:])  # TODO:存放值,不可存放索引
                return
            # for 遍历树的宽度
            for i in range(start_index, n + 1):
            # for i in range(start_index, n - (k-len(path))+1+1): # TODO:剪枝优化 n - (k-len(path))+1  总共n个元素,已经有了k-len(path)个元素,最多从n-(k-len(path))+1 + 1是边界
            # if len(path)+(n-i+1)<k:# 剪枝
            #     break
                # 处理
                path.append(i)
                # 递归
                backtrack(n, k, i + 1)
                # 回溯:撤销处理
                path.pop()
        backtrack(n, k, 1)
        return paths

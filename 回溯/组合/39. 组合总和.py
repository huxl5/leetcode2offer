#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/25 7:58 下午 
# @Author : huxiaoliang
# @description :
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1： 输入：candidates = [2,3,6,7], target = 7, 所求解集为： [ [7], [2,2,3] ]
#
# 示例 2： 输入：candidates = [2,3,5], target = 8, 所求解集为： [   [2,2,2,2],   [2,3,3],   [3,5] ]


class Solution:
    def __init__(self):
        self.paths = []
        self.path = []
        self.tmp_sum = 0
    def combinationSum(self, candidates, target: int) :

        def backtrack(candidates,target,start_index):
            # 递归退出条件,同时收集结果
            if self.tmp_sum>target:
                return
            if self.tmp_sum==target:
                # 收集结果
                self.paths.append(self.path[:])
                return
            # 横向遍历所有选择
            for i in range(start_index,len(candidates)):
                # 因为是无序数组，剪枝只能是纵向剪枝，使用continue停止纵向递归，但横向遍历仍然得继续 FIXME:是否对,应该对，不是return
                if self.tmp_sum+candidates[i]>target:
                    continue
                # 处理
                self.path.append(candidates[i])
                self.tmp_sum += candidates[i]
                # 递归
                backtrack(candidates,target,i)
                # 回溯:撤销处理
                self.path.pop()
                self.tmp_sum -= candidates[i]
        backtrack(candidates,target,0)
        return self.paths
candidates = [2,3,6,7,1]
target = 7
print(Solution().combinationSum(candidates, target))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/29 7:15 下午 
# @Author : huxiaoliang
# @description :
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出: [ [2], [1], [1,2,2], [2,2], [1,2], [] ]
# 理解“树层去重”和“树枝去重”非常重要。
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def subsetsWithDup(self, nums):
        nums.sort()
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums, start_index: int) -> None:
        # ps.空集合仍符合要求
        self.paths.append(self.path[:])
        # Base Case
        if start_index == len(nums):
            return

        # 单层递归逻辑
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                # 当前后元素值相同时，跳入下一个循环，去重
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()

#TODO 用usedlist记录树枝和数层去重
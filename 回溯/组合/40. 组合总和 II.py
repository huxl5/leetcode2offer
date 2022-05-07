#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/25 8:36 下午 
# @Author : huxiaoliang
# @description :
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明： 所有数字（包括目标数）都是正整数。 解集不能包含重复的组合。
#
# 示例 1: 输入: candidates = [10,1,2,7,6,1,5], target = 8, 所求解集为: [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ]
#
# 示例 2: 输入: candidates = [2,5,2,1,2], target = 5, 所求解集为: [   [1,2,2],   [5] ]
 # TODO： 横向重复，纵向重复
 # 本题是横向不可重复
# 回溯+巧妙去重(省去使用used
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []
        self.tmp_sum = 0
    def combinationSum2(self, candidates, target: int):
        # 重复主要出现在,树宽度遍历时,会出现相同元素
        candidates.sort()

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
                # 因为纵向不可继续加数字，横向有序，也不可加。剪枝 FIXME:return
                if self.tmp_sum+candidates[i]>target:
                    return #
                if i>start_index and candidates[i]==candidates[i-1]:
                    continue # 不往深度递归了
                # 处理
                self.path.append(candidates[i])
                self.tmp_sum += candidates[i]
                # 递归
                backtrack(candidates,target,i+1) # 不重复使用同一个元素,但是可以相同的值在数的不同深度
                # 回溯:撤销处理
                self.path.pop()
                self.tmp_sum -= candidates[i]
        backtrack(candidates,target,0)
        return self.paths

# 回溯+去重（使用used）
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []
        self.used = []

    def combinationSum2(self, candidates, target: int):
        '''
        类似于求三数之和，求四数之和，为了避免重复组合，需要提前进行数组排序
        本题需要使用used，用来标记区别同一树层的元素使用重复情况：注意区分递归纵向遍历遇到的重复元素，和for循环遇到的重复元素，这两者的区别
        '''
        self.paths.clear()
        self.path.clear()
        self.usage_list = [False] * len(candidates)
        # 必须提前进行数组排序，避免重复
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates, target: int, sum_: int, start_index: int) -> None:
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(start_index, len(candidates)):
            # 剪枝，同39.组合总和
            if sum_ + candidates[i] > target:
                return

            # 检查同一树层是否出现曾经使用过的相同元素
            # 若数组中前后元素值相同，但前者却未被使用(used == False)，说明是for loop中的同一树层的相同元素情况
            if i > 0 and candidates[i] == candidates[i - 1] and self.usage_list[i - 1] == False:
                continue

            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.usage_list[i] = True
            self.backtracking(candidates, target, sum_, i + 1)
            self.usage_list[i] = False  # 回溯，为了下一轮for loop
            self.path.pop()  # 回溯，为了下一轮for loop
            sum_ -= candidates[i]  # 回溯，为了下一轮for loop

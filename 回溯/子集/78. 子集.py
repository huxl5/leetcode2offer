#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/29 2:03 下午 
# @Author : huxiaoliang
# @description :
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例: 输入: nums = [1,2,3] 输出: [ [3],   [1],   [2],   [1,2,3],   [1,3],   [2,3],   [1,2],   [] ]
class Solution:
    def subsets(self, nums):
        result = []
        path = []

        def backtrack(nums,start_index):
            result.append(path[:]) # 此处收集结果,所有叶子节点
            # 递归结束
            if start_index==len(nums):
                # pass
                return
            for i in range(start_index,len(nums)):
                path.append(nums[i])
                backtrack(nums,i+1)
                path.pop()
        backtrack(nums,0)
        return result

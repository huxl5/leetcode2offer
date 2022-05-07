#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/29 7:44 下午 
# @Author : huxiaoliang
# @description :
# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
#
# 示例:
#
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# 输入：nums = [4,4,3,2,1]
# 输出：[[4,4]]
# 说明:
#
# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
class Solution:
    def findSubsequences(self, nums):
        result = []
        path = []
        def backtrack(nums,start_index):
            if len(path)>=2:
                result.append(path[:])
            if start_index == len(nums):
                return
            # 单层递归逻辑
            # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
            used_list = set() # 相同元素不一定相邻,所以要同层去重
            for i in range(start_index,len(nums)):
                if (path and path[-1]>nums[i]) or nums[i] in used_list:
                    continue
                used_list.add(nums[i])
                path.append(nums[i])
                backtrack(nums,i+1)
                path.pop()
        backtrack(nums,0)
        return result
# FIXME：有人用深度优先

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/29 8:31 下午 
# @Author : huxiaoliang
# @description :
class Solution:
    def permute(self, nums):
        result = []
        path = []
        used = [False]*len(nums) # 表达每一个分支节点是否用过
        def backtrack(nums): # 不需要
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(0,len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(nums)
                path.pop()
                used[i] = False
        backtrack(nums)
        return result
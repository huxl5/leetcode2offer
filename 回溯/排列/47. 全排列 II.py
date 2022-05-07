#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/29 8:45 下午 
# @Author : huxiaoliang
# @description :

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [0]*len(nums)
        nums.sort()
        def backtrack(nums):
            if len(path)==len(nums):
                result.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]: # 同列去重
                    if i>0 and nums[i]==nums[i-1] and not used[i-1]: # 同层重复要去除
                            continue
                    path.append(nums[i])
                    used[i] = 1
                    backtrack(nums)
                    path.pop()
                    used[i] = 0
        backtrack(nums)
        return result

print(Solution().permuteUnique([1, 1, 2]))
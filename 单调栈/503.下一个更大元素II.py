#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/25 3:00 下午 
# @Author : huxiaoliang
# @description :
class Solution:
    def nextGreaterElements(self, nums):
        dp = [-1] * len(nums)
        stack = []
        for i in range(len(nums)*2):
            while(len(stack) != 0 and nums[i%len(nums)] > nums[stack[-1]]):
                    dp[stack[-1]] = nums[i%len(nums)]
                    stack.pop()
            stack.append(i%len(nums))
        return dp

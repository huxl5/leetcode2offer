#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/25 2:31 下午 
# @Author : huxiaoliang
# @description :
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 单调栈 分别找左右连续子数组的左右边界
        # see:https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/dan-diao-zhan-jie-fa-on-by-20182726-e3pb/
        n = len(nums)
        stack = [0]
        left = n
        for i in range(1,n):
            while stack and nums[i]<nums[stack[-1]]:
                left = min(stack.pop(),left)
            stack.append(i)
        right = 0
        stack = [n-1]
        for i in range(n-1)[::-1]:
            while stack and nums[i]>nums[stack[-1]]:
                right = max(stack.pop(),right)
            stack.append(i)
        return right-left+1 if right-left>0 else 0

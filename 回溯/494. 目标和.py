#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/8 11:34 
# @Author : Eden.hu
# @description :
class Solution:
    def __init__(self):
        self.result = 0
    def findTargetSumWays(self, nums, target: int) -> int:
        def backtrack(nums,target,start_index,sum):
            # 递归出口
            if start_index>len(nums)-1:
                if sum==target:
                    self.result +=1
                return
            # 横向遍历 + -
            # 递归 回溯
            backtrack(nums,target,start_index+1,sum-nums[start_index])
            backtrack(nums,target,start_index+1,sum+nums[start_index])
        backtrack(nums,target,0,0)

        return self.result
        # 时间复杂度：O(2^n) 空间复杂度O(n):主要取决于递归调用的栈空间，栈的深度不超过n。
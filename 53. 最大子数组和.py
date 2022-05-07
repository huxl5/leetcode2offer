#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 16:09 
# @Author : Eden.hu
# @description :

class Solution:
    def maxSubArray(self, nums) -> int:
        # 动态规划
        # dp[i] 表示以i为最后一个元素的连续子数组的最大和
        n = len(nums)
        dp = nums[:]
        for i in range(1,n):
            dp[i] = max(nums[i],dp[i-1]+nums[i])
        return max(dp)

class Solution:
    def maxSubArray(self, nums) -> int:
        # 动态规划 优化
        # dp[i] 表示以i为最后一个元素的连续子数组的最大和
        n = len(nums)
        predp = nums[0]
        result = nums[0]
        for i in range(1,n):
            predp = max(nums[i],predp+nums[i])
            result = max(predp,result)
        return result

# TODO：进阶分治法
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/3 13:50 
# @Author : Eden.hu
# @description :
class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return None
        # dp[i][0,1]:0 i为结尾的最大积，i为结尾的最小积
        dp = [[0,1] for _ in range(len(nums))]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        max_product = nums[0]# 求最小积
        for i in range(1,len(nums)):
            dp[i][0] = max(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i],nums[i])
            dp[i][1] = min(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i],nums[i])
            max_product = max(max_product,dp[i][0])
        return max_product
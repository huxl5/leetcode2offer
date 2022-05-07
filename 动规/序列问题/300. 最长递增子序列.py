#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/22 10:53 
# @Author : Eden.hu
# @description :
class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        # dp[i] 为0-i，包含i数字时，最长。。。的长度。（不连续）
        dp = [1]*n
        ans = 1 # 一个数字return 1
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
            ans = max(ans,dp[i])
        return ans

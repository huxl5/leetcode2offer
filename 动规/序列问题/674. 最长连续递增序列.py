#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/22 12:28 
# @Author : Eden.hu
# @description :
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = 1
        dp = [1]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i] = dp[i-1]+1
            ans= max(ans,dp[i])
        return ans
class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        # 贪心算法
        n = len(nums)
        ans = 1
        count = 1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                count +=1
            else:
                count = 1
            ans = max(ans,count)
        return ans
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/1 11:49 
# @Author : Eden.hu
# @description :
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 完全背包：排列问题
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1,target+1):# 先容量，再物品
            for j in range(len(nums)):
                if nums[j]<=i:
                    dp[i] +=dp[i-nums[j]]
        return dp[-1]
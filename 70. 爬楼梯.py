#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 16:34 
# @Author : Eden.hu
# @description :
# 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
# 动态规划 优化
class Solution:
    def climbStairs(self, n: int) -> int:
        dp0 = 1
        dp1 = 1
        dp2 = 1
        for i in range(2,n+1):
            dp2 = dp0 + dp1
            dp0,dp1 = dp1,dp2
        return dp2

# TODO：其他：递归，递归空间优化
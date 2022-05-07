#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/26 12:06 
# @Author : Eden.hu
# @description :
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 动归
        # dp[i][j] 到i-1的s串和到j-1的t串子串出现的个数
        # TODO:初始化
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    # 用/不用s[i-1]
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
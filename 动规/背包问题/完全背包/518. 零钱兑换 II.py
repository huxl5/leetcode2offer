#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/1 11:51 
# @Author : Eden.hu
# @description :
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1 # 一般方案数均为1
        for i in range(len(coins)):# 组合时，先遍历物品
            for j in range(coins[i],amount+1):
                dp[j] += dp[j-coins[i]]
        return dp[-1]
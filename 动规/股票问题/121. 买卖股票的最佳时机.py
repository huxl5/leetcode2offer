#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 17:36
# @Author : Eden.hu
# @description :TODO：需要重做
# see：https://programmercarl.com/0121.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA.html#_121-%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA
# 方法一：暴力O(n^2) O(1)


# 方法二：动态规划
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if not prices or n<=1:
            return 0
        dp = [[0,0] for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],-prices[i])
            dp[i][1] = max(prices[i]+dp[i-1][0],dp[i-1][1])
        return dp[-1][1]

# 动态规划：空间优化
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if not prices or n<=1:
            return 0
        dp = [[0,0] for _ in range(2)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1,n):
            dp[0][0] = max(dp[0][0],-prices[i])
            dp[0][1] = max(prices[i]+dp[0][0],dp[0][1])
        return dp[0][1]

# 方法三：贪心算法
# 因为股票就买卖一次，那么贪心的想法很自然就是取最左最小值，取最右最大值，那么得到的差值就是最大利润。
    def maxProfit(self, prices) -> int:
        min_price = int(1e9)
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit,price-min_price)
            min_price = min(min_price,price)
        return max_profit
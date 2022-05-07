#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/13 17:18 
# @Author : Eden.hu
# @description :
# 动态规划思路简单，但初始化要注意下
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)] # 注意初始化
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]

# 其他深搜，数论 TODO：一维数组
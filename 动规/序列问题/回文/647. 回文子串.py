#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/25 11:07 
# @Author : Eden.hu
# @description :

# 方法二：动态规划
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not str:
            return 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = 0
        for i in range(n)[::-1]:
            for j in range(i,n):
                if s[i] == s[j]:
                    if j-i<=1 or dp[i+1][j-1]:
                        ans +=1
                        dp[i][j] = True
        return ans
# 方法三：双指针-中心扩散法
class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(s, i, j, ans):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1
            return ans
            # 双指针
        ans = 0
        for i in range(len(s)):  # 0-n-1
            ans += helper(s, i, i, 0) + helper(s, i, i + 1, 0)  # i+1 TODOOK
        return ans

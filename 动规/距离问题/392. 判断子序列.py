#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/26 12:05 
# @Author : Eden.hu
# @description :

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m,n = len(s),len(t)
        i,j =0,0
        while i<m and j<n:
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return i == m
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # TODO为空处理
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        # 初始化：dp[i][0] dp[0][j] =0
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[-1][-1] == len(s)
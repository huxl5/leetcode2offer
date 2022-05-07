#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/1 16:49 
# @Author : Eden.hu
# @description :
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # dp[j] 0-j 的单词拆分开是否都出现在wordDict
        dp = [False]*(len(s)+1)
        dp[0] = True # 要是False的话，则全为False
        for i in range(1,len(s)+1):
            for word in wordDict:
                if len(word)<=i:
                    dp[i] = (dp[i]) or (dp[i-len(word)] and s[i-len(word):i]==word)
        return dp[-1]
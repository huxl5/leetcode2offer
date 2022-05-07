#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/23 13:30 
# @Author : Eden.hu
# @description :
class Solution:
    def findLength(self, nums1, nums2) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        if not nums1 or not nums2:
            return 0
        dp = [[0 for _ in range(n1+1)] for _ in range(n2+1)] # n1列，n2行
        ans = 0
        for i in range(1,n2+1):
            for j in range(1,n1+1):
                if nums1[j-1] == nums2[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                ans = max(ans,dp[i][j])
        return ans
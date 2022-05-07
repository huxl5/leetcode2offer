#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/24 16:05 
# @Author : Eden.hu
# @description :
class Solution:
    def rob(self, nums) -> int:
        #在198入门级的打家劫舍问题上分两种情况考虑
        #一是不偷第一间房，二是不偷最后一间房
        if len(nums)==1:#题目中提示nums.length>=1,所以不需要考虑len(nums)==0的情况
            return nums[0]
        val1=self.roblist(nums[1:])#不偷第一间房
        val2=self.roblist(nums[:-1])#不偷最后一间房
        return max(val1,val2)

    def robRange(self,nums):
        l=len(nums)
        dp=[0]*l
        dp[0]=nums[0]
        for i in range(1,l):
            if i==1:
                dp[i]=max(dp[i-1],nums[i])
            else:
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
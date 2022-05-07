#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 22:26 
# @Author : Eden.hu
# @description : 双指针
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 用l r维护一个0的区间：l指向第一个0，r指向第一个需要操作的数
        l = r = 0
        while r<len(nums):
            if nums[r]!=0:
                nums[l],nums[r] = nums[r],nums[l]
                l +=1
            r +=1
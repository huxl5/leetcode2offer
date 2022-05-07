#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/12 15:09 
# @Author : Eden.hu
# @description : 原定哈希
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 利用num和index对应关系为num-1 = index
        # 用num值标定其应该出现的位置，最后没有出现的位置即为结果
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]>0: # abs(nums[i])
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        res = []
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
    # set 做差
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1,len(nums)+1))-set(nums))
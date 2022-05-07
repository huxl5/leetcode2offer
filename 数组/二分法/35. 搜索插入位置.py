#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/19 23:06 
# @Author : Eden.hu
# @description :
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left = 0
        right = len(nums)-1 # target [left,right]
        while left <= right:
            middle = (left+right)>>1 # left + ((right-left)>>1)
            if nums[middle]<target: # 右
                left = middle +1
            elif nums[middle]>target: # 左
                right = middle -1
            else:
                return middle
        return right+1
        # // 分别处理如下四种情况
        # // 目标值在数组所有元素之前  [0, -1]
        # // 目标值等于数组中某一个元素  return middle;
        # // 目标值插入数组中的位置 [left, right]，return  right + 1
        # // 目标值在数组所有元素之后的情况 [left, right]， return right + 1
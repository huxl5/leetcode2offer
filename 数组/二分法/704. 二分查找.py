#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/19 22:37 
# @Author : Eden.hu
# @description :
class Solution:
    def search(self, nums, target: int) -> int:
        # 左闭右闭区间
        left = 0
        right = len(nums)-1 # 定义target在左闭右闭的区间里，[left, right]
        while left<=right:# 当left==right，区间[left, right]依然有效，所以用 <=
            middle = (left+right)>>1 # (left+right)//2
            if nums[middle]>target:
                right = middle - 1 # target 在左区间，所以[left, middle - 1]
            elif nums[middle]<target:
                left = middle + 1 # target 在右区间，所以[middle + 1, right]
            else: # nums[middle] == target
                return middle # 数组中找到目标值，直接返回下标
        return -1

class Solution:
    def search(self, nums, target: int) -> int:
        # 左闭右开区间
        left = 0
        right = len(nums) # 定义target在左闭右开的区间里，[left, right)
        while left<right:# 当left==right，区间[left, right)无效，所以用 <
            middle = (left+right)>>1 # (left+right)//2
            if nums[middle]>target:
                right = middle# target 在左区间，所以[left, middle)
            elif nums[middle]<target:
                left = middle + 1 # target 在右区间，所以[middle + 1, right)
            else: # nums[middle] == target
                return middle # 数组中找到目标值，直接返回下标
        return -1
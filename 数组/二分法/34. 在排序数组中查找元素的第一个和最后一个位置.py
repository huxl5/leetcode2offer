#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/19 23:18 
# @Author : Eden.hu
# @description :  TODO
class Solution:
    def searchRange(self, nums, target: int):
        def getRightBorder(nums:, target: int) -> int:
            left, right = 0, len(nums) - 1
            rightBoder = -2  # 记录一下rightBorder没有被赋值的情况
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                else:  # 寻找右边界，nums[middle] == target的时候更新left
                    left = middle + 1
                    rightBoder = left

            return rightBoder

        def getLeftBorder(nums, target: int) -> int:
            left, right = 0, len(nums) - 1
            leftBoder = -2  # 记录一下leftBorder没有被赋值的情况
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] >= target:  # 寻找左边界，nums[middle] == target的时候更新right
                    right = middle - 1;
                    leftBoder = right;
                else:
                    left = middle + 1
            return leftBoder

        leftBoder = getLeftBorder(nums, target)
        rightBoder = getRightBorder(nums, target)
        # 情况一
        if leftBoder == -2 or rightBoder == -2: return [-1, -1]
        # 情况三
        if rightBoder - leftBoder > 1: return [leftBoder + 1, rightBoder - 1]
        # 情况二
        return [-1, -1]
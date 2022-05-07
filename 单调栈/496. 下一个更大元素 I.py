#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/25 3:00 下午 
# @Author : huxiaoliang
# @description : 题目跟739类似，不过是需要判断是否在num1中
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = [-1]*len(nums1)
        stack = [0]
        for i in range(1,len(nums2)):
            # 情况一情况二
            if nums2[i]<=nums2[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack)!=0 and nums2[i]>nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]]) #求list元素index
                        result[index]=nums2[i]
                    stack.pop()
                stack.append(i)
        return result

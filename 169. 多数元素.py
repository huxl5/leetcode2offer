#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 21:20 
# @Author : Eden.hu
# @description : leetcode 169 27
# see:https://blog.csdn.net/fuxuemingzhu/article/details/51288749
# https://www.cnblogs.com/frankcui/p/10474223.html
# see：众数
class Solution:
    def majorityElement(self, nums) -> int:
        # 暴力：逐个判定是否是众数
        # 哈希表：O(n) O(n)
        count = 0
        for num in nums:
            if count == 0:
                cur = num
                count +=1
            else:
                if cur==num:
                    count+=1
                else:
                    count-=1
        return cur
    # TODO：27
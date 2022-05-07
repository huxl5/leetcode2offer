#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/12 16:01 
# @Author : Eden.hu
# @description :
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x^y # 异或
        y = 0
        while(x):
            if x%2==1:
                y +=1
            x = x//2 # 短除
        return y
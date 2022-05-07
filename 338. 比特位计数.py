#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/12 16:00 
# @Author : Eden.hu
# @description :
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 利用异或：参考461汉明距离
        res = []
        for i in range(n+1):
            tmp_bits = 0
            while i:
                if i%2:
                    tmp_bits +=1
                i = i//2
            res.append(tmp_bits)
        return res
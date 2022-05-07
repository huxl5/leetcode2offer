#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 20:51 
# @Author : Eden.hu
# @description :
# see：https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/

# 异或：
# 任何数和 00 做异或运算，结果仍然是原来的数，即a⊕0=a。
# 任何数和其自身做异或运算，结果是 00，即a⊕a=0。
# 异或运算满足交换律和结合律，即a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。


# 扩展：只有一个奇数个

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for num in nums:
            temp = temp^num
        return temp
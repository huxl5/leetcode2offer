#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/20 10:46 
# @Author : Eden.hu
# @description :
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = 1
        square = 1
        while square <= num:
            if square == num:
                return True
            x += 1
            square = x * x
        return False
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x0 = num
        while True:
            x1 = (x0 + num / x0) / 2
            if x0 - x1 < 1e-6:
                break
            x0 = x1
        x0 = int(x0)
        return x0 * x0 == num

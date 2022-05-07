#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/20 9:55 
# @Author : Eden.hu
# @description :
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        # 标准的二分法模版 ans随时记录结果
        left,right,ans = 0,x,-1
        while left<=right:
            mid = (left+right)>>1
            if mid**2 <= x:
                ans = mid
                left = mid +1
            elif mid**2  >x:
                right = mid -1
        return ans

    class Solution:
        def mySqrt(self, x: int) -> int:
            if x == 0:
                return 0
                # 牛顿迭代法，求函数0点。
            # xi = (x0+C/x0)/2 # x0通过斜率函数得到的xi
            C, x0 = float(x), float(x)  # 初始化要大一点，求正数根
            while True:
                xi = (x0 + C / x0) / 2
                if abs(x0 - xi) < 1e-6:  # 足够的冗余
                    break
                x0 = xi
            return int(x0)
class Solution:
    def mySqrt(self, x: int) -> int:
        # 函数变换
        if x==0:
            return 0
        ans = int(math.exp(0.5*math.log(x))) # 函数变换
        return ans+1 if (ans+1)**2<=x else ans
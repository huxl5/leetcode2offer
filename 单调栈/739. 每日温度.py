#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/24 11:10 上午 
# @Author : huxiaoliang
# @description :
# 方法一：暴力 求每个元素的结果，两层for


# 方法二:单调栈
class Solution:
    def dailyTemperatures(self, temperatures) :
        answer = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            # 情况一和情况二
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)

        return answer

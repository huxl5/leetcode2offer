#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/24 11:16 下午 
# @Author : huxiaoliang
# @description :
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 方法一:双指针 遍历,求i左右比其小的元素索引,然后heights[i]*w
        # O(n^2)
        # n = len(heights)
        # max_area = 0
        # for i in range(n):

        #     # 求左测最小元素索引
        #     left_index = i
        #     while left_index>=0 and heights[i]<=heights[left_index]:
        #         left_index -=1
        #     # 求右测最小元素索引
        #     right_index = i
        #     while right_index<=n-1 and heights[i]<=heights[right_index]:
        #         right_index +=1
        #     max_area = max(max_area,(right_index-left_index-1)*heights[i])
        # return max_area

        # 优化:将索引存起来
        # n = len(heights)
        # max_area = 0
        # left_index = [0]*n
        # right_index  = [0]*n
        # left_index[0] = -1 # 防止while死循环
        # for i in range(1,n): # 从1开始
        #     t = i -1
        #     while t>=0 and heights[t]>=heights[i]:
        #         t = left_index[t]
        #     left_index[i] = t
        # right_index[n-1] = n
        # for i in range(n-1)[::-1]:
        #     t = i +1
        #     while t<=n-1 and heights[t]>=heights[i]:
        #         t = right_index[t]
        #     right_index[i] = t
        # for i in range(n):
        #     max_area = max(max_area,(right_index[i]-left_index[i]-1)*heights[i])
        # return max_area

        # 单调栈
        # heights = [0]+heights
        # heights.append(0)
        # n = len(heights)
        # stack = [0]
        # max_area = 0
        # for i in range(1,n):
        #     if heights[i]>heights[stack[-1]]:
        #         stack.append(i)
        #     elif heights[i]==heights[stack[-1]]:
        #         stack.pop()
        #         stack.append(i)
        #     else:
        #         while stack and heights[i]<heights[stack[-1]]:
        #             mid = stack.pop()
        #             if stack:
        #                 left_index = stack[-1]
        #                 right_index = i
        #                 max_area = max(max_area,(right_index-left_index-1)*heights[mid])
        #         stack.append(i)
        # return max_area

        # 单调栈 优化
        heights = [0] + heights
        heights.append(0)
        n = len(heights)
        stack = [0]
        max_area = 0
        for i in range(1, n):
            while stack and heights[i] < heights[stack[-1]]:
                mid = stack.pop()
                if stack:
                    left_index = stack[-1]
                    right_index = i
                    max_area = max(max_area, (right_index - left_index - 1) * heights[mid])
            stack.append(i)
        return max_area




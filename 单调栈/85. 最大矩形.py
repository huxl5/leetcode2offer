#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/23 10:40 上午 
# @Author : huxiaoliang
# @description :
# @see:https://leetcode-cn.com/problems/maximal-rectangle/solution/tu-jie-jiang-ju-zhen-zhuan-huan-cheng-zh-xs8x/


class Solution:
    def maximalRectangle(self, matrix):

        # 简化为直方图中求最大面积
        def largestRectangleArea(heights):
            heights.insert(0, 0)
            heights.append(0)
            n = len(heights)
            stack = [0]
            max_area = 0
            for i in range(1, n):
                while stack and heights[i] < heights[stack[-1]]:
                    mid = stack.pop()
                    if stack:
                        max_area = max(max_area, heights[mid] * (i - stack[-1] - 1))
                stack.append(i)
            return max_area

        max_area = 0
        if not matrix:
            return matrix
        row_nums = len(matrix)
        col_nums = len(matrix[0])
        heights = [0] * col_nums
        for row in range(row_nums):
            for col in range(col_nums):
                if matrix[row][col] == "0": # 重点
                    heights[col] = 0
                else:
                    heights[col] += 1 # 重点
            max_area = max(max_area, largestRectangleArea(heights))
        return max_area

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalRectangle(matrix))
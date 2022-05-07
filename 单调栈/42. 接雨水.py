#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/24 10:22 上午 
# @Author : huxiaoliang
# @description :

# ***方法一：双指针，找当前元素（列）的左右两侧的最大值，从而求的当前列的水柱高度

# 方法二：双指针优化，用动态规划思路记忆中间步骤 left_max = max(left_max,height[i])

# 方法三：利用左右都要计算最大值再计算

# ***方法四：单调栈
class Solution:
    def trap(self, height) -> int:
        # see:https://programmercarl.com/0042.%E6%8E%A5%E9%9B%A8%E6%B0%B4.html#%E5%8F%8C%E6%8C%87%E9%92%88%E8%A7%A3%E6%B3%95
        # 方法一:双指针:计算所有位置的存水量(头尾没有)通过计算左右的最大值中的最小值-当前值计算
        # O(n^2) O(1)
        # n = len(height)
        # res_sum = 0
        # for i in range(1,n-1): # 首尾无法存水
        #     left_max,right_max = 0,0
        #     # 左边最大值
        #     for j in range(i):
        #         if height[j]>left_max:
        #             left_max = height[j]
        #     # 右边最大值
        #     for j in range(i+1,n):
        #         if height[j]>right_max:
        #             right_max = height[j]
        #     h = min(left_max,right_max)-height[i]
        #     if h>0:
        #         res_sum += h
        # return res_sum

        # 方法二:动态规划,针对双指针计算左边和右边的最大值,  left_max[i] = max(height[i],left_max[i-1])  right_max[i] = max(height[i],right_max[i+1])
        # O(n) O(n)
        # n = len(height)
        # res_sum = 0
        # left_max = [0]*n
        # right_max = [0]*n
        # left_max[0] = height[0]
        # right_max[n-1] = height[-1]
        # for i in range(1,n):
        #     left_max[i] = max(height[i],left_max[i-1])
        # for i in range(n-1)[::-1]:
        #     right_max[i] = max(height[i],right_max[i+1])
        # for i in range(1,n-1):
        #     h = min(left_max[i-1],right_max[i+1])-height[i]
        #     if h>0:
        #         res_sum +=h
        # return res_sum

        # 方法二:动态规划空间优化:https://leetcode-cn.com/problems/trapping-rain-water/solution/shuang-zhi-zhen-fa-dong-tai-gui-hua-fa-d-yle3/
        n = len(height)
        res_sum = 0
        i,i_left_max,j_right_max = 0,0,0 # i<j 故 i_left_max<=j_left_max j_right_max<=i_right_max
        j = n-1
        while i<j:
            i_left_max = max(i_left_max,height[i])
            j_right_max = max(j_right_max,height[j])
            if i_left_max<j_right_max: #i_left_max<j_right_max<=i_right_max
                res_sum += i_left_max - height[i]
                i +=1
            else:#j_left_max>=i_left_max>=j_right_max
                res_sum += j_right_max-height[j]
                j-=1
        return res_sum


        # 方法三:方法一二都是当前列存雨水量,方法三计算当前行的雨水量,利用单调栈,递减栈,每次上升时,结算一次当前行雨水量.栈中存放索引
        # O(n^2)
        # res_sum = 0
        # n = len(height)
        # stack = [0]
        # for i in range(1,n):
        #     # if len(stack)>0 and height[i]<height[stack[-1]]:
        #     #     stack.append(i)
        #     if len(stack)>0 and height[i]==height[stack[-1]]:
        #         stack.pop()
        #         # stack.append(i)
        #     while len(stack)>0 and height[i]>height[stack[-1]]:
        #         mid = stack.pop()
        #         if stack: # 保证有左边界
        #             left = stack[-1]
        #             right = i
        #             h = min(height[left],height[right])-height[mid]
        #             w = right-left-1
        #             res_sum += h*w
        #     stack.append(i)
        # return res_sum

        # 方法三简化:
        # res_sum = 0
        # n = len(height)
        # stack = [0]
        # for i in range(1,n):
        #     while len(stack)>0 and height[i]>height[stack[-1]]:
        #         mid = stack.pop()
        #         if stack: # 保证有左边界
        #             left = stack[-1]
        #             right = i
        #             h = min(height[left],height[right])-height[mid]
        #             w = right-left-1
        #             res_sum += h*w
        #     stack.append(i)
        # return res_sum



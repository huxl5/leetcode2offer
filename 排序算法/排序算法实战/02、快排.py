#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/15 8:55 下午 
# @Author : huxiaoliang
# @description :快排 找一个点，左边放小，右边放大的 O(nlogn) 不稳定

def quick_sort(lis):
    if len(lis)<=1:
        return lis
    left = []
    right = []
    baseline = lis[0]
    for i in lis[1:]:
        if i<baseline:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [baseline] + quick_sort(right) # [baseline]

a = [2, 3, 4, 1, 45, 6, 6, 7, 8, 7, 9, 10, 18, 20, 30, 12]

print(quick_sort(a))
[1, 2, 3, 4, 6, 6, 7, 7, 8, 9, 10, 12, 18, 20, 30, 45]
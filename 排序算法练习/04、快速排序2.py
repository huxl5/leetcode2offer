#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/8 4:26 下午 
# @Author : huxiaoliang
# @description :
# Quick Sort
def quick_sort(data):
    """quick_sort"""
    if len(data) >= 2:
        mid = data[len(data)//2]
        left,right = [], []
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data
a = [2,3,4,1,45,6,6,7,8,7,9,10,18,20,30,12]

print(quick_sort(a))
[1, 2, 3, 4, 6, 6, 7, 7, 8, 9, 10, 12, 18, 20, 30, 45]

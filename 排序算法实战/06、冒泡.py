#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/16 10:54 上午 
# @Author : huxiaoliang
# @description :

def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

    return a
a = [2, 3, 4, 1, 45, 6, 6, 7, 8, 7, 9, 10, 18, 20, 30, 12]
print(bubbleSort(a))
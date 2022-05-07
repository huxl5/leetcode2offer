#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/15 9:25 下午 
# @Author : huxiaoliang
# @description : O(n^2) 稳定  维护左边有序，逐个插入前边有序序列
# TODO
def insert_sort(a):
    if a is None or len(a)<=1:
        return a
    for i in range(1,len(a)):
        tmp = a[i]
        j = i -1
        while j>=0 and a[j]>tmp:
            a[j+1] = a[j]
            j -=1
        a[j+1] = tmp
    return a
a = [2, 3, 4, 1, 45, 6, 6, 7, 8, 7, 9, 10, 18, 20, 30, 12]
print(insert_sort(a))


print([j for j in range(0,5)[::-1]])
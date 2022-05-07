#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/16 10:46 上午 
# @Author : huxiaoliang
# @description :左侧有序，右侧无序，右侧找最小放入左侧后 O(n^2) 稳定


def chooseSort(a):

    for i in range(0,len(a)):
        min_index = i
        j = i+1
        while j < len(a):
            if a[j]<a[min_index]:
                min_index = j
            j +=1
        a[i],a[min_index] = a[min_index],a[i]
    return a

a = [2, 3, 4, 1, 45, 6, 6, 7, 8, 7, 9, 10, 18, 20, 30, 12]
print(chooseSort(a))
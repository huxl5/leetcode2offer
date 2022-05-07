#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/15 9:08 下午 
# @Author : huxiaoliang
# @description :归并 二分，递归，合并 O(nlogn) 稳定
# TODO
def merge(left,right):
    # 两个有序数组合并，双指针
    i = 0
    j = 0
    res = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i +=1
        else:
            res.append(right[j])
            j +=1
    return res + left[i:]+right[j:]


def merge_sort(a):
    if a is None or len(a)<=1:
        return a
    mid = len(a)//2 # 保证 len为2时，仍然可以分成两份
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left,right)




a = [2, 3, 4, 1, 45, 6, 6, 7, 8, 7, 9, 10, 18, 20, 30, 12]

print(merge_sort(a))
[1, 2, 3, 4, 6, 6, 7, 7, 8, 9, 10, 12, 18, 20, 30, 45]

print([1,2,3][5:]) # lis不会越界
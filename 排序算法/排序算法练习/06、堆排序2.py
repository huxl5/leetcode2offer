#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/10 4:29 下午 
# @Author : huxiaoliang
# @description :对10亿个数，取TOP-1000 ；（有限的内存和计算复杂度）

# 思路：利用小顶堆，先取1000个数构建小顶堆，然后遍历剩余的数，跟顶堆比较，小于则舍弃，大于则替换，重新heapify



def heapify(tree,n,i):
    # i,left,right 求最小，交换
    if i>=n:
        return
    left = 2*i+1
    right = 2*i+2
    min = i
    if left<n and tree[left]<tree[min] :
        min = left
    if right<n and tree[right]<tree[min]:
        min = right
    if min !=i:
        tree[min],tree[i] = tree[i],tree[min]
        heapify(tree,n,min)

def build_heap(tree,n):
    last_node = n-1
    parent = (last_node-1)//2
    while parent>=0:
        heapify(tree,n,parent)
        parent = parent-1
    return tree

def topk_sort(topk,tree):
    for i in tree:
        if i >topk[0]:
            topk[0] = i
            heapify(topk,len(topk),0)

    # 排序 topk
    i = len(topk)-1
    while i >=0:
        topk[i],topk[0] = topk[0],topk[i]
        heapify(topk,i,0)
        i = i-1


tree = [58,26,45,18,22,39,96,75,80,65,63,28]
# heapify(tree,len(tree),0)
topk = build_heap(tree[:5],5)
topk_sort(topk,tree[5:-1])
print(topk)
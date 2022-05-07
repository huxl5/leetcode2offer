#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/8 9:55 下午 
# @Author : huxiaoliang
# @description :


def heapify(tree,n,i):
    if i>n-1:
         return
    left = 2*i+1
    right = 2*i+2
    max = i
    if left < n and tree[left]>tree[max]:
         max = left
    if right < n and tree[right]>tree[max]:
         max = right
    if max !=i:
         tree[i],tree[max] = tree[max],tree[i]
         heapify(tree,n,max)

# 构建堆
def build_heap(tree,n):
    last_node = n-1
    parent = int((last_node-1)/2)
    while parent>=0:
        heapify(tree,n,parent)
        parent = parent -1

def heap_sort(tree,n):
    build_heap(tree,n)
    i = n-1
    while i >=0:
        tree[0],tree[i] = tree[i],tree[0]
        heapify(tree,i,0)
        i = i-1



# tree = [4,10,3,5,1,2]
tree = [10,5,8,3,4,6,7,1,2]
# heapify(tree,len(tree),0)
# build_heap(tree,len(tree))
heap_sort(tree,len(tree))
print(tree)
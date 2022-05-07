#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/15 7:08 下午 
# @Author : huxiaoliang
# @description :堆排：
# asc：从小到大
# 大顶堆 用数组/列表存储完全二叉树
# O(nlogn) 不稳定

class Solution:
    def __init__(self):
        pass

    # 对某个节点进行heapify
    # i的子节点均为大顶堆的时候，则heapify后包括i在内为大顶堆
    def heapify(self,tree,n,i):
        if i>n:
            return
        left = 2 * i +1
        right = 2 * i +2
        max = i
        if left<n and tree[left]>tree[max]:
            max = left
        if right<n and tree[right]>tree[max]:
            max = right
        if max !=i:
            tree[max],tree[i] = tree[i],tree[max]
            self.heapify(tree,n,max)

    def build_heap(self,tree,n):
        # 构建大顶堆
        last_node = n-1
        parent = (last_node-1)//2
        while parent >= 0:
        # for i in range(parent)[::-1]: for 倒叙
            self.heapify(tree,n,parent)
            parent -= 1

    def heap_sort(self,tree,n):
        self.build_heap(tree,n)
        i = n-1
        while i>=0:
            # 交换头元素到最后，
            tree[0],tree[i] = tree[i],tree[0]
            self.heapify(tree,i,0)
            # print(tree)
            i -=1



# tree = [10,5,8,3,4,6,7,1,2]
# Solution().heapify(tree,len(tree),0)
tree = [4,6,7,1,2,5,10,8,3]
# Solution().build_heap(tree,len(tree))
Solution().heap_sort(tree,len(tree))
print(tree)
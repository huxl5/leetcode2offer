#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/8 20:27 
# @Author : Eden.hu
# @description :
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 双指针
    # see:https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/tu-jie-xiang-jiao-lian-biao-by-user7208t/
    # 无相交时，p1==p2为null
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1,p2 = headA,headB
        while p1!=p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
    # TODO：方法一：哈希集合
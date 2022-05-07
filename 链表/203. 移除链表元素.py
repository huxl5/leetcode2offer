#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/8 13:39 
# @Author : Eden.hu
# @description :
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):

        dummy_head = ListNode(next=head) #添加一个虚拟节点，方便头结点的删除
        pre = dummy_head
        cur = pre.next
        while cur:
            if cur.val != val:
                pre = cur
            else:
                pre.next = cur.next #删除cur.next节点
            cur = cur.next
        return dummy_head.next

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/8 19:52 
# @Author : Eden.hu
# @description :
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 迭代 O(2*min(m,n)) O(1)
    def mergeTwoLists(self, list1, list2):
        head_dummy = ListNode(val=-1) # 哑节点
        cur = head_dummy
        while list1 and list2:
            if list1.val<list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next  =list1  if list1 else list2
        return head_dummy.next
    # 递归
    def mergeTwoLists(self, list1, list2):
        def helper(l1,l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val<l2.val:
                l1.next = helper(l1.next,l2)
                return l1
            else:
                l2.next = helper(l1,l2.next)
                return l2
        return helper(list1,list2)
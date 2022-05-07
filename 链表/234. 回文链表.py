#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/8 20:43 
# @Author : Eden.hu
# @description :
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]
    # TODO:递归
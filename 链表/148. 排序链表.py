#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 11:17 
# @Author : Eden.hu
# @description :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        # 堆排，归并，快排
        # 插入排序 O(n^2) O(1)
        # if not head:
        #     return head
        # dummp_head = ListNode(-1,head)
        # last_sorted = head
        # curr = last_sorted.next
        # while curr:
        #     if last_sorted.val <= curr.val:
        #         last_sorted = curr
        #         curr = curr.next
        #     else:
        #         pre = dummp_head
        #         while pre.next.val<=curr.val:
        #             pre = pre.next
        #         last_sorted.next = curr.next
        #         curr.next = pre.next
        #         pre.next = curr
        #         curr = last_sorted.next
        # return dummp_head.next
        def helper(head,tail):
            if not head:
                return head
            if head.next == tail: # 左开右闭，有两个元素，不好含右边的
                head.next = None
                return head
            slow = fast = head
            while fast!=tail:
                slow = slow.next
                fast = fast.next # 直接fast.next.next 可能出现None，跟tail一致
                if fast!=tail:
                    fast = fast.next
            mid = slow
            return merge(helper(head,mid),helper(mid,tail))# 左闭右开
        def merge(h1,h2):
            dummp_head = ListNode(-1)
            curr = dummp_head
            while h1 and h2:
                if h1.val <= h2.val:
                    curr.next = h1
                    h1 = h1.next
                else:
                    curr.next = h2
                    h2 = h2.next
                curr = curr.next
            curr.next =h1 if h1 else h2
            return dummp_head.next

        return helper(head,None)
    # TODO:优化

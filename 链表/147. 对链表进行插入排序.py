#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 9:53 
# @Author : Eden.hu
# @description :
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummp_head = ListNode(-1, next=head)  # 可能操纵第一个节点，设置一个哑节点
        last_sort = head  # 最后一个有序，下一个无序
        cur = head.next
        while cur:
            if cur.val >= last_sort.val:
                last_sort = cur
            else:
                pre = dummp_head
                while pre.next.val <= cur.val:
                    pre = pre.next
                last_sort.next = cur.next
                cur.next = pre.next
                pre.next = cur
            cur = last_sort.next
        return dummp_head.next



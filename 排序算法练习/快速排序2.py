# -*- coding:utf-8 -*-
# TODO：最坏时间复杂度
# 参考：https://blog.csdn.net/weixin_36913190/article/details/80550347
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        pi = partition(alist, first, last)
        quickSortHelper(alist, first, pi - 1)
        quickSortHelper(alist, pi + 1, last)


def partition(alist, first, last):
    mid = alist[first]
    left_mark = first + 1
    right_mark = last
    done = True
    while done:
        # left_mark <= right_mark 必须是，才能出现left_mark大于right_mark
        # <= mid：才能出现left_mark大于right_mark
        while left_mark <= right_mark and alist[left_mark] <= mid:
            left_mark += 1
        while right_mark >= left_mark and alist[right_mark] >= mid:
            right_mark -= 1
        if left_mark > right_mark:
            done = False
        else:
            temp1 = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp1
    temp2 = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp2
    return right_mark


alist = [52, 312, 54, 54, 7, 3, 2]
quickSort(alist)
print(alist)

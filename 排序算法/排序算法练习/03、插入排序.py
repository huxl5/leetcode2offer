# -*- coding:utf-8 -*-
# 分为两部分，左边为排序好的，右边为未排序的。先移位，最后放入。
class Solution:

    def insertionSort2(self, arr):
        # write code here
        if type(arr) is not list:
            return '请传入一个数组'
        n = len(arr)
        for i in range(1, n):  # n-1轮
            tmp = arr[i]  # 该轮排序的那个关键元素
            j = i - 1  # 每轮起始的元素
            while j > -1 and arr[j] > tmp:  # 后移动元素
                arr[j + 1] = arr[j]
                j = j - 1
            arr[j + 1] = tmp
        return arr

    def insertionSort3(self, arr):

        # n-1轮
        n = len(arr)
        for i in range(1, n):
            current = arr[i]
            j = i - 1
            while j > -1 and arr[j] > current:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = current  # 注意
        return arr


solution = Solution()
arr = [12, 56, 92, -1, 5, 110, 92, 999, -39, 21, 76, 33, 56]
# print(solution.insertionSort(arr))
# print(solution.insertionSort2(arr))
print(solution.insertionSort3(arr))
# range:左开右闭
# for i in range(1,2):
#     print(i)

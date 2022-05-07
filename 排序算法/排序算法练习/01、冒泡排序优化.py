# -*- coding:utf-8 -*-
# 两两比较，交换
class Solution:
    def bubbleSort(self, arr):
        # write code here
        if not arr:
            return arr
        arr_len = len(arr)
        swapped = 0
        for i in range(0, arr_len - 1):# n-1
            for j in range(0, arr_len - 1 - i):# n-1,n-2,n-3 ... 1 = O(n*2)
                if arr[j] > arr[j + 1]: # 相邻比较：稳定排序
                    tmp = arr[j + 1]# 一个临时变量 O(1)
                    arr[j + 1] = arr[j]
                    arr[j] = tmp
                    swapped = 1
            if swapped ==0:
                break
        return arr


solution = Solution()
arr = [1, 2, 5, 3, 7]
print(solution.bubbleSort(arr))

# range:左开右闭
# for i in range(1,2):
#     print(i)
# TODO python交换

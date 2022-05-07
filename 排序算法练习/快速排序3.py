def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


# 递归函数
def quickSortHelper(alist, first, last):  # 空间复杂度。递归，n或这log n
    # 递归结束条件
    if first < last:
        pi = partition(alist, first, last)
        quickSortHelper(alist, first, pi - 1)
        quickSortHelper(alist, pi + 1, last)


# 找mid元素的索引
def partition(alist, first, last):
    mid = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        # 找mid的应该在的索引
        while leftmark <= rightmark and alist[leftmark] <= mid:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= mid:
            rightmark -= 1
        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark


alist = [52, 312, 54, 54, 7, 3, 2]
quickSort(alist)
print(alist)

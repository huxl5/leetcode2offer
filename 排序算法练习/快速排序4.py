def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    if first < last:
        pi = find_mid(alist, first, last)
        quick_sort_helper(alist, first, pi - 1)
        quick_sort_helper(alist, pi + 1, last)


def find_mid(alist, first, last):
    mid = alist[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= mid:
            left_mark += 1
        while right_mark >= left_mark and alist[right_mark] >= mid:
            right_mark -= 1
        if left_mark > right_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
    alist[first], alist[right_mark] = alist[right_mark], alist[first]
    return right_mark


alist = [52, 312, 54, 54, 7, 3, 2]
quick_sort(alist)
print(alist)

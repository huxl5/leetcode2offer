def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[0:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


def merge(left, right):
    j = h = 0
    c = []
    while j < len(left) and h < len(right):
        if left[j] <= right[h]:  # TODO<=才能稳定
            c.append(left[j])
            j += 1
        else:
            c.append(right[h])
            h += 1
    if j == len(left):
        c += right[h:]
    if h == len(right):
        c += left[j:]
    return c


a = [52, 312, 54, 54, 7, 3, 2]
print(merge_sort(a))

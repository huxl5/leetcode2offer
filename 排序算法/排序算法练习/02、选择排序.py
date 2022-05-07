class Solution:
    def selectionSort(self, arr):
        # write code here
        if not arr:
            return arr
        len_arr = len(arr)
        for i in range(0,len_arr-1):# n-1 轮
            min_index = i
            for j in range(i+1,len_arr):
                if arr[j]<arr[min_index]:
                    min_index = j
            tmp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = tmp
        return arr



test = Solution()
arr = [1,2,6,3,5]
print(test.selectionSort(arr))
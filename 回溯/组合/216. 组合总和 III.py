#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/25 6:53 下午 
# @Author : huxiaoliang
# @description :
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。
# 示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]
#
# 示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]
class Solution:
    def combinationSum3(self, k: int, n: int):
        result = []
        path = []
        tmp_sum = 0 # 需要传入,否则需要tmp_sum= [0] ???
        def backtrack(k,n,start_index,tmp_sum):
            if tmp_sum>n:
                return
            if len(path)==k:
                if tmp_sum==n:
                    result.append(path[:]) # 只能放值,不能放索引
                return
            # for i in range(start_index,10):
            for i in range(start_index,9-(k-len(path))+1+1): # 剪枝:9-(k-len(path))+1+1
                path.append(i)
                tmp_sum += i
                backtrack(k,n,i+1,tmp_sum)
                path.pop()
                tmp_sum -= i
        backtrack(k,n,1,tmp_sum)
        return result

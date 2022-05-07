#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/25 7:47 下午 
# @Author : huxiaoliang
# @description :
class Solution:

    def __init__(self):
        self.results=[]
        self.result=''
        self.letter_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

    def letterCombinations(self, digits: str):
        if not digits:
            return self.results

        def backtrack(digits,start_index): # start_index 指向递归的深度
            if start_index == len(digits): # 递归出口
                self.results.append(self.result)
                return
            letters = self.letter_map[digits[start_index]]
            for letter in letters: # 每一层的选择
                self.result = self.result+letter # 处理
                backtrack(digits,start_index+1) # 递归
                self.result = self.result[:-1] # 撤销处理,即回溯
        backtrack(digits,0)
        return self.results
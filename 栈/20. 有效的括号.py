#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 12:49 
# @Author : Eden.hu
# @description :
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 ==1:
            return False
        valid_dict = {")":"(","]":"[","}":"{"}
        # 匹配左括号时，后进先出，栈只放左括号
        stack = []
        for ch in s:
            if ch not in valid_dict:
                stack.append(ch)
            else:
                if not stack or valid_dict[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack
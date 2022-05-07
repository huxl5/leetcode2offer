#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/26 11:49 上午 
# @Author : huxiaoliang
# @description :
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。
#
# 示例 1：
#
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 示例 2：
#
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 示例 3：
#
# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 示例 4：
#
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
# 示例 5：
#
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# 提示：
#
# 0 <= s.length <= 3000
# s 仅由数字组成
class Solution:
    def restoreIpAddresses(self, s: str):
        vaid_num = [str(i) for i in range(10)]
        def is_valid(s):
            if not s:
                return False
            if len(s)>4:
                return False
            for s_s in s:
                if s_s not in vaid_num:
                    return False
            if s.startswith('0') and len(s)>1:
                return False
            if not 0<=int(s)<=255:
                return False
            return True

        if len(s)>12 and len(s)<4:
            return False
        paths = []
        path =  []
        k = 0 # 几段

        def backtrack(s,start_index,k):
            # 递归出口 切三次,且最后一个串满足要求即可
            if k == 3:
                if is_valid(s[start_index:]):
                    paths.append('.'.join(str(i) for i in path)+'.'+s[start_index:])
                return
            # 遍历所有切割位置
            for i in range(start_index,len(s)+1):
                # 处理结果
                if k>3: # 剪枝
                    return
                temp_s = s[start_index:i+1]
                if not is_valid(temp_s):
                    continue
                path.append(temp_s)
                # 递归,深度
                backtrack(s,i+1,k+1)
                # 回溯,撤销结果处理
                path.pop()
        backtrack(s,0,k)
        return paths


class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        本质切割问题使用回溯搜索法，本题只能切割三次，所以纵向递归总共四层
        因为不能重复分割，所以需要start_index来记录下一层递归分割的起始位置
        添加变量point_num来记录逗号的数量[0,3]
        '''
        self.result.clear()
        if len(s) > 12: return []
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s: str, start_index: int, point_num: int) -> None:
        # Base Case
        if point_num == 3:
            if self.is_valid(s, start_index, len(s) - 1):
                self.result.append(s[:])
            return
        # 单层递归逻辑
        for i in range(start_index, len(s)):
            # [start_index, i]就是被截取的子串
            if self.is_valid(s, start_index, i):
                s = s[:i + 1] + '.' + s[i + 1:]
                self.backtracking(s, i + 2, point_num + 1)  # 在填入.后，下一子串起始后移2位
                s = s[:i + 1] + s[i + 2:]  # 回溯
            else:
                # 若当前被截取的子串大于255或者大于三位数，直接结束本层循环
                break

    def is_valid(self, s: str, start: int, end: int) -> bool:
        if start > end: return False
        # 若数字是0开头，不合法
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start:end + 1]) <= 255:
            return False
        return True



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/30 11:14 
# @Author : Eden.hu
# @description :


# 动态规划
def bag_problem(bag_size, weight, value):
    # dp[i][j]:0-i的物品，随意选取，放入容量为j的背包的最大价值
    dp = [[0]*(bag_size+1) for _ in range(len(weight))]
    for j in range(weight[0],bag_size+1):
        dp[0][j] =value[0]
    for i in range(1,len(weight)):
        for j in range(1,bag_size+1):
            if weight[i]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
    return dp

# 动态规划：滚动数组问题
def bag_problem_2(bag_size, weight, value):
    # dp[j]:容量为j的背包的最大价值
    dp = [0]*(bag_size+1)
    for i in range(len(weight)):
        for j in range(bag_size,weight[i]-1,-1): # 从第0个物品开始，计算dp数组，dp[j]从容量大迭代
            dp[j] = max(dp[j],dp[j-weight[i]]+value[i])
    return dp

bag_size = 4
weight = [1, 3, 4]
value = [15, 20, 30]
print(bag_problem(bag_size, weight, value))
print(bag_problem_2(bag_size, weight, value))


def canPartition(nums):
    # 找出一组元素和为sum/2
    target = sum(nums)
    if target % 2 == 1:
        return False
    target = target >> 1
    dp = [[0] * (target + 1) for _ in range(len(nums))]
    # 初始化
    for j in range(nums[0], target + 1):
        dp[0][j] = nums[0]

    for i in range(1, len(nums)):
        for j in range(1, target + 1):
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])

    return dp[-1][target] == target


print(canPartition([1,2,5]))
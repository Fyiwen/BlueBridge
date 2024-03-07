import os
import sys

# 请在此输入您的代码
n = int(input()) # 数列长度
l1 = list(map(int,input().split())) # 数列里面每一个元素
dp = [1]*n # 元素i存储：以i为末尾元素的递增序列的最大长度
for i in range(1,n):# 从数列的第二个元素遍历到最后一个
    if l1[i]>l1[i-1]: #元素i大于前面一个元素，满足递增
        dp[i] = dp[i-1]+dp[i]

print(max(dp)) # 得到最长递增序列的长度


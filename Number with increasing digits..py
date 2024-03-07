import os
import sys

# 请在此输入您的代码
n=int(input())

count=0# 记录数位递增的数的个数
for i in range(1,n): # 遍历1-n之间的每个数字
    a=list(str(i)) # 数字转成字符串之后存在数组里
    if a==sorted(a): # 如果当前数是数位递增，那么对这个数进行递增排序后的结果应该对原来的字符顺序不会产生影响
        count+=1
print(count)
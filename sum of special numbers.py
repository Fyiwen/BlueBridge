import os
import sys

# 请在此输入您的代码
n=int(input())

sum = 0
for i in range(1, n + 1): # 遍历从1--n的每个数字
    for j in str(i): # 遍历当前数字中的每一个字符
        if j in '2019': # 判断这个字符是否是2019这四个中的一个
            sum += i # 一旦满足要求他就要参与求和
            break # 为了不重复叠加一旦成功就要中止这个操作
            
print(sum)
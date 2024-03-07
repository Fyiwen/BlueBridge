import os
import sys

# 请在此输入您的代码
n, m = map(int, input().split()) # 输入图片的行和列

a = []
for i in range(n): # 元素放进矩阵里
    a.append(list(map(int, input().split()))) # a是n*m的矩阵

b = [[0]*n for i in range(m)]           #创建一个旋转之后m*n的矩阵，初始化

for i in range(n):
    for j in range(m):
        b[j][n-i-1] = a[i][j]                #找规律把值填入旋转之后的矩阵

for i in b:   #按顺序读取b的一行 ，可以说按照b的第一维遍历                                 #打印结果
    for j in i: # 按顺序读取行中的每一个元素
        print(j, end=' ') # 输出一个元素和一个空格
    print()
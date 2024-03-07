import os
import sys

# 请在此输入您的代码
m,n = map(int,input("请输入笔画的宽度和X的高度").split())

lis = [['.'] * (m+n-1) for _ in range(n)] # 初始化一个二维数组n行，m+n-1列

for i in range(n): # 更改二维数组，实则是准备需要打印的X的过程，把数组矩阵里面默认的元素替换掉
  for j in range(m):
    lis[i][i+j] = '*'
    lis[i][m+n-2-i-j] = '*'

for k in lis: # 打印结果，这个lis数组里面顺序存储的就是
    for k1 in k:
      print(k1,end='')
    print('\n')
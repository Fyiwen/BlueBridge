import os
import sys

# 请在此输入您的代码
n=int(input("请输入一个整数"))
count=0

for i in range (1,n+1):
  if "2" not in str(i): # 整数转换成字符串，然后直接判断是否包含字符2
    count+=1

print(count)

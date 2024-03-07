import os
import sys

# 请在此输入您的代码
n=input("输入1个数字")

def zhuwei(n): # 用于逐位求和的函数
  num=0
  for i in range(len(n)):# 用于逐位求和的循环
    num+=int(n[i])

  s=str(num) # 将整数字符串化
  if(len(s)>1): # 一旦这是个二位以上的整数，需要继续进行逐位求和
    return  zhuwei(s)
  else:
    return num

ans=zhuwei(n)
print(ans)
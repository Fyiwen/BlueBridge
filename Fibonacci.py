import os
import sys

# 请在此输入您的代码
N=int(input())

def Fibo(N):
  if(N==1 or N==2):
    return 1
  else:
    return(Fibo(N-1)+Fibo(N-2))

if(N>20):
  print("0.61803399") # 因为只保留8位小数，算计可以发现n大于20的情况下，除法的结果一样。如果没有这一步，计算会超时
else:
  ans=1.0*Fibo(N)/Fibo(N+1) # 转换成浮点数，确保小数部分的准确性
  
  print("%.8f"%ans) #保留八位小数


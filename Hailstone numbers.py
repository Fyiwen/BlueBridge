import os
import sys

# 请在此输入您的代码
# 模拟这个循环往复的过程，然后几下其中的最大数
N=int(input())
h=N # h用于记录往复过程中出现的最大数字

for i in range(2,N+1):
    m=i
    while(m!=1):
      if(m%2==0):
        m=m//2
      else:
        m=m*3+1
        h=max(m,h)
      if(m<i): # 可以提前结束的语句，节省时间.因为比i小的数字，在前面循环里判断过
        break

print(h)

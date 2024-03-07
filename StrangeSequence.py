import os
import sys

def change(s):
  count=1 # 记录相邻且相同的字符个数
  s_n='' # 存储下一行变换后的字符串

  for i in range(len(s)-1):
    if(s[i]==s[i+1]):
      count+=1
    else:
      s_n=s_n+str(count)+s[i]
      count=1
  s_n += str(count) + s[-1]
  return s_n

# 请在此输入您的代码
if __name__=='__main__':
  s=input("请输入一个初始字符串")
  n=int(input("需要连续变换多少次"))
  for _ in range(n):
    s=change(s) # 按照要求变换
  print(s)

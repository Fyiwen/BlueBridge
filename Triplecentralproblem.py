import os
import sys

# 请在此输入您的代码

n=int(input("请输入数组长度"))
a=list(map(int,input("请用空格分隔输入每个数组元素").split()))

count=0 # 记录三元组中心数量

for i in range(1,n-1): # 从头遍历数组元素，第一个元素没有考虑（第一个元素毫无意义）
  ai=min(a[0:i]) # 在当前元素之前的所有元素中最小值
  aj=a[i] # 当前元素
  ak=max(a[i+1:]) # 在当前元素之后的所有元素中最大值
  if ai<aj and aj<ak: # 因为满足递增条件，所以当前元素可以是三元组中心
    count+=1

print(count)
# 请在此输入您的代码
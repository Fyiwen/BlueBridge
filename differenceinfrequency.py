import os
import sys

# 请在此输入您的代码
s=input("请输入获胜情况")
a=[]
for i in s: # 遍历字符串s里面的每一个字符
  a.append(s.count(i)) # 计算字符i在s中出现的次数存在数组a中，虽然这里的循环会导致同一个元素的出现次数呗重复存储，但是这个并不影响结果

print(max(a)-min(a)) # 得到最多获胜次数和最少之间的差值
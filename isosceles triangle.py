import os
import sys

# 请在此输入您的代码
n = int(input("请输入等腰三角形的高度"))
s = '0'

for i in range(1, 10000):
    s += str(i)   # s是用于围出这个等腰三角形的字符串

# print(s)
print("." * (n - 1) + s[1]) #根据观察，找到规律这个三角形的第一行必是n-1个点再跟个1

for j in range(2, n): # 根据观察，三角形的第二行开始到倒数第二行都满足这个性质
    a = ''
    a += '.' * (n - j) + s[j] + "." * (2 * j - 3) + s[4 * n - j - 2]
    print(a)

print(s[n:3*n-1]) # 根据观察，等腰三角形的最后一行必是这些字符
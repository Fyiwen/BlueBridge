import os
import sys
from math import sqrt

def f(n):
  am = int(sqrt(n))
  # 经过下面三个循环可以穷举得到三个满足条件的平方数，第四个循环数靠算出来
  for a in range(am+1):  # 平方数a必然小于根号n
    bm = int(sqrt(n-a*a))
    for b in range(a, bm+1): # 平方数b，必然小于根号下n-a^2,必然大于a
      cm = int(sqrt(n-a*a-b*b))
      for c in range(b, cm+1): # 平方数c，必然小于根号下n-a^2-b^2，必然大于b
        t = n - a*a-b*b-c*c  # d*2
        d = int(sqrt(t))
        if d >= c and a*a+b*b+c*c+d*d==n: # 平方数d，必大于c，满足四平方和
          print(a,b,c,d)
          return 

n = int(input())
f(n)
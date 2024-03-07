import os
import sys

n,m=map(int,input("请给出螺旋矩阵的行和列").split()) 
r,c=map(int,input("请给出要求的行号和列号").split())
ans=[[0]*m for i in range(n)] # ans是二元数组，一维表示行，二维表示列
#初始化当前坐标
x,y=0,0
#当前坐标存放的值
value=1

ans[x][y]=value

# 模拟螺旋矩阵产生的这个过程
while value<n*m: # 因为n*m-1是这个螺旋矩阵中可能出现的最大元素
    #先一直往右走（只要右边能走且没有走过）
    while y+1<m and ans[x][y+1]==0:
        value+=1
        y+=1
        ans[x][y]=value
    #再一直往下走（只要下面能走且没有走过）
    while x+1<n and ans[x+1][y]==0:
        value+=1
        x+=1
        ans[x][y]=value
    #再一直往左走（只要左边能走且没有走过）
    while y-1>=0 and ans[x][y-1]==0:
        value+=1
        y-=1
        ans[x][y]=value
    #再一直往上走（只要上面能走且没有走过）
    while x-1>=0 and ans[x-1][y]==0:
        value+=1
        x-=1
        ans[x][y]=value
    #这一圈走下来，矩阵没有填满，那么开启新的一层里圈，继续按照这个顺序填数字
print(ans[r-1][c-1]) # 输出指定位置的元素
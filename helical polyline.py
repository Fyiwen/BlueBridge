
import os
import sys

# 请在此输入您的代码
#x,y=map(int,input().split())
#n=max(abs(x),abs(y))
#if x==-n or y==n:
 #   t=n*(n*4-2)+x+y
#elif x==n or y==-n:
#    t=n*(n*4+2)-x-y
#print(t)
import os
import sys

# 请在此输入您的代码
x1,y1=map(int,input("请输入整数坐标位置").split(" "))

#判断是哪一种类型
def judge_1(x,y):
    if x<0 and y==0:
        return 1
    elif x==0 and y>0:
        return 2
    elif x>0 and y==0:
        return 3
    elif x==0 and y<0:
        return 4

#判断该点的a相对于参考点b的位置
def judge_2(a,b,type):
    if type==1 or type==2:   #(负数，0)，比较y
        if a>b:  #在参考点的上方,路径要加上
            return abs(a)
        else:    #在参考点下方，路径要减去
            return abs(a)*(-1)
    elif type==3 or type==4:
        if a > b:  # 在参考点的上方,路径要减去
            return abs(a)*(-1)
        else:  # 在参考点下方，路径要加上
            return abs(a)

ans=0 # 记录要查询的整数坐标，按螺旋路线走距离原点的距离

#首先先找他的对照点
if x1==0 and y1==0:   #如果是原点
    ans=0
else:
    n1,n2=x1,y1   #创造一个副本
    # 找绝对值基准大的，比如（3，2）会找（3，0）为基准
    # (-2,-1),找(-2,0)为基准
    if abs(n2)>=abs(n1): #所以取绝对值，如果y坐标的绝对值更大，那么基准坐标按照y找
        a=judge_1(0,n2)
    else: # 否则基准坐标按照x找
        a=judge_1(n1,0)
        
    m=max(abs(n1),abs(n2))
    step,r=0,0
    if a==1:
        step=m*(4*m-3)
        r=judge_2(y1,0,a)    #只用比y
    elif a==2:
        step=m*(4*m-1)
        r=judge_2(x1,0,a)
    elif a==3:
        step=m*(4*m+1)
        r = judge_2(y1, 0, a)
    elif a==4:
        step=m*(4*m+3)
        r = judge_2(x1, 0, a)
    # print(a,step,r)
    ans=step+r
print(ans)
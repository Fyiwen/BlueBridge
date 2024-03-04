import os
import sys

#N=int(input("请输入数列的长度"))#输入的是字符串所以需要转换
#K=int(input("请输入K倍区间的K值"))
#上面这样写是的输入在两行中给出，不符合题目要求
N, K = map(int, input().split())
count=0
a=[]
for _ in range(N):
  value=int(input("请依次输入数列元素"))
  a.append(value)
for i in range(N):
   if(a[i]%K==0):  # 判断整数也可以 用 B.is_integer()
     count=count+1
   A=a[i] 
   for j in range (i+1,N):
     A=A+a[j]
     if(A%K==0):
       count=count+1

print(count)


##############虽然对但是是超时方法##############
import sys

n, k = map(int, sys.stdin.readline().split())

a = [0] #存储前缀和
# 任意区间的值 % k == 0
# 即 a[x] - a[y] % k == 0 (x, y+1)
# 即 a[x] % k  == a[y] % k
# 所以只需要寻找每一个前缀和与其前面的值模 k 相等的值即可
# 其中，a[0] = 0, dp[0] = 1。
# 这样考虑了单个前缀和构成区间的情况。
dp = {0: 1}

ans = 0
for i in range(1, n+1): # 循环计算前缀和
    a.append(a[i-1]+int(sys.stdin.readline())) # a[i]表示的前缀和=a[i-1]+当前元素i

    amod = a[i] % k
    ans += dp.get(amod, 0) # amod作为key若在字典dp中能查询到会返回对应value，查不到就会返回默认值0。也就是只有 a[i] % k为整数或者与前面的前缀的模相同，次数才会加一
    dp[amod] = dp.get(amod, 0) + 1 # 更新字典，在对应key为amod的地方，value加1
print(ans)
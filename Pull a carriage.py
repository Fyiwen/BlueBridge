import os
import sys

# 请在此输入您的代码
A = list(input()) # 输入A方手中的牌
B = list(input()) # 输入B方手中的牌
table = []

def put_card(a,b):
  global table
  if not a: # a的手里没有牌了
    return b #牌都在b手上，所以返回b这个赢家手里所有的牌
  if not b:
    return a

  card = a[0]
  table.append(a[0]) #记录打出去的在桌子上的牌
  a.pop(0) # 出栈，表征当前出牌人当前的第一张手牌出出去了
  temp = []
  if table.count(card) > 1:#当前在出牌的这个人赢牌
    idx = table.index(card) # 获得与当前出的这张牌一样的那种古早牌所在的位置
    temp = table[idx:] # 鼓噪对应牌之后的所有牌都需要拿出来归赢方
    table = table[:idx] # 桌上的牌变少
    a.extend(temp[::-1]) # 赢者手里的牌变多
    return put_card(a,b) # 赢者继续出牌
  else:
    return put_card(b,a) # 轮到另一个人出牌


rs = put_card(A,B)
print(''.join(rs)) # 将列表 rs 中的所有元素通过（空）连接成一个字符串，并将该字符串打印输出
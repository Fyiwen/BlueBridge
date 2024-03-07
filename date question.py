import os
import sys

# 请在此输入您的代码
import datetime
date = input() # 输入时间字符串

Date = datetime.datetime

fmt = ["%y/%m/%d","%m/%d/%y","%d/%m/%y"] # 三种可能出现的不同日期格式

d = []
for i in fmt: # 遍历三种格式
  try:
    _date = Date.strptime(date,i) # 尝试日期是否可以按照当前格式被解析
    if(_date.year>2059): # 如果解析后的时间超过2059那么需要调整成19
      _date = _date.replace(year = 1900 + _date.year%100)
    if(_date not in d): # 如果这个日期形式还没出现过，那么可以存在数组里作为输出（防止重复的结果）
      d.append(_date)
  except Exception as e:# 如果不能解析，就触发异常直接跳过
    pass
d.sort() # 将数组内的日期排序，因为输出的时候要求有序

for i  in d:
  print(Date.strftime(i,"%Y-%m-%d"))
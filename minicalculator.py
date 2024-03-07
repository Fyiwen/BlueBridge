import os
import sys



def toans(x, k): # 用作进制转换的函数，x是要转换的十进制数，k是目标进制
    if x == 0:
        return '0' # 0在任何进制下都是0
    s = ''#用于保存进制转换后的结果
    while x:
        tm = x % k
        if tm <= 9: #tm是0-9的数字，可以直接转换成字符串
            s = str(tm) + s # 字符串连接
        else: # 10以上的数字需要转换成字母
            s = chr(ord('A') + tm - 10) + s #ord('A') 的值为65，因此可以通过 ord('A') + tm - 10 来得到对应的字母的 ASCII 值，然后利用chr再将其转换为字符
        x //= k
    return s


def toten(s, k): # 为了方便计算，需要将任意进制的操作数转换成十进制形式。s是要转换的进制数，k对应他的进制
    ans = 0 # 最后的十进制结果
    arg = 1 # 权重值
    for i in range(len(s) - 1, -1, -1): # 反向遍历字符串
        if s[i] <= '9':
            ans += (int(s[i]) * arg)
        else:
            ans += ((ord(s[i]) - ord('A') + 10) * arg)
        arg *= k # 每一轮转换后，权重值都增加，因为要算更前的一位数
    return ans


def getop(a, b, op): # 对十进制数的计算
    if op == 'ADD':
        return a + b
    elif op == 'SUB':
        return a - b
    elif op == 'MUL':
        return a * b
    elif op == 'DIV':
        return a // b
    else:
        return a % b

if __name__=='__main__':

    n=int(input("请给出指令数量"))
    ans = 0
    k = 10
    op = ''
    for _ in range(n):
        s = input() # 获取当前行输入的字符串
        if s == 'CLEAR':# # 输入的是清空指令，把当前保存的数字和操作符都清空
            s = ''
            op = ''
        elif s == 'EQUAL': # # 输入的是输出指令，以当前进制输出结果
            op = ''
            print(toans(ans, k))
        elif s[:6] == 'CHANGE':# 进制转换指令
            k = int(s[7:])# 当前进制需要转换成k进制
        elif s[:3] == 'NUM' and op == '':# 操作符之前的数字
            ans = toten(s[4:], k)
        elif s[:3] == 'NUM' and op != '':# 操作符之后的数字
            ans = getop(ans, toten(s[4:], k), op)
        else: # 运算指令
            op = s
dp = [0 for i in range(int(1e5 + 50))]
a = []
W = 0
N = 0

# cur0是当前行的宽度，cur1是当前行的高度
def add(cur, k):  # 以cur标识当前行状态，在此状态基础上加入k号图片，并更改cur状态
    if cur[0] + a[k][0] <= W:  # 当前行已有的宽度加上这个新图片宽度，没有超过限制
        cur[0] += a[k][0] # 记录的当前行宽度增加
        cur[1] = max(cur[1], a[k][1]) # 更新当前行高度
    else:  # 超过限制，当前行不能再加入图片
        w = W - cur[0]  # 剩余宽度
        cur[0] = W
        cur[1] = max(cur[1], (w * a[k][1] + a[k][0] - 1) // a[k][0])  # 考虑在当前行剩余空间内添加图片可能会导致的高度变化
    return


def getdp(cur, k):  #计算在给定当前行状态 cur 的情况下，加入第 k张图片及其后所有图片的总高度
    while k < N and cur[0] < W: # 不超过图片总数且当前行的宽度还没超过
        add(cur, k) # 不断向当前行添加图片，直到超过while的限制
        k += 1
    return cur[1]+dp[k]   # 当前行高度(已经填满)，从第 k 号图片开始的最小总高度


if __name__ == '__main__':
    W, N = map(int, input("输入纸张宽度和图像总数").strip().split()) # 读取一行，清理输入，按照空格分离字符串

    for i in range(N):
        a.append(list(map(int, input("输入每张图像的宽和高").strip().split())))# 二元数组，第一维标识是哪张图片，第二维0为w，1为h。

    for i in range(N - 1, -1, -1):  # 执行反向遍历
        tmp = [0, 0]
        dp[i] = getdp(tmp, i)
# dpi存储从第i张图片到最后一张图片排放好的最小总高
    ans = 999999
    h = 0  # h：前i-1张图片已经排好的各行的累计高度
    cur = [0, 0]
    for i in range(N):  # 循环尝试计算，去掉第i张图片后的总高度，得到最低总高
        ans = min(ans, h + getdp(cur[:], i + 1))  # 前i-1张图片已经排好的各行的累计高度+把从第i+1张图片之后的图片都加入排列能得到的总高度
        add(cur, i) # 更新当前行信息，便于下一次循环
        if cur[0] == W:  # 当前行已填满，另起一行
            h += cur[1] #更新目前累计的行高
            cur = [0, 0] # 开始下一行，这一行的信息是初始的

    print(ans)
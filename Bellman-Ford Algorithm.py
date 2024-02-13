import numpy as np

n, m = map(int, input().split(' '))

dis = np.zeros(10, dtype=np.int)
bak = np.zeros(10, dtype=np.int)

u = np.zeros(10, dtype=np.int)
v = np.zeros(10, dtype=np.int)
w = np.zeros(10, dtype=np.int)
inf = 99999999

# 讀入邊
for i in range(1, m+1):
    u[i], v[i], w[i] = map(int, input().split(' '))

# 初始化 dis 陣列，此處用 1 號頂點到其餘各點的初始路程
for i in range(1, n+1):
    dis[i] = inf
dis[1] = 0

# Bellman-Ford Algorithm
for k in range(1, n):
    # 將 dis 陣列備份到 bak 陣列中
    for i in range(1, n+1):
        bak[i] = dis[i]
    # 進行一輪鬆弛
    for i in range(1, m+1):
        if dis[v[i]] > dis[u[i]] + w[i] :
            dis[v[i]] = dis[u[i]] + w[i]
    # 鬆弛完畢檢測 dis 陣列有無更新
    check = 0
    for i in range(1, n+1):
        if bak[i] != dis[i]:
            check = 1
            break
    # 如果 dis 陣列沒有更新，提前退出演算法迴圈
    if check == 0:
        break

# 檢測負權迴路
flag = 0
for i in range(1, m+1):
    if dis[v[i]] > dis[u[i]] + w[i]:
        flag = 1
if flag == 1 :
    print("此圖含有負權迴路")
else:
    # 輸出最終結果
    for i in range(1, n+1):
        print(dis[i])

'''
5 5
2 3 2
1 2 -3
1 5 5
4 5 2
3 4 3
'''

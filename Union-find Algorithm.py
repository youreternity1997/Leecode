# people = 人數; leads = 線索數
people, leads = map(int, input().split(' '))

# 初始化每個人的編號
f = []
for i in range(people):
    f.append(i)

# 「擒賊先擒王原則」，不斷的找，找到小團體裡面的頭為止。
def getf(f, v):
    if f[v] == v:
        return v
    else:
        # 路徑壓縮 (path compression)，每次在函數返回的時候，
        # 順道把路上遇到的「頭頭」改為最後找到的「大頭編號」，也就是小團體的主要人物。
        # 這樣可以提高以後找主要人物的速度。
        f[v] = getf(f, f[v])
        return f[v]

# 合併兩個小團體的函數
def merge(f, v, u):
    t1 = getf(f, v)
    t2 = getf(f, u)
    if t1 != t2 : # 判斷兩位學生是否同屬一個小團體，及是否同一個頭頭。
        f[t2] = t1
        # 「靠左原則」，左邊變成右邊的頭頭。即把右邊的集合，變成左邊的子集合。
        # 經過路徑壓縮以後，將f[u]的根的值也指定為v的大頭f[t1]

'''
測試資料 (test data) :
10 9
1 2
3 4
5 2
4 6
2 6
8 7
9 7
1 6
2 4
'''

# 開始合併線索
for i in range(leads):
    clue1, clue2 = map(int, input().split(' '))
    merge(f, clue1, clue2)

# 掃描最後有幾個獨立的小團體
sum = 0
for j in range(people):
    if f[j] == j :
        sum += 1

print(sum)

'''
answer = 3
'''
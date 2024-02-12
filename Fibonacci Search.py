import sys

# 產生費氏數列
def fibo(max):
    fib = [sys.maxsize] * max
    fib[0] = 0
    fib[1] = 1
    for i in range(2, max):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

def getY(fib, n):
    i = 0
    while fib[i] <= n:
        i += 1
    return i - 1

def search(data, key):
    fib = fibo(len(data))
    max = len(data) - 1  # data的最大索引值
    y = getY(fib, max + 1) # 在費氏數列裡的值，如果比data的最大索引值()還大，回傳費氏數列索引值的前一個
    m = max - fib[y] 
    x = y - 1  #找到在data搜尋的起始索引值
    print("\nx=%d, m=%d, fib[x]=%d" % (x, m, fib[x]))
    i = x
    if data[i] < key:
        i += m
    while fib[x] > 0:
        if data[i] < key:
            x -= 1
            i += fib[x]
        elif data[i] > key:
            x -= 1
            i -= fib[x]
        else:
            return i
    return -1

number = [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130]
find = search(number, 60)
print("找到數值於索引 " + str(find) if find >= 0 else "找不到數值")

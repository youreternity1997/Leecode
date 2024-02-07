data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

# Radix sort
def radixsort(data):
    length = len(data)
    count = max(data) # 資料裡最大的數值

    # 用最大數來判斷最大位數
    digit = 1
    while count > 9:
        count /= 10
        digit += 1

    tmp = []
    cur = 0
    for i in range(length):    # 資料的大小會決定桶子的數量，會是一個二維陣列
        tmp.append([0] * length)
    order = [0] * length       # 游標行，用來將資料放到同一位數但不同列的桶子

    if digit <= 9:
        '''use LSD(Least significant digit) method '''
        n = 1
        while n <= max(data):
            for i in range(length):
                lsd = int(data[i]/n) % 10  # 將資料用10來取個位數的餘數
                tmp[lsd][order[lsd]] = data[i]
                order[lsd] += 1
            for i in range(length):
                # 如果這個位數的桶子在此行有資料，就丟到同一個位數，但下一列的位置
                if order[i] != 0:
                    for j in range(order[i]):
                        data[cur] = tmp[i][j]
                        cur += 1
                # 將游標行的資料歸零
                order[i] = 0
            n *= 10
            cur = 0
        print(data)
        
radixsort(data)

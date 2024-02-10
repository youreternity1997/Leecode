a = [] 
book = []
for i in range(10):
    a.append(0)     #設數字9+1個空盒子
    book.append(0)  #設數字9+1個空盒子，表示目前是否有使用此數字

total = 0 #代表可行解總共有幾種
def dfs(step, total, a, book):  #step代表目前的位置
    if step == 9:   #如果站在索引為9的盒子表示0~8共九個位置都已有待運算的數字
        if a[0]/(a[1]*10.+a[2]) + a[3]/(a[4]*10.+a[5]) + a[6]/(a[7]*10.+a[8]) == 1 : 
            total += 1  #如果滿足解，可行解+1
            print(a)
        return total    #返回之前的一步(最接近呼叫的地方)
    
    #站在地step位置，按照0~8的順序一一的嘗試
    for i in range(9):
        if book[i] == 0 :  #如果book[i]等於0，代表這個位置的數字可以用
            a[step] = i+1  #將可用數字給到空盒子裡(因為i為索引，所以要加1)
            book[i] = 1    #表示這個位置的數字已被取用

            total = dfs(step + 1, total, a, book) #藉由遞迴來找出更深層的解

            book[i] = 0    #但記得要把剛才嘗試過的數字重置，才能進行下一次的嘗試
    return total


total = dfs(0, total, a, book)
print(total/2)  #因為有重複解，所以要除以2
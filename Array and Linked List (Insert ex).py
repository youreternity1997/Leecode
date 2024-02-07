data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
right = []
insert_num = 41
length = len(data)
# Initialization
for i in range(length):
    right.append(0)

# 設定right來存放data中每一個節點右邊節點的位置
for i in range(length):
    if i != length-1:
        right[i] = i + 1
    else:
        right[i] = 0 # 0代表右邊沒節點

# data插入節點
data.append(insert_num)
right.append(0) # right增加位置給插入的節點存放右邊節點的位置資料
length = len(data)

# 從鏈結串列的頭部開始讀取
t = 0
for i in range(length):
    #如果目前節點的下一個節點值大於待插入的數字，將數插入到中間
    if data[right[t]] > data[length-1]: 
        #將目前節點的右邊位置給予新插入的節點存放在right
        right[length-1] = right[t]
        #將新插入節點的位置給到目前節點的right存放
        right[t] = length-1
        #跳出回圈
        break

    t = right[t]


#印出鏈結串列的所有數字
t = 0
tmp = []
for i in range(length):
    tmp.append(data[t])
    t = right[t]

print (tmp)
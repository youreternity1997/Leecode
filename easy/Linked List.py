# https://lovedrinkcafe.com/python-single-linked-list/
'''
Welcome to use my SingleLinkedList
The following line is the ouput of the SingleLinkedList
[1]1 --> [2]2 --> [3]3 --> [4]5
[index]: means the index of the node
And the following number/string of [index] is the data of the Node
'''
import os
class Node:
    def __init__(self ,data=None, next=None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        #要檢查item是否是一個結點，若不是的話則使用Node(item)建立一個帶有item資料的節點
        #if not isinstance(data, Node):
        new_node = Node(data)

        # 如果head == None 代表為第一個Node
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node #本來的tail指向新的節點
        self.tail = new_node #新加入的節點變成新的tail

    #重寫
    def delete(self):
        if self.head == None:
            return print("This list is empty")
        else:
            if len(self) == 1:
                self.head = None
            else:
                current_node = self.head
                while current_node.next != None:
                    self.tail = current_node
                    current_node = current_node.next
                self.tail.next = None



    # index: 第幾個node
    # data: 要新增的data
    def insert(self, index , data):
        '''
        To insert the data to the specific index
        '''
        if self.head == None:
            print("You can only insert the data to a not empty list")
        if not 1 <= index <= len(self):
            print("{} is not in range".format(index))

        elif index == 1:
            #圖8
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            #圖9
            cur_idx = 1
            new_node = Node(data)
            current_node = self.head
            while cur_idx+1 != index:
                current_node = current_node.next
                cur_idx += 1

            new_node.next = current_node.next #圖10
            current_node.next = new_node #圖11

    def delete_node_by_index(self, index):
        '''
        To delete the specific node
        '''
        if self.head == None:
            print("You can only delete the data from a not empty list")

        if index == 1 and len(self) > 1:
            self.head = self.head.next

        elif index == 1 and len(self) == 1:
            self.head = None
            self.tail = None

        elif 1 < index < len(self):
            cur_idx = 1
            current_node = self.head
            while cur_idx != index:
                previous_node = current_node
                current_node = current_node.next
                cur_idx += 1
            previous_node.next = current_node.next

        elif index == len(self):
            cur_idx = 1
            current_node = self.head
            while cur_idx != index:
                previous_node = current_node
                current_node = current_node.next
                cur_idx += 1
            previous_node.next = None
            self.tail = previous_node

        else:
            print("index out of range")

    def reverse(self):

        # reverse the order of the list
        previous_node = None
        current_node = self.head
        self.tail = current_node
        next_node = current_node.next

        while next_node is not None:
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next

        current_node.next = previous_node
        self.head = current_node
        return


    def __len__(self):
        length = 0
        current_node = self.head
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length

    def __str__(self):
        current_node = self.head
        chain = []
        index = 1
        while current_node != None:
            chain.append("["+str(index)+"]"+str(current_node.data))
            index += 1
            current_node = current_node.next
        return " --> ".join(chain)



def main():

    l = SingleLinkedList()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(__doc__)
        print(l)
        print("這個鏈結串列的長度為："+ str(len(l)))
        print("-"*20)
        opt = input("1. 加入資料\n2. 刪除資料\n3. 插入資料\n4. 刪除特定資料\n5. 反轉串列\n0. 結束程式\n 請輸入要使用的功能：")

        if opt == "1":
            data = input("請輸入要加入的資料：")
            l.append(data)
            print(l)

        elif opt == "2":
            l.delete()
            print(l)

        elif opt == "3":
            index = input("請輸入要插入的資料的index：")
            data = input("請輸入要插入的資料：")
            l.insert(int(index), data)
            print(l)

        elif opt == "4":
            index = int(input("請輸入要刪除的資料的index："))
            l.delete_node_by_index(int(index))
            print(l)

        elif opt == "5":
            l.reverse()
            print(l)

        elif opt == "0":
            print("The Final result is: {}".format(l))
            return False
        else:
            print("請輸入合法指令")


if __name__ == '__main__':
    #main()
    l = SingleLinkedList()
    l.append(2)
    print(l)
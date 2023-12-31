import os 
os.system('cls' if os.name == 'nt' else 'clear')

class ListNode:
    def __init__(self ,val=None, next=None):
        self.val = val
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        #要檢查item是否是一個結點，若不是的話則使用Node(item)建立一個帶有item資料的節點
        #if not isinstance(val, ListNode):
        new_node = ListNode(val)
        
        # 如果head == None 代表為第一個Node
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node #本來的tail指向新的節點
        self.tail = new_node #新加入的節點變成新的tail

    def __str__(self):
        current_node = self.head
        chain = []
        index = 1
        while current_node != None:
            chain.append("["+str(index)+"]"+str(current_node.val))
            index += 1
            current_node = current_node.next
        return " --> ".join(chain)
    

class Solution:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        print('l1.val=', l1.val)
        print('l2.val=', l2.val)
        
        val = l1.val + l2.val + c
        
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret

if __name__ == '__main__':
    #l1 = SingleLinkedList()
    #l1.append(2)
    #l1.append(4)
    #l1.append(3)
    #print(l1)
    
    #l2 = SingleLinkedList()
    #l2.append(5)
    #l2.append(6)
    #l2.append(4)
    #print(l2)
    l1 = ListNode([2,4,3])
    l2 = ListNode([5,6,4])
    
    ans = Solution().addTwoNumbers(l1, l2, c=0)
    print(ans)
    
#l1 = 
#l2 = 
#Solution.addTwoNumbers([2,4,3],[5,6,4])
#ListNode(9)
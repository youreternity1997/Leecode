// C++ code
#include <iostream>
using namespace std;

class SLLNode {
    int data; // 資料內容
    SLLNode *next; // 鏈結
};

class SLL {
private:
    SLLNode *head;
public:
    SLL();
    void pushFront(int);
    void printAll();
    int popFront();
    void pushBack(int);
};


void SLL::pushFront(int _data) {
    SLLNode *newNode = new SLLNode(_data);
    newNode -> next = this -> head;
    this -> head = newNode;
}

void SLL::printElement(SLLNode *head) {
    if (head == NULL) {
        std::cout << "NULL\n";
        return ;
    }
    std::cout << head -> data << " -> ";
    printElement(head -> next);
}

int SLL::popFront() {
    if (this -> head == NULL) 
        return -1;
    else if (this -> head -> next == NULL) {
        int removeElement = this -> head -> data; // 先儲存到變數中，因為未來無法再觸及該節點
        del this -> head; // 釋放動態記憶體
        this -> head = NULL; 
        return removeElement;
    }
    else {
        /*
            head 指向的記憶體在未來會被釋放，
            所以要先將這個節點的資料先取出，
            否則未來無法再觸及該節點
        */
        int removeElement = this -> head -> data;
        SLLNode *temp = this -> head -> next; 
        del this -> head;
        this -> head = temp;
        return removeElement;
    }
}
void SLL::pushBack(int _data)
{
    if (this -> head == NULL) // 鏈結串列為空
    {
        this -> head = new SLLNode(_data);
        this -> head -> next = NULL;
    }
    else 
    {
        SLLNode *cur = this -> head;
        while (cur && cur -> next != NULL) 
        {
            cur = cur -> next;
        }
        cur -> next = new SLLNode(_data);
    }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class DLLNode {
    int data; // 資料內容
    DLLNode *next, *prev; // 鏈結
};

class DLL {
private:
    DLLNode *head;
public:
    DLL();
    void pushFront(int);
    void printAll();
    int popFront();
    void pushBack(int);
};


void DLL::pushFront(int _data) {
    DLLNode *newNode = new DLLNode(_data);
    if (this -> head == NULL) {
        this -> head = newNode;
        this -> tail = newNode;
        return ;
    }
    this -> head -> prev = newNode;
    newNode -> next = this -> head;
    this -> head = newNode;
}
void DLL::printElement(DLLNode *head) {
    if (head == NULL) {
        std::cout << "NULL\n";
        return ;
    }
    std::cout << head -> data << " -> ";
    printElement(head -> next);
}

int DLL::popFront() {
    if (this -> head == NULL) 
        return -1;
    else if (this -> head -> next == NULL) {
        int removeElement = this -> head -> data; // 先儲存到變數中，因為未來無法再觸及該節點
        del this -> head; // 釋放動態記憶體
        this -> head = NULL;
        this -> tail = NULL;
        return removeElement;
    }
    else {
        /*
            head 指向的記憶體在未來會被釋放，
            所以要先將這個節點的資料先取出，
            否則未來無法再觸及該節點
        */
        int removeElement = this -> head -> data;
        DLLNode *temp = this -> head -> next;
        del this -> head;
        this -> head = temp;
        return removeElement;
    }
}
void DLL::pushBack(int _data)
{
    if (this -> tail == NULL)
    {
        this -> tail = new DLLNode(_data);
        this -> head = this -> tail;
    }
    else
    {
        this -> tail -> next = new DLLNode(_data);
        this -> tail -> next -> prev = this -> tail;
        this -> tail = this -> tail -> next;
    }
}


int main() {
    SLL *sll = new SLL;
    sll -> pushFront(5);
    DLL *dll = new DLL;
    dll -> pushFront(5);
}
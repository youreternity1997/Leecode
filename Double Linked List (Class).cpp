#include <iostream>
using namespace std;

class DLLNode {
public:
    int data; // 資料內容
    DLLNode *next, *prev; // 鏈結
    DLLNode(int _data) : data(_data), next(NULL), prev(NULL) {}; //In the DLLNode class, there's no constructor defined, but you're trying to create a new DLLNode object with data in the pushFront method. You need to add a constructor to initialize the data, next, and prev pointers.
};

class DLL {
private:
    DLLNode *head, *tail;
public:
    DLL() {
        this -> head = NULL;
        this -> tail = NULL;
    }
    void pushFront(int);
    void printAll();
    //void printElement();
    void printElement(DLLNode *);

    int popFront();
    void pushBack(int);
    int popBack();
    void insert(int);
    void remove(int);
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

/*
void DLL::printElement() {
    DLLNode *cur = this -> head;
    while (cur != NULL) {
        std::cout << cur->data << " -> ";
        cur = cur->next;
    }
    std::cout << "NULL\n";
}
*/

void DLL::printElement(DLLNode *head) {
    if (head == NULL) {
        std::cout << "NULL (printElement)\n";
        return ;
    }
    std::cout << head -> data << " -> ";
    printElement(head -> next);
}

void DLL::printAll() {
    printElement(this->head);
}

int DLL::popFront() {
    if (this -> head == NULL) 
        return -1;
    else if (this -> head -> next == NULL) {
        int removeElement = this -> head -> data; // 先儲存到變數中，因為未來無法再觸及該節點
        delete this -> head; // 釋放動態記憶體
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
        delete this -> head;
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

int DLL::popBack()
{
    if (this -> tail == NULL)
    {
        return -1;
    }
    int toBeReturn;
    if (this -> head == this -> tail)
    {
        toBeReturn = this -> head -> data;
        delete this -> head;
        this -> head = NULL;
        this -> tail = NULL;
    }
    else
    {
        DLLNode *tmp = this -> tail;
        this -> tail = this -> tail -> prev;
        this -> tail -> next = NULL;
    }
    return toBeReturn;
}

void DLL::insert(int _data) {
    if (this -> head == NULL) { // 鏈結串列為空
        this -> head = new DLLNode(_data);
        this -> tail = this -> head;
        return;
    }
    if (_data <= this -> head -> data) { // pushFront()
        DLLNode *newDLLNode = new DLLNode(_data);
        newDLLNode -> next = this -> head;
        this -> head -> prev = newDLLNode;
        this -> head = newDLLNode;
        return;
    }
    DLLNode *cur = this -> head;
    while (1)
    {
        if (cur -> next == NULL) { // pushBack()
            DLLNode *newDLLNode = new DLLNode(_data);
            cur -> next = newDLLNode;
            newDLLNode -> prev = cur;
            return;
        }
        else if (cur -> next -> data < _data)
            cur = cur -> next;
        else {
            DLLNode *newDLLNode = new DLLNode(_data);
            newDLLNode -> next = cur -> next;
            newDLLNode -> prev = cur;
            newDLLNode -> next -> prev = newDLLNode;
            cur -> next = newDLLNode;
            return;
        }
    }
}

void DLL::remove(int tg) {
    DLLNode *tmp;
    if (this -> head == NULL) { // 鏈結串列為空
        return ;
    }
    if (this -> head -> data == tg) { // 目標節點為鏈結串列第一個節點
        tmp = this -> head;
        this -> head = this -> head -> next;
        if (this -> head == NULL) { // 考慮鏈結串列是否為空
            this -> tail = NULL;
            delete tmp;
            return ;
        }
        delete tmp;
        this -> head -> prev = NULL;
        return ;
    }
    if (this -> tail -> data == tg) { // 目標節點為鏈結串列第一個節點
        tmp = this -> tail;
        this -> tail = this -> tail -> prev;
        if (this -> tail == NULL) { // 考慮鏈結串列是否為空
            this -> head = NULL;
            delete tmp;
            return ;
        }
        delete tmp;
        this -> tail -> next = NULL;
        return ;
    }
    DLLNode *cur = this -> head;
    while (cur) { // 目標節點在鏈結串列中間
        if (cur -> data == tg) {
            tmp = cur;
            cur -> prev -> next = cur -> next;
            cur -> next -> prev = tmp -> prev;
            delete tmp;
            return ;
        }
        else {
            cur = cur -> next;
        }
    }
    return ; // 目標節點不存在於鏈結串列中
}   

int main() {
    DLL *dll = new DLL;
    dll -> pushFront(1);
    dll -> pushFront(2);
    dll -> pushFront(3);
    dll -> pushFront(4);
    dll -> pushFront(5);
    dll -> printAll();

    dll -> popFront();
    dll -> printAll();

    dll -> pushBack(0);
    dll -> printAll();

    dll -> popBack();
    dll -> printAll();
    return 0;
}




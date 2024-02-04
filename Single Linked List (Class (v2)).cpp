#include <iostream>
using namespace std;

class SLLNode {
public:
    int data; // 資料內容
    SLLNode *next; // 鏈結
    SLLNode(int _data) : data(_data), next(NULL) {};
};

class SLL {
private:
    SLLNode *head;
public:
    SLL() {
        this -> head = NULL;
    }
    void pushFront(int);
    void printAll();
    //void printElement();
    void printElement(SLLNode *);

    int popFront();
    void pushBack(int);
    int popBack();
    void insert(int);
    void remove(int);
};

void SLL::pushFront(int _data) {
    SLLNode *newNode = new SLLNode(_data);
    newNode -> next = this -> head;
    this -> head = newNode;
}

/*
void SLL::printElement() {
    SLLNode *cur = this -> head;
    while (cur != NULL) {
        std::cout << cur->data << " -> ";
        cur = cur->next;
    }
    std::cout << "NULL\n";
}
*/

void SLL::printElement(SLLNode *head) {
    if (head == NULL) {
        std::cout << "NULL\n";
        return ;
    }
    std::cout << head -> data << " -> ";
    printElement(head -> next);
}

void SLL::printAll() {
    printElement(this->head);
}

int SLL::popFront() {
    if (this -> head == NULL) 
        return -1;
    else if (this -> head -> next == NULL) {
        int removeElement = this -> head -> data; // 先儲存到變數中，因為未來無法再觸及該節點
        delete this -> head; // 釋放動態記憶體
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
        delete this -> head;
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

int SLL::popBack()
{
    if (head == NULL) 
        return -1;
    int toBeReturn;
    if (head -> next == NULL)
    {
        toBeReturn = head -> data;
        delete head;
        head = NULL;
    }
    else
    {
        SLLNode *cur = head;
        SLLNode *prev;
        while (cur && cur -> next != NULL)
        {
            prev = cur;
            cur = cur -> next;
        }
        toBeReturn = cur -> data;
        delete cur;
        prev -> next = NULL;
    }
    return toBeReturn;
}

void SLL::insert(int _data) {
    if (this -> head == NULL) { // 鏈結串列為空
        this -> head = new SLLNode(_data);
        return;
    }
    if (_data <= this -> head -> data) { // pushFront()
        SLLNode *newSLLNode = new SLLNode(_data);
        newSLLNode -> next = this -> head;
        this -> head = newSLLNode;
        return;
    }
    SLLNode *cur = this -> head;
    while (1)
    {
        if (cur -> next == NULL) { // pushBack()
            SLLNode *newSLLNode = new SLLNode(_data);
            cur -> next = newSLLNode;
            return;
        }
        else if (cur -> next -> data < _data)
            cur = cur -> next;
        else {
            SLLNode *newSLLNode = new SLLNode(_data);
            newSLLNode -> next = cur -> next;
            cur -> next = newSLLNode;
            return;
        }
    }
}

void SLL::remove(int tg) {
    if (this -> head == NULL) 
        return ;
    if (this -> head -> data == tg) {
        SLLNode *tmp = this -> head;
        this -> head = this -> head -> next;
        delete tmp;
        return ;
    }
    SLLNode *cur = this -> head, *prev;
    while (cur) {
        if (cur -> data == tg) {
            prev -> next = cur -> next;
            delete cur;
            return ;
        }
        else {
            prev = cur;
            cur = cur -> next;
        }
    }
    return ;
}

int main() {
    SLL *sll = new SLL;
    sll -> pushFront(1);
    sll -> pushFront(2);
    sll -> pushFront(3);
    sll -> pushFront(4);
    sll -> pushFront(5);
    sll -> printAll();

    sll -> popFront();
    sll -> printAll();

    sll -> pushBack(0);
    sll -> printAll();

    sll -> popBack();
    sll -> printAll();
    return 0;
}





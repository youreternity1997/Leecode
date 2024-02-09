// C++ code
#include <iostream>
using namespace std;

class DLLNode {
public:
    int data; // 資料內容
    DLLNode *next, *prev; // 鏈結
    DLLNode(int _data) : data(_data), next(NULL), prev(NULL) {};
};

class DLL {
private:
    DLLNode *head, *tail;
public:
    DLL() {
        this->head = NULL;
        this->tail = NULL;
    }
    void pushFront(int);
    void printElement();
};


void DLL::pushFront(int _data) {
    DLLNode *newNode = new DLLNode(_data);
    if (this->head == NULL) {
        this->head = newNode;
        this->tail = newNode;
        return ;
    }
    this->head->prev = newNode;
    newNode->next = this->head;
    this->head = newNode;
}


void DLL::printElement() {
    DLLNode *cur = this -> head;
    while (cur != NULL) {
        std::cout << cur->data << " -> ";
        cur = cur->next;
    }
    std::cout << "NULL\n";
}


int main() {
    DLL *dll = new DLL;
    dll -> pushFront(1);
    dll -> pushFront(2);
    dll -> pushFront(3);
    dll -> pushFront(4);
    dll -> pushFront(5);
    dll->printElement();

    return 0;
}






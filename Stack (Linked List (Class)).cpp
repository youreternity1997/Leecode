// 將鏈結串列的 head 設為私有變數，以確保外人無法觸及
// 想要取得堆疊中的資料，唯有透過 getTop()
#include <iostream>
using namespace std;

class SLLNode {
public:
    int data; // 資料內容
    SLLNode *next; // 鏈結
    SLLNode(int _data) : data(_data), next(NULL) {};
};

class Stack
{
private:
    SLLNode *head;
public:
    Stack();
    bool isEmpty();
    void push(int); 
    int pop(); 
    int getTop();
    void printAll();
};
Stack::Stack() { this -> head = NULL; }

bool Stack::isEmpty() { return this -> head == NULL; }

void Stack::push(int _data) {
    if (this -> head == NULL)
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

int Stack::pop() {
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

void Stack::printAll(){
    SLLNode *cur = head;
    SLLNode *prev;
    if (cur==NULL){
        cout<< "Empty Stack"<< endl;
        return ;
    }
    cout<< "Stack : "; 
    while (cur) //&& cur -> next != NULL
    {
        cout<< cur->data << " -> ";
        prev = cur;
        cur = cur -> next;
    }
    cout<< "Null "<< endl;
    return ;
}


int main() {
    Stack *stack = new Stack;
    stack -> push(1);
    stack -> push(2);
    stack -> push(3);
    stack -> push(4);
    stack -> push(5);
    stack -> printAll();

    stack -> pop();
    stack -> printAll();
    
    stack -> push(6);
    stack -> printAll();

    return 0;
}

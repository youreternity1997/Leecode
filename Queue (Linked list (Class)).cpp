// 將鏈結串列的 head 設為私有變數，以確保外人無法觸及
// 想要取得堆疊中的資料，唯有透過 getFront()
#include <iostream>
using namespace std;

class SLLNode {
public:
    int data; // 資料內容
    SLLNode *next; // 鏈結
    SLLNode(int _data) : data(_data), next(NULL) {};
};

class Queue
{
private:
    SLLNode *head;
public:
    Queue();
    bool isEmpty();
    void enqueue(int); 
    int dequeue(); 
    void printAll();
    void Front();
};

Queue::Queue() { this -> head = NULL; }

bool Queue::isEmpty() { return this -> head == NULL; }

void Queue::enqueue(int _data) {
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

int Queue::dequeue() {
    if (head == NULL)
    {
        return -1;
    }
    int toBeReturn = head -> data;
    if (head -> next == NULL)
    {
        delete head;
        head = NULL;
        return toBeReturn; 
    }
    else 
    {
        SLLNode *tmp = head;
        head = tmp -> next;
        delete tmp;
        return toBeReturn; 
    }
}

void Queue::printAll(){
    if (head == NULL){
        cout<< "Empty Queue"<< endl;
        return ;
    }
    SLLNode *cur = this -> head;
    cout<< "Queue : "; 
    while (cur -> next != NULL) //&& cur -> next != NULL
    {
        cout<< cur -> data << " -> ";
        cur = cur -> next;
    }
    cout<< "Null "<< endl;
    return ;
}

void Queue::Front(){
    if (head == NULL){
        cout<< "Empty Queue"<< endl;
        return ;
    }
    else
        cout<< "Front : "<< head->data << endl;
        return ;
        
}


int main() {
    Queue *queue = new Queue;
    queue -> enqueue(1);
    queue -> enqueue(2);
    queue -> enqueue(3);
    queue -> enqueue(4);
    queue -> enqueue(5);
    queue -> printAll();
    queue -> Front();

    queue -> dequeue();
    queue -> printAll();

    queue -> dequeue();
    queue -> printAll();

    queue -> dequeue();
    queue -> printAll();

    return 0;
}



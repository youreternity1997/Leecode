// C++ code
#include <iostream>

struct QueueNode{
    int data;
    QueueNode *next;
    QueueNode():data(0),next(0){};
    QueueNode(int x):data(x),next(0){};
};

class QueueList{
private:
    QueueNode *front;
    QueueNode *rear;
    int size;
public:
    QueueList():front(0),rear(0),size(0){};
    void enqueue(int x);
    void dequeue();
    bool IsEmpty();
    int getFront();
    int getBack();
    int getSize();
};

void QueueList::enqueue(int x){

    if (IsEmpty()) {
        front = new QueueNode(x);
        rear = front;
        size++;
        return;
    }

    QueueNode *newNode = new QueueNode(x);
    rear->next = newNode;
    rear = newNode;         // update back pointer
    size++;
}

void QueueList::dequeue(){

    if (IsEmpty()) {
        std::cout << "Queue is empty.\n";
        return;
    }

    QueueNode *deletenode = front;
    front = front->next;    // update front pointer
    delete deletenode;
    deletenode = 0;
    size--;
}

int QueueList::getFront(){

    if (IsEmpty()) {
        std::cout << "Queue is empty.\n";
        return -1;
    }

    return front->data;
}

int QueueList::getBack(){

    if (IsEmpty()) {
        std::cout << "Queue is empty.\n";
        return -1;
    }

    return rear->data;
}

bool QueueList::IsEmpty(){

//    return (size == 0);
    return ((front && rear) == 0);
}

int QueueList::getSize(){

    return size;
}

int main(){

    QueueList q;
    if (q.IsEmpty()) {
        std::cout << "Queue is empty.\n";
    }
    q.enqueue(24);
    std::cout<< "\nAfter enqueue 24: \n";
    std::cout << "front: " << q.getFront() << "    rear: " << q.getBack() << "\n";
    q.enqueue(8);
    std::cout<< "\nAfter enqueue 8: \n";
    std::cout << "front: " << q.getFront() << "    rear: " << q.getBack() << "\n";
    q.enqueue(23);
    std::cout<< "\nAfter enqueue 23: \n";
    std::cout << "front: " << q.getFront() << "    rear: " << q.getBack() << "\n";
    q.enqueue(13);
    std::cout<< "\nAfter enqueue 13: \n";
    std::cout << "front: " << q.getFront() << "    rear: " << q.getBack() << "\n";
    q.dequeue();
    std::cout<< "\nAfter pop the front element: \n";
    std::cout << "front: " << q.getFront() << "     rear: " << q.getBack() << "\n";
    q.enqueue(35);
    std::cout<< "\nAfter enqueue 35: \n";
    std::cout << "front: " << q.getFront() << "     rear: " << q.getBack() << "\n";
    q.dequeue();
    std::cout<< "\nAfter pop the front element: \n";
    std::cout << "front: " << q.getFront() << "    rear: " << q.getBack() << "\n";
    q.dequeue();
    std::cout<< "\nAfter pop the front element: \n";
    std::cout << "front: " << q.getFront() << "    rear: " << q.getBack() << "\n";
    q.dequeue();
    std::cout<< "\nAfter pop the front element: \n";
    std::cout << "front: " << q.getFront() << "    rear: " << q.getBack() << "\n";
    q.dequeue();
    std::cout<< "\nAfter pop the front element: \n";
    q.dequeue();

    return 0;
}
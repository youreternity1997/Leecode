// http://wayne.cif.takming.edu.tw/datastru/queue.pdf
#include<iostream>
using namespace std;
#define MAXQUEUE 10 /* 佇列的最大容量 */
int queue[MAXQUEUE]; /* 佇列的陣列宣告 */
int front = -1; /* 佇列的前端 */
int rear = -1; /* 佇列的尾端 */
int isQueueEmpty();
int isQueueFull();
void enqueue(int d);
void dequeue();
void Front();
void PrintQueue();

int isQueueFull(){
    if (rear == MAXQUEUE-1){
        return 1;
    }
    return 0;
}

int isQueueEmpty(){
    if (front == rear){
        cout << "Queue is Empty" << endl;
        return 1;
    }
    return 0;
}

void enqueue(int d){
    if (isQueueFull()){
        cout <<"Queue is Full" << endl;
    }
    else{
        queue[++rear]= d;
        cout <<"enqueue= "<< rear << ",  data= "<< d << endl;
    }
}

void dequeue(){
    if (isQueueEmpty()){
        cout <<"Queue is Empty" << endl;
    }
    else{
        cout <<"dequeue= "<< front << ",  data= "<< queue[++front] << endl;
    }
}

void Front(){
    if(isQueueEmpty())
        cout << "Queue is empty" << endl;
    else
        if (front == -1){
            cout <<"front = "<< 0 << " Front data : "<< queue[0] << endl;
        }
        else{
            cout <<"front = "<< front << " Front data : "<< queue[++front] << endl;
        }
        
}

void PrintQueue()
{   
    cout << "PrintQueue : ";
    if (front == -1){
        for (int i = 0; i <= rear; i++){
            cout << queue[i] << "  ";
        }
    }
    else{
        for (int i = front; i <= rear; i++){
            cout << queue[i] << "  ";
        }
    }
    cout << endl;
    return;
}


int main(){
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    enqueue(5);
    enqueue(6);
    enqueue(7);
    enqueue(8);
    enqueue(9);
    enqueue(10);
    enqueue(11);
    //dequeue();
    //dequeue();
    //dequeue();
    Front();
    PrintQueue();
    return 0;
}
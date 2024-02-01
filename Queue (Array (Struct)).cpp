#include<iostream>
using namespace std;


struct Queue{
    // 先設需要的變數
    int front, rear, MaxSize;
    int *arr;
    
    //建構子constructor，一開始建立struct的初始值
    Queue(int MaxSize)
    {
        front = -1;
        rear = -1;
        MaxSize = MaxSize;
        //動態配置一個陣列出來，因為我們知道陣列其實就含有指標的意涵
        arr = new int;
    }
    //解構子，程式結束後，會自動把使用的空間釋放掉
    ~Queue() 
    {
        delete[] arr; 
    }
    //存入資料
    void enqueue(int val)
    {
        if(rear == MaxSize-1)
        {
            cout << "Queue is full" << endl;
        }
        else
        {
            //這邊使用++rear後置運算，也就是會先做rear++ -->arr[rear] = val
            arr[++rear] = val;
            cout << "rear=" << rear << endl;
        }
        return;
    }
    //刪除資料
    void dequeue()
    {
        if(rear == front)
        {
            cout << "Queue is empty" << endl;
        }
        else
        {
            //因為pop掉之後，會出現空隙，所以要把剩下的陣列全部往前移一格，填補他
            cout << "dequeue------------------------"<< endl;
            for(int i = 0; i < rear; i++)
            {
                cout << "value=" << arr[i+1] << endl;
                arr[i] = arr[i+1];
            }
        }
        rear--;
        return;
    }
    //印出最先進去的那筆資料
    void queueFront()
    {
        if(rear == front)
            cout << "Queue is empty" << endl;
        else
        	cout << "queueFront="<< arr[++front] << endl;
    }
    //印出最後進去的那筆資料
    void queueRear()
    {
        if(rear == front)
            cout << "Queue is empty" << endl;
        else
            cout << "queueRear=" << arr[rear] << endl;
    }
    void View()
    {   
        cout << "View------------------------"<< endl;
    	for(int i = front+1; i <= rear; ++i)
    		cout << "value="<< arr[i] << endl;
    }
    
    
};


int main()
{
    Queue q(5);
    
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);
    q.View();
    
    q.dequeue();
    q.dequeue();
    q.View();
    
    q.queueFront();
    q.queueRear();
    
    return 0;
}
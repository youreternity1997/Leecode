# include<iostream>
#include<string>
using namespace std;
const int MAX_SIZE = 5; // 堆疊的最大大小

class Stack{
    private:
        int top;            // 堆疊頂端的索引
        int stackArray[MAX_SIZE]; // 用陣列實現堆疊
    public:
    Stack(){
        top = -1;
    }
    void push(int data); // 將資料放入堆疊
    int pop(); // 將資料從堆疊取出
    int peek(); // 查看堆疊頂端的資料
    int size();
    bool isEmpty(); // 檢查堆疊是否為空
    bool isFull(); // 檢查堆疊是否已滿
    void clear();
    void outputStack(); // 輸出堆疊

};
void Stack::push(int data){
    if(isFull()){
        cout << "stack is full" << endl;
        return;
    }
    else{
        stackArray[++top] = data;
        cout <<"top= "<< top << ",  data= "<< data<< endl;
    }
}

int Stack::pop(){
    if(isEmpty()){
        cout << "stack is empty" << endl;
        return -1;
    }
    else{
        int data = stackArray[top--];
        return data;
    }
}
int Stack::peek(){
    if(isEmpty()){
        cout << "stack is empty" << endl;
        return -1;
    }
    else{
        return stackArray[top];
    }
}
int Stack::size(){
    return top+1;
}
bool Stack::isEmpty(){
    return (top == 0);
}
bool Stack::isFull(){
    return (top == MAX_SIZE-1);
}
void Stack::clear(){
    top = -1;
    return;
}
void Stack::outputStack(){
    cout << "stack: ";
    for(int i=0; i<=top; i++){
        cout << stackArray[i] << " ";
    }
    cout << endl;
}


int main(){
    Stack stack;
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    //stack.clear();
    stack.push(5);
    stack.push(6); //stack is full
    stack.outputStack();
    cout << "pop value= "<< stack.pop() << endl;
    cout << "peek value= "<< stack.peek() << endl;
    stack.outputStack();
    return 0;
}

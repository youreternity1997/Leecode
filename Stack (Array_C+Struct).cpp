# include<iostream>
#include<string>
using namespace std;
const int MAX_SIZE = 5; // 堆疊的最大大小

class Stack{
    private:
        int size;            // 堆疊頂端的索引
        int stackArray[MAX_SIZE]; // 用陣列實現堆疊
    public:
    Stack(){
        size = 0;
    }
    void push(int data); // 將資料放入堆疊
    int pop(); // 將資料從堆疊取出
    int peek(); // 查看堆疊頂端的資料
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
        stackArray[size] = data;
        size++;
    }
}
int Stack::pop(){
    if(isEmpty()){
        cout << "stack is empty" << endl;
        return -1;
    }
    else{
        int data = stackArray[size-1];
        size--;
        return data;
    }
}
int Stack::peek(){
    if(isEmpty()){
        cout << "stack is empty" << endl;
        return -1;
    }
    else{
        return stackArray[size-1];
    }
}
bool Stack::isEmpty(){
    return (size == 0);
}
bool Stack::isFull(){
    return (size == MAX_SIZE);
}
void Stack::clear(){
    size = 0;
    return;
}
void Stack::outputStack(){
    cout << "stack: ";
    for(int i=0; i<size; i++){
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
    stack.push(6);
    stack.outputStack();
    cout << "pop value= "<< stack.pop() << endl;
    cout << "peek value= "<< stack.peek() << endl;
    stack.outputStack();
    return 0;
}

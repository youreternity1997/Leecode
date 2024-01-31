# include<iostream>
#include<string>
using namespace std;
const int MAX_SIZE = 10; // 堆疊的最大大小
int st[MAX_SIZE], top = -1;

bool isFull(){
    return (top == MAX_SIZE-1);
}

bool isEmpty(){
    return top == -1; // size=0
}

void push(int num){
    if (!isFull()){
        st[++top] = num;
    }
}

void pop(){
    if(!isEmpty()){
        top--;
    }
}

int size(){
    return top+1;
}

void clear(){
    top = -1;
}

// 拿出 stack 最上層的元素
int peek(){
    if(!isEmpty()){
        return st[top];
    }
    return -1;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    push(2); // st[] = {2}
    push(5); // st[] = {2,5}
    push(8); // st[] = {2,5,8}
    push(22); // st[] = {2,5,8,22}
    cout << "Size= "<< size() << "\n"; // 4
    cout << "top data= "<< peek() << "\n"; // 22
    pop(); // st[] = {2,5,8}
    cout << "Size= "<< size() << "\n"; // 3
    cout << "top data= "<< peek() << "\n"; // 8
    clear(); // // st[] = {}
    cout << "Size= "<< size() << "\n"; // 0
    cout << "top data= "<< peek() << "\n"; // -1
    return 0;
}
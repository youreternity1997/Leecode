#include <bits/stdc++.h>
using namespace std;
int st[100100], now = 0;

// push 將元素放入 stack
void push(int num){
    st[now] = num;
    now++;
}

// 確認 stack 是否為空
bool isempty(){
    return now == 0;
}

// 回傳 stack 大小
int size(){
    return now;
}

// 清空 stack
void clear(){
    now = 0;
}

// 拿出 stack 最上層的元素
int top(){
    if(!isempty()){
        return st[now - 1];
    }
    return -1;
}

// 將 stack 最上層的元素刪除
void pop(){
    if(!isempty()){
        now--;
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    push(2); // st[] = {2}
    push(5); // st[] = {2,5}
    push(8); // st[] = {2,5,8}
    push(22); // st[] = {2,5,8,22}
    cout << "Size= "<< size() << "\n"; // 4
    cout << "top= "<< top() << "\n"; // 22
    pop(); // st[] = {2,5,8}
    cout << "Size= "<< size() << "\n"; // 3
    cout << "top= "<< top() << "\n"; // 8
    clear(); // // st[] = {}
    cout << "Size= "<< size() << "\n"; // 0
    cout << "top= "<< top() << "\n"; // -1
    return 0;
}
// https://shengyu7697.github.io/std-queue/
// g++ std-queue.cpp -o a.out -std=c++11
/*push：把值加到尾巴
pop：移除頭的值
back：回傳尾巴的值
front：回傳頭的值
size：回傳目前長度
empty：回傳是否為空
*/
#include <iostream>
#include <queue>

using namespace std;

int main() {
    queue<int> q;
    q.push(1); // [1]
    q.push(2); // [1, 2]
    q.push(3); // [1, 2, 3]

    cout << q.front() << endl; // 1
    cout << q.back() << endl; // 3
    cout << q.size() << endl; // 3

    int a = q.front(); // copy , 記憶體位置不相同
    int &b = q.front(); // reference

    cout << "q.f= "<< q.front() << " " << &q.front() << endl; // 印記體位置
    cout << "a= " << a << " " << &a << endl;
    cout << "b= " << b << " " << &b << endl; // 與 q.front() 記憶體位置相同

    // 印出 queue 內所有內容
    /*
    int size = q.size();
    for (int i = 0; i < size; i++) {
        cout << q.front() << " "; // FIFO 
        q.pop();
    }
    cout << "\n";
    */

    // 印出 queue 內所有內容
    while (!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }
    cout << "\n";

    return 0;
}
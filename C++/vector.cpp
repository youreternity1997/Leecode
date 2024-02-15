// g++ std-vector.cpp -o a.out -std=c++11
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vec; // 宣告一個放 int 的 vector

    vec.push_back(1); // {1}
    vec.push_back(2); // {1, 2}
    vec.push_back(3); // {1, 2, 3}
    vec.push_back(4); // {1, 2, 3, 4}
    vec.push_back(5); // {1, 2, 3, 4, 5}

    vec.pop_back(); // {1, 2, 3, 4} 移除尾巴的值
    vec.pop_back(); // {1, 2, 3}

    cout << "size: " << int(vec.size()) << endl; // 印出大小

    // 印出 vector 內所有內容
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
    cout << "\n";

    // 用 iterator 來印出 vector 內所有內容
    for (vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) {
        cout << *it << " ";
    }
    cout << "\n";

    vec[0] = 99; // {99, 2, 3} 改變裡面的值

    vector<int>::iterator it = vec.begin();
    vec.insert(it+2, 6); // {99, 2, 6, 3}
    vec.erase(it+2); // {99, 2, 3}

    // 快速(懶人)寫法, c++11 才支援
    for (auto &v : vec) {
        cout << v << " ";
    }
    cout << "\n";

    return 0;
}
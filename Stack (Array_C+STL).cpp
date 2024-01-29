#include <iostream>
#include <stack>
using namespace std;
int main(){
    ios::sync_with_stdio(0);//std::ios::sync_with_stdio(false);這條語句關掉scanf 和cin 的同步，加快效率
    cin.tie(0);
    stack<int> st;
    st.push(12); // st = {12}
    st.push(25); // st = {12,25}
    st.push(8); // st = {12,25,8}
    st.push(90); // st = {12,25,8,90}
    cout << st.size() << "\n"; // 4
    cout << st.top() << "\n"; // 90
    st.pop(); // st = {12,25,8}
    cout << st.size() << "\n"; // 3
    cout << st.top() << "\n"; // 8
    cout << st.empty() << "\n"; // 0，代表 false
    return 0;
}
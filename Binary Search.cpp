// Binary Search in C++

#include <iostream>
using namespace std;

int binary_search(int array[], int target, int n) {
    int left = 0;
    int right = n-1; // array 長度 -1
    while (left <= right) {
        int mid = (left + right) / 2; // 用 int 的性質做無條件捨去
        if (array[mid] > target) {
            right = mid - 1;
        } else if (array[mid] < target) {
            left = mid + 1;
        } else {
            return mid; // 剛好找到 target
        }
    }
    return -1;
}
int main(void) {
    int array[] = {3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(array)/sizeof(array[0]); // array 長度 
    cout << binary_search(array, 3, n)  << endl; // 
    cout << binary_search(array, 4, n)  << endl; // 
    cout << binary_search(array, 5, n)  << endl; //
    cout << binary_search(array, 6, n)  << endl; // 
    cout << binary_search(array, 7, n)  << endl; // 
    cout << binary_search(array, 8, n)  << endl; // 
    cout << binary_search(array, 9, n)  << endl; // 
    cout << binary_search(array, 12, n) << endl; // 
}
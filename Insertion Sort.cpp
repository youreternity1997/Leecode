// Insertion sort in C++

#include <iostream>
using namespace std;

// Function to print an array
void printArray(int array[], int size) {
  for (int i = 0; i < size; i++) {
    cout << array[i] << " ";
  }
  cout << endl;
}

void insertionSort(int array[], int size) {
  for (int i = 1; i < size; i++) {
    int key = array[i];
    int j = i - 1;

    // Compare key with each element on the left of it until an element smaller than it is found.
    while (key < array[j] && j >= 0) {
      array[j + 1] = array[j];
      --j;
    }
    //  key>=array[j]
    array[j + 1] = key;
  }
}

// Driver code
int main() {
  int data[] = {6, 4, 5, 7, 1, 3, 2};
  int size = sizeof(data) / sizeof(data[0]);
  insertionSort(data, size);
  cout << "Sorted array in ascending order:\n";
  printArray(data, size);
}

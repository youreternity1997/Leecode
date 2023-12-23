/*******************************************************************************
*
* Program: Selection Sort
*
*******************************************************************************/

#include <iostream>

using namespace std;

void selectionSort(int arr[], int length);

int main()
{
  // A test array and array length
  int arr[] = {6, 3, 2, 4, 1, 5};
  int length = 6;
  
  // Call the function to perform the selection sort algorithm
  selectionSort(arr, length);
  
  // Print out the array so we can be sure it is sorted correctly
  for (int i = 0; i < length; i++)
  {
    cout << "arr[" << i << "] = " << arr[i] << endl;
  }
  return 0;
}

void selectionSort(int arr[], int length)
{
    int i, j, min;
    for (i = 0; i < length - 1; i++) {
        // Find the minimum element in unsorted array
        min = i;
        for (j = i + 1; j < length; j++) {

            if (arr[j] < arr[min])
                min = j;
        }
 
        // Swap the found minimum element
        // with the first element

        if (min != i)
        {
            //swap(arr[min], arr[i]);
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
}
# MergeSort in Python

def mergeSort(array):
    print("array=", array)
    if len(array) > 1:
        m = len(array)//2 # #  m is the point where the array is divided into two subarrays
        L = array[:m]
        R = array[m:]

        mergeSort(L) # Sort the left array
        mergeSort(R) # Sort the right array

        i = j = k = 0
        # Until we reach either end of either L or R, pick larger among
        # elements L and R and place them in the correct position at A[p..r]
        while i < len(L) and j < len(R):
            print('L=', L)
            print('R=', R)
            print('k=', k)
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            print('array=', array)
            k += 1

        # When we run out of elements in either L or R,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            print("array(pick up remaining L)=", array)

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
            print("array(pick up remaining R)=", array)

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
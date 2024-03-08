#include <iostream>
using namespace std;

int decimalToBinary(int decimal) {
    int binary = 0; // Initialize binary result
    int base = 1; // Initialize base for binary place value

    while (decimal > 0) {
        binary += (decimal % 2) * base; // Get the least significant bit and add to binary
        decimal /= 2; // Shift right
        base *= 10; // Move to the next binary place value
    }

    return binary;
}

int main() {
    int decimal;
    
    cout << "Enter a decimal number: ";
    cin >> decimal;

    // Convert decimal to binary and print the result
    int binary = decimalToBinary(decimal);
    cout << "Binary representation: " << binary << endl;

    return 0;
}

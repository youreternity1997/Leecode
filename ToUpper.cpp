#include <iostream>
using namespace std;

char my_toupper(char c) {
    // Check if the character is lowercase
    if (c >= 'a' && c <= 'z') {
        // Convert lowercase to uppercase by subtracting the difference between lowercase and uppercase letters
        return c - ('a' - 'A');
    }
    // If the character is already uppercase or not a letter, return it as is
    return c;
}

int main() {
    char lowercase = 'a';
    char uppercase = my_toupper(lowercase); // Convert 'a' to 'A'
    cout << "Uppercase: " << uppercase << endl;

    return 0;
}
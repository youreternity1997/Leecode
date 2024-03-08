#include <iostream>
#include <cstring>

using namespace std;

void revstr(char *str1){
    char temp;
    int len = strlen(str1); 
    for (int i=0; i<len/2 ;i++){
        temp = str1[i];
        str1[i]= str1[len - i - 1];
        str1[len - i - 1] = temp;
    }
}

int main() {
    char Stri[] = "I will" ;
    cout << "Before Str= "<< Stri << endl; 
    revstr(Stri);
    cout << "Ans : Str= "<< Stri << endl; 
    cout << "\n";
    return 0;
}
#include<iostream>
using namespace std;


int n = 4; // 宣告一塊記憶體，值為 4
int *nptr = &n; // 指標指向n的記憶體前緣


int main(){
    std::cout << nptr << std::endl; // 取得記憶體位址  0x404004
    std::cout << &n << std::endl; // 取得記憶體位址   0x404004

    std::cout << *nptr << std::endl; // 取得記憶體的值  4
    std::cout << n << std::endl; // 取得記憶體的值  4

}
int *n;
float *s;
char *c;

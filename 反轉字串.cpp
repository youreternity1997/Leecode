void revstr(char *str1){
    char temp;
    int len = strlen(str1); 
    for (int i=0; i<len/2 ;i++){
        temp = str1[i];
        str1[i]= str1[len - i - 1];
        str1[len - i - 1] = temp;
    }
}

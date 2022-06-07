#include <stdio.h>
// 문자열을 입력으로 받아서 문자열에 포함된 
// 모든 공백 문자를 
// 삭제하는 함수를 작성

int main(void)
{

    char str[100];
    char dst[100];
    gets(str);
    
    int i=0;
    while(str[i]!='\0'){
        i++;
    }

    int k=0;
    for(int j=0; j<i; j++){
        if(str[j] != ' '){
            dst[k] = str[j];
            k++;
        }
    }
    printf("%s", dst);
   
}

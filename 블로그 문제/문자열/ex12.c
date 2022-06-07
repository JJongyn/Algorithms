#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// 사용자로부터 문자열을 받아서 문자열에 포함된 구두점의 개수를 세는 프로그램을 작성하라.
// 여기서 구두점에는 마침표와 쉼표만이 포함된다고 가정하자.

int main(void)
{
    
    char str[100];
    gets(str);
    int cnt = 0;
    for(int i=0; str[i]!='\0'; i++){
        if(str[i] == '.' || str[i] == ','){
            cnt += 1;
        }
    }
    printf("%d", cnt);
    
}



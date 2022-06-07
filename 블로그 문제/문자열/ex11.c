#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// 사용자에게 영어 이름을 성과 이름으로 나누어서 대문자로 입력하도록 하여서 
// 성과 이름의 위치를 바꾸고 소문자로 변환하여 출력하는 프로그램을 작성하라.


int main(void)
{
    
    char str[100];
    char first_name[100];
    char second_name[100];
    char *token;
    int first = 1;
    
    gets(str);
    
    tolower(str);
    token = strtok(str, " ");
    for(int i=0; token!='\0'; i++){
        if(first){
            strcpy(first_name, token);
            first = 0;
            token = strtok(NULL, " ");
        }
        second_name[i] = token;
        token = strtok(NULL, " ");
    }
}


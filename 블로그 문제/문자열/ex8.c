#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// 영문 문자열 안에 포함된 영단어의 개수를 계산하여 화면에 출력하는 프로그램을 작성하여 보자.

int get_word_count(char *str);

int main(void)
{
    
    char str[100];
    gets(str);

    printf("%d", get_word_count(str));
   
}

int get_word_count(char *str){
    char *token;
    int cnt = 0;
    token = strtok(str, " ");
    while(token!='\0'){
        token = strtok(NULL," ");
        cnt++;
    }
    return cnt;
}

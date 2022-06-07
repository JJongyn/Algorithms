#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// 사용자로부터 받은 문자열에서 각각의 문자가 나타나는 빈도를 계산하여 출력하는 프로그램을 작성하라.

int check(char* str, char c){
    for(int i=0; str[i] !='\0'; i++){
        if(str[i] == c){
            return 0;
        }
    }
    return 1;
}

int main(void)
{
    
    char str[100];
    char pass[100];
    int j=0;
    gets(str);

    for(int i=0; str[i]!='\0'; i++){
        int cnt = 0;
        if(check(pass, str[i])){
            for(int k=i; str[k]!='\0'; k++){
                if(str[i] == str[k]){
                    cnt++;
                }
            }
            printf("%c : %d\n", str[i], cnt);
            pass[j] = str[i];
            j++;
        }
        
    }
}

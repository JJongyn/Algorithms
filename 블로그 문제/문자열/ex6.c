#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// 문자열을 입력으로 받아서 문자열에 포함된 모든 공백 문자를 삭제하는 함수를 작성하고 테스트하라.

void space_delete(char* str){
    char dst[100];
    int j=0;
    for(int i=0; str[i] != '\0'; i++){
        if (isspace(str[i])){
            continue;
        }
        else{
            dst[j] = str[i];
            j++;
        }
    }
    for(int k=0; k<j; k++){
        str[k] = dst[k];
        printf("%c",str[k]);
    }

}

int main(void)
{
    
    char str[100];
    printf("공백 문자가 있는 문자열을 입력하시오: ");
    gets(str);
    space_delete(str);     
}

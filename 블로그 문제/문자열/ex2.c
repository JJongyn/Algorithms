#include <stdio.h>
// 문자열을 입력으로 받아서 문자열에 포함된 
// 모든 공백 문자를 
// 삭제하는 함수를 작성

int main(void)
{

    char str[100];
    char dst[50]; 
    char str2;

    gets(str); // 문자열
    scanf("%c", &str2); // 특정 문자
    
    int cnt = 0;
    for(int i=0; str[i]!='\0'; i++){
        if(str[i] == str2){
            cnt++;
        }
    }

    printf("%d", cnt);   
}

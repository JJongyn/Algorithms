#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// 간단한 철자 교정 프로그램을 작성하여 보자. 문자열을 입력으로 받아서 문자열 안에 마침표가 있으면 문자열의 첫 번째 문자가 대문자인지를 검사한다.
// 만약 대문자가 아니면 대문자로 변환한다. 또한 문장의 끝에 마침표가 존재하는지를 검사한다. 역시 마침표가 없으면 넣어준다. 
// 즉 입력된 문자열이 "pointer is easy"라면 "Pointer is easy."로 변환하여 화면에 출력한다.

int main(void)
{
    
    char str[100];
    gets(str);

    int cnt=0;
    while(str[cnt]!='\0')
        cnt++;
    int first_alpha = 1;

    for(int i=0; i<cnt; i++){
        if(isalpha(str[i]) && first_alpha){
            if(islower(str[i])){
                str[i] = toupper(str[i]);
            }
            first_alpha = 0;
        }
    }

    if(str[cnt-1] != '.'){
        str[cnt] = '.';
        str[cnt+1] = '\0';
    }
    printf("%s", str);
   
}


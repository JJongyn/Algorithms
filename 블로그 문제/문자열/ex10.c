#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// 회문(palindrome)이란 바로 읽거나 거꾸로 읽어도 같은 글이 되는 문구이다. 
// 예를 들면 "Able was I ere I saw Elba"와 같은 문자열이 회문이다. 
// 사용자로부터 문자열을 받아서 회문 여부를 판별하여 그 결과를 화면에 출력하는 프로그램을 작성하여 보라.
// strlen()와 같은 라이브러리 함수는 사용해도 좋다.





int main(void)
{
    
    char str[100];
    gets(str);
    
    int i=0;
    int j=strlen(str)-1;
    int result = 0;


    while(i < j){
        if(tolower(str[i++]) != tolower(str[j--])){
            result = 1;
        }
    }
    if(result)
        printf("X");
    else
        printf("O");
   
}


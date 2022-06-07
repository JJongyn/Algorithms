#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
// 입력받은 문자열에서 문자열과 숫자의 합을 출력
/*
 입력 예시 : baNaNa25aPPLE35
 출력 예시 : baNaNaaPPLE
            60
*/
int main(void)
{

    char *str = "2021sads213sd11dass1s1";
    char buff[] = {0};
    int i  = 0;
    int num_flag = 0;
    int sum = 0;
    int num = 0;


    for(int k=0; k<=strlen(str); k++)
    {
        if(isdigit(str[k]))
        {
            buff[i++] = str[k];
            num_flag = 1;
        }

        else
            num_flag = 0;

        if(num_flag == 0)
        {
            num = atoi(buff);
            sum += num;
            num = 0;
            i = 0;
            buff[0] = '\0';            
        }
    }
    printf("%d\n", sum);
    
}

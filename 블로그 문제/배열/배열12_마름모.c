#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

대각선 길이를 입력 받아
속이 꽉 찬 마름모를 '*'문자를 사용하여 옆으로 나란하게 그리는 프로그램

문제 출처 : https://white-world.tistory.com/6
  *    0 -> 1
 ***   1 -> 3
*****  2 -> 5
 ***   3 -> 3
  *    4 -> 1 
 */
void main()
{  
    int num, i, j, k, t, mid;
    scanf("%d", &num);
    t = num;
    mid = num/2;
    for(i=0; i<num; i++)
    {
        if(i<=mid) //5개면 위에 3개 
        {
            for(j=0; j<mid-i; j++){
                printf(" ");
            }
            for(k=0; k<i*2+1; k++){
                printf("*");
            }
            printf("\n");
        }
        else //5개면 아래 2개 위에랑 반대로 출력
        {
            for(j=0; j<i-mid; j++){
                printf(" ");
            }
            t = t-2;
            for(k=0; k<t;k++){
                printf("*");
            }
            printf("\n");
        }
        



    }
}

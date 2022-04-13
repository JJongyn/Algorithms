#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

가로의 길이가9, 세로의 길이가 3인 int형 2차원 배열에 구구단 2,3,4단 다음과 같이 출력하여라.

문제 출처 : https://billnairk.tistory.com/56?category=771307
 */
void main()
{      
    int data[3][9];
    int i, j;
    for(i=2; i<5; i++){
        for(j=1; j<10; j++){
            data[i-2][j-1] = i * j;
        }
    }
    for(i=0; i<3; i++){
        for(j=0; j<9; j++){
            printf("%d ", data[i][j]);
        }
        printf("\n");
    }
}

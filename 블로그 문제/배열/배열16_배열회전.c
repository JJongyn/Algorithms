#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

4 x 4 배열 회전 코드

문제 출처 : https://m.blog.naver.com/njmk990/220702528255

 */

void getArray(int a[4][4], int b[4][4]);
void PrintArray(int b[4][4]);
void main()
{
   int a[4][4] = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
   int b[4][4] = {0};
   getArray(a, b);
   PrintArray(b);
   
}

void getArray(int a[4][4], int b[4][4])
{
    int i,j;
    for(i=0; i<4; i++){
        for(j=0; j<4; j++){   //00 <- 30, 01 <- 20
            b[i][j] = a[3-j][i];
        }
    }
}

void PrintArray(int b[4][4]){
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            printf("%d", b[i][j]);
        }
        printf("\n");
    }
}
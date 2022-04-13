#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

밑의 그림과 같이 배열 A와 B를 선언한 후 배열 A의 값을 초기화 후 배열 A의 값을 참조하여
배열 B의 값을 초기화 해보자.

문제 출처 : https://billnairk.tistory.com/56?category=771307
 */
void main()
{   
    int i,j;   
    int data_A[2][4] = {{1,2,3,4},{5,6,7,8}};
    int data_B[4][2];

    for(i=0; i<2; i++){
        for(j=0; j<4; j++){
            data_B[j][i] = data_A[i][j];
        }
    }


    for(i=0; i<4; i++){
        for(j=0; j<2; j++){
            printf("%d", data_B[i][j]);
        }
        printf("\n");
    }
}

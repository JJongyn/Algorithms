#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

사용자에게서 총 9개의 숫자를 입력 받아, 3 X 3 배열을 초기화 하시오.   

3 X 3 배열에서 대각선 원소들의 합을 출력하시오..

문제 출처 : https://man-25-1.tistory.com/16?category=940891
 */

void main()
{      
    int size = 3;
    int data[size][size];
    int sum = 0;
    for(int i=0; i<size; i++){
        for(int j=0; j<size; j++){
            scanf("%d", &data[i][j]);
        }
    }
    
    for(int i=0; i<size; i++){
        sum += data[i][i];
    }

    printf("%d", sum);
}

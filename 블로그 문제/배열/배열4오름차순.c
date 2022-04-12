#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

배열3문제의 작업을 N-1번 반복하여, 가장 작은 수부터 가장 큰 수까지 오름차순으로 정렬하시오.
여기서 N = 5 이다.

문제 출처 : https://man-25-1.tistory.com/16?category=940891
 */

void main()
{      
    int size = 5;
    int data[size];
    int tmp;
    for(int i=0; i<size; i++){
        scanf("%d", &data[i]);
    }
    
    for(int j=0; j<size; j++){
        for(int i=0; i<4-j; i++){
            if(data[i] > data[i+1])
            {
                tmp = data[i];
                data[i] = data[i+1];
                data[i+1] = tmp;
            }
        }
    }
    for(int i=0; i<size; i++){
        printf("%d", data[i]);
    }
}

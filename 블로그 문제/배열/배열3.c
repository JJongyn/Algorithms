#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

배열에 5개의 정수를 입력 받아서 저장하시오.
- 첫 번째 원소와 두 번째 원소를 비교하여 첫 번째 원소가 두 번째 원소보다 크면 서로 교환하여 저장하시오.
- 이 교환 연산을 첫 번째 원소부터 마지막 바로 전 원소까지 반복하시오.
- 참고 : 제일 큰 수가 맨뒤로 이동한다.

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
    
    for(int i=0; i<size-1; i++){
        if(data[i] > data[i+1])
        {
            tmp = data[i];
            data[i] = data[i+1];
            data[i+1] = tmp;
        }
    }
    for(int i=0; i<size; i++){
        printf("%d", data[i]);
    }
}

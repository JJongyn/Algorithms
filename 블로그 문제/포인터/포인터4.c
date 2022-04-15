#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [포인터] 

직원들의 월급이 배열 A에 저장되어 있다고 가정하자. 이번달에 회사에서 지급할 월급의
총액을 계산하고자 한다.
정수형 배열 원소들의 합을 구하여 반환하는 함수를 작성하고 테스트하라.

*/
int salary_sum(const int *A, int size);

void main(){
    int a[5] = {200, 300, 400, 500, 600};
    int sum, size;
    sum = salary_sum(a,5);
    size = sizeof(a) / sizeof(a[0]);
    printf("%d\n", size);
    printf("%d", sum);
}
int salary_sum(const int *A, int size){
    int sum = 0;
    for(int i=0; i<size; i++){
        sum += A[i];
    }
    return sum;
}

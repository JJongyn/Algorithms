#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [포인터] 

직원들의 기본급이 배열 A[]에 저장되어 있다. 배열 B[]에는 직원들의 보너스가 저장되어 있다.
기본급과 보너스를 합하여 이번 달에 지급할 월급의 총액을 계산하고자 한다.
A[]와 B[]를 더하여 배열 C[]에 저장하는 함수를 작성하고 테스트하라.
즉, 모든 i에 대하여 C[i] = A[i]+B[i]가 된다.

*/
void salary_sum(const int *A, const int *B, int *C, int size);

void main(){
    int a[5] = {200, 300, 400, 500, 600};
    int b[5] = {30, 60, 90, 120, 150};
    int c[5];
    salary_sum(a,b,c,5);

    for(int i=0; i<5; i++){
        printf("%d ", c[i]);
    }

}
void salary_sum(const int *A, const int *B, int *C, int size){
    for(int i=0; i<size; i++){
        C[i] = A[i] + B[i];
    }
}

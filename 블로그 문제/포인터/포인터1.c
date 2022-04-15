#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [포인터] 
2개의 정수의 합과 차를 동시에 반환하는 함수를 작성하고 테스트하라.
포인터 매개 변수를 사용한다.
*/
void get_sum_diff(int x, int y, int *p_sum, int *p_diff);

void main(){
    int num1, num2;
    int sum, diff;

    scanf("%d", &num1);
    scanf("%d", &num2);

    get_sum_diff(num1, num2, &sum, &diff);

    printf("%d\n", sum);
    printf("%d", diff);

}

void get_sum_diff(int x, int y, int *p_sum, int *p_diff){
    *p_sum = x + y;
    *p_diff = x - y;

}
#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [������] 
2���� ������ �հ� ���� ���ÿ� ��ȯ�ϴ� �Լ��� �ۼ��ϰ� �׽�Ʈ�϶�.
������ �Ű� ������ ����Ѵ�.
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
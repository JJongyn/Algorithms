#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [������] 

�������� ������ �迭 A�� ����Ǿ� �ִٰ� ��������. �̹��޿� ȸ�翡�� ������ ������
�Ѿ��� ����ϰ��� �Ѵ�.
������ �迭 ���ҵ��� ���� ���Ͽ� ��ȯ�ϴ� �Լ��� �ۼ��ϰ� �׽�Ʈ�϶�.

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

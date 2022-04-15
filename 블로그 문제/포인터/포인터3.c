#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [������] 

�������� �⺻���� �迭 A[]�� ����Ǿ� �ִ�. �迭 B[]���� �������� ���ʽ��� ����Ǿ� �ִ�.
�⺻�ް� ���ʽ��� ���Ͽ� �̹� �޿� ������ ������ �Ѿ��� ����ϰ��� �Ѵ�.
A[]�� B[]�� ���Ͽ� �迭 C[]�� �����ϴ� �Լ��� �ۼ��ϰ� �׽�Ʈ�϶�.
��, ��� i�� ���Ͽ� C[i] = A[i]+B[i]�� �ȴ�.

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

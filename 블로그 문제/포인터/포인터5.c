#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [������] 

� ��Ģ�� ���� ���� ������� ������ ���� �����̶�� �Ѵ�. ���� ��� 1 -1 -3 -5
11 -21 43 ...�� ���� �� 1���� ������ ������ ���� ���� ���� �� -2�� ���� ���� ���� �� 1��
���� ���� ���� ���� �����̴�.

: ���� ��(a), ���� ��(m), ���� ��(d), �� ��°������ ��Ÿ���� ����(n)�� �Էµ� ��,
n��°������ ������ ����ϴ� ���α׷��� ������.
*/
void arr_print(int a, int m, int d, int n, int *arr);
void main(){
    int a, m, d, n;
    scanf("%d %d %d %d", &a, &m, &d, &n);
    int arr[n];
    arr_print(a, m, d, n, arr);

    for(int i=0; i<n; i++){
        printf("%d ", arr[i]);
    }
}
void arr_print(int a, int m, int d, int n, int *arr){
    arr[0] = a;
    for(int i=1; i<n; i++){
        arr[i] = arr[i-1] * m + d;
        }
    }



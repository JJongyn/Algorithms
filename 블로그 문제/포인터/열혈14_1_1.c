#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
/*
�� ������ ����� ���� ���� �ڹٲٴ� �Լ��� �����غ���. ���� ��� �Լ��� �̸��� SWAP3���ϸ�,
������ ���·� �Լ��� ȣ��Ǿ�� �Ѵ�.

Swap3(&num1, &num2, &num3);

�׸��� �Լ�ȣ���� ����� num1�� ����� ���� num2��, num2�� ����� ���� num3��, num3�� ����� ���� num1�� ����Ǿ�� �Ѵ�.
*/
void Swap3(int *num1, int *num2, int *num3){
    int temp1;
    temp1 = *num1;
    *num1 = *num3;
    *num3 = *num2;
    *num2 = temp1;
}
void main(){
    int i;
    int arr[3];
    for(i=0; i<3; i++){
        scanf("%d", &arr[i]);
    }
    for(i=0; i<3; i++){
        printf("%d\n", arr[i]);
    }
    printf("-------------------\n");
    Swap3(&arr[0], &arr[1], &arr[2]);

    for(i=0; i<3; i++){
        printf("%d\n", arr[i]);
    }
}   
#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

void main(){
    int num1 = 10, num2 = 20;
    int* ptr1 = &num1;
    int* ptr2 = &num2;
    int* temp; // <-�̻��� ���� ����Ű�� ���� ����

    printf("%d\n", ptr1); // ptr1�� �ּ�
    printf("%d\n", *ptr1); // ptr1�� ����Ű�� ������ ���� ���

    printf("%d\n", ptr2); // ptr2�� �ּ�
    printf("%d\n", *ptr2); // ptr2�� ����Ű�� ������ ���� ���

    // ptr1�� ptr2�� �ּҰ��� ���� ������. �ּҰ��� �����ؾ��ϴϱ� temp�� �ּҰ����� ��������!
    temp = ptr1;
    ptr1 = ptr2;
    ptr2 = temp;

    printf("-------------------------------------------\n");
    printf("%d\n", ptr1); // ptr1�� �ּ�
    printf("%d\n", *ptr1); // ptr1�� ����Ű�� ������ ���� ���

    printf("%d\n", ptr2); // ptr2�� �ּ�
    printf("%d\n", *ptr2); // ptr2�� ����Ű�� ������ ���� ���


}
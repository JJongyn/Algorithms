#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
/*
�迭�� ����� ���� ������ 6,5,4,3,2,1�� �ǵ��� �����ϴ� ������ �ۼ��غ���. ��, ����� �հ� �ڸ� 
����Ű�� ������ ���� �� ���� �����ؼ� �̸� Ȱ���Ͽ� ����� ���� ������ �ڹٲ���Ѵ�.
*/

void main(){
    int arr[6] = {1,2,3,4,5,6};
    int *st = arr;
    int *end = &arr[5];
    int temp;
    for(int i=0; i<3; i++){
        temp = *st;
        *st = *end;
        *end = temp;

        st++;
        end--;
    }
    for(int i=0; i<6; i++){
        printf("%d", arr[i]);
    }
}   
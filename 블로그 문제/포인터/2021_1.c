#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* 2021 1�� 

0�� �Էµ� ������ ������ ����(10�� ����)�� ���� �������� �Է� �޾� ����������
�Էµ� 0�� ������ ���ڵ��� ũ�⸦ ��Ÿ���� ���� ����׷����� ����ϴ� ���α׷��� �ۼ��Ͻÿ�

*/

void main(){
    int arr[10];
    int num, max_idx, max_cp;
    int i, max = 0;

    // �Է� 
    while(1){
        scanf("%d", &num);
        if(num == 0) break;
        if(max < num){
            max = num;
            max_idx = i;
        }
        arr[i] = num;
        i++;
    }
    max_cp = max;
    for(int j=0; j<max; j++){ // 1 2 3 4 5       max = 5    
        for(int k=0; k<i; k++){
            if(arr[k] >= max_cp){
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
        max_cp--;
    }



}



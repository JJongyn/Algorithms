#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* 2021 5�� 

0�� �Էµ� ������ ���� �����͸� �Է� �޾� 0�� ������ �Է� �����͵��� v[]�迭�� �����ϰ� �Էµ� �������� ������ ����
�ϴ� �Լ� int GetIntArray�ϼ��ϰ� 
���̰� n�� �迭 int v[]���� �����ؼ� ����� ������ ������ �������� ���� �ּҰ� min�� ����Ͽ�
'����'�� �����ϴ� �Լ� void SubSumMin(int v[], int n, int * index_start, int* index_end)�� �ۼ��Ѵ�.
�̸� �̿��Ͽ� 0�� �Էµ� ������ ����(100�� ����)���� �Է� �޾�, �����ؼ� �Էµ� ������ ������ �������� ���� �ּҰ� �Ǵ�
��츦 ����ϴ� �Լ��� �ϼ�.

ex)
10 -5 -12 4 -13 11 7 -3 7 -10 5 0 > -5 -12 4 -13
-2 5 -1 -1 0 > -1 -1
-3 -1 8 -1 -3 0 > -1 -3

*/
int GetIntArray(int v[]){
    int num;
    int i = 0;
    while(1){
        scanf("%d", &num);
        if(num == 0) break;
        v[i] = num;
        i++;
    }
    return i;

}

void SubSumMin(int v[], int n, int* index_start, int* index_end){
    int min = 999999;
    for(int i=0; i<n; i++){
        int sum = 0;
        for(int j=i; j<n; j++){
            sum = sum + v[j];
            if(sum <= min){
                min = sum;
                *index_start = i;
                *index_end = j;
            }
        }
    }

}



void main(){
    int arr[100] = { 0 };
    int size;
    int index_start, index_end;
    size = GetIntArray(arr);
    SubSumMin(arr, size, &index_start, &index_end);
    for(int i = index_start; i <= index_end; i++)
        printf("%d ", arr[i]);

}



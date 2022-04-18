#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* 2021 5번 

0이 입력될 때까지 정수 데이터를 입력 받아 0을 제외한 입력 데이터들을 v[]배열에 저장하고 입력된 데이터의 개수를 리턴
하는 함수 int GetIntArray완성하고 
길이가 n인 배열 int v[]에서 연속해서 저장된 임의의 개수의 정수들의 합의 최소값 min을 계산하여
'구간'을 리턴하는 함수 void SubSumMin(int v[], int n, int * index_start, int* index_end)를 작성한다.
이를 이용하여 0이 입력될 때까지 정수(100개 이하)들을 입력 받아, 연속해서 입력된 임의의 개수의 정수들의 합이 최소가 되는
경우를 출력하는 함수를 완성.

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



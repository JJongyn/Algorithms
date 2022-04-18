#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* 2021 1번 

0이 입력될 때까지 임의의 개수(10개 이하)의 양의 정수들을 입력 받아 마지막으로
입력된 0을 제외한 숫자들의 크기를 나타내는 세로 막대그래프를 출력하는 프로그램을 작성하시오

*/

void main(){
    int arr[10];
    int num, max_idx, max_cp;
    int i, max = 0;

    // 입력 
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



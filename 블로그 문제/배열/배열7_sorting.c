#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

배열에 정수를 입력받은 뒤 오름차순과 내림차순으로 정렬해보자
단, 두개의 함수를 사용하여라

문제 출처 : https://billnairk.tistory.com/53
 */


void up(int arr[]){
    int i, j, temp;
    for(i=0; i<10; i++){
        for(j=0; j<9; j++){
            if(arr[j]>arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    for(i=0; i<10; i++){
        printf("%d", arr[i]);
    }
    printf("\n");
}
void down(int arr[]){
    int i,j,temp;
    for(i=0; i<10; i++){
        for(j=0; j<9; j++){
            if(arr[j] < arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;

            }
        }
    }
    for(i=0; i<10; i++){
        printf("%d", arr[i]);
    }    

}
void main()
{      
    int data[10];
    for(int i=0; i<10; i++){
        scanf("%d", &data[i]);
    }
    up(data);
    down(data);

}

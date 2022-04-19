#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* 

버블정렬 (오름차순)

*/

void main(){
    int arr[5]={6,2,1,4,7};
    int tmp;
    for(int i=0; i<5; i++){
        for(int j=0; j<4; j++){
            if(arr[j] > arr[j+1]){
                tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
        }
    }
    
    
    for(int i=0; i<5; i++){
        printf("%d", arr[i]);
    }

}



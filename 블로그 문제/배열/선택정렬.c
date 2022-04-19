#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* 

선택정렬 

*/

void main(){
    int arr[5]={6,2,1,4,7};
    int tmp;
    for(int i=0; i<5; i++){
        int least = i;
        for(int j=i; j<5; j++){
            if(arr[least] > arr[j]){
                tmp = arr[least];
                arr[least] = arr[j];
                arr[j] = tmp;
            }
        }
    }

    for(int i=0; i<5; i++){
        printf("%d", arr[i]);
    }

}



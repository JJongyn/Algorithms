#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [버블 정렬] 

세 수를 오름차순으로 정렬하려고 한다. (낮은 숫자 -> 높은 숫자)

예)
5 8 2   ====> 2 5 8    로 출력

*/

int main(){
    int arr[3];
    int temp;
    scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);

    for(int i=0; i<3; i++){
        for(int j=0; j<3-i; j++){ // or j<3-1
            if(arr[j]>arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    for(int i=0; i<3; i++){
        printf("%d ", arr[i]);
    }
}

/* [추가]


*/
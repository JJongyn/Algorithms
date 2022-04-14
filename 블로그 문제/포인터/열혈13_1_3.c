#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
/*
배열에 저장된 값의 순서가 6,5,4,3,2,1이 되도록 변경하는 예제를 작성해보자. 단, 배욜의 앞과 뒤를 
가리키는 포인터 변수 두 개를 선언해서 이를 활용하여 저장된 값의 순서를 뒤바꿔야한다.
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
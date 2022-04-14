#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
/*
세 변수에 저장된 값을 서로 뒤바꾸는 함수를 정의해보자. 예를 들어 함수의 이름이 SWAP3라하면,
다음의 형태로 함수가 호출되어야 한다.

Swap3(&num1, &num2, &num3);

그리고 함수호출의 결과로 num1에 저장된 값은 num2에, num2에 저장된 값은 num3에, num3에 저장된 값은 num1에 저장되어야 한다.
*/
void Swap3(int *num1, int *num2, int *num3){
    int temp1;
    temp1 = *num1;
    *num1 = *num3;
    *num3 = *num2;
    *num2 = temp1;
}
void main(){
    int i;
    int arr[3];
    for(i=0; i<3; i++){
        scanf("%d", &arr[i]);
    }
    for(i=0; i<3; i++){
        printf("%d\n", arr[i]);
    }
    printf("-------------------\n");
    Swap3(&arr[0], &arr[1], &arr[2]);

    for(i=0; i<3; i++){
        printf("%d\n", arr[i]);
    }
}   
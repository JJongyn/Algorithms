#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

void main(){
    int num1 = 10, num2 = 20;
    int* ptr1 = &num1;
    int* ptr2 = &num2;
    int* temp; // <-이상한 곳을 가리키고 잇을 거임

    printf("%d\n", ptr1); // ptr1의 주소
    printf("%d\n", *ptr1); // ptr1이 가리키는 변수에 값을 출력

    printf("%d\n", ptr2); // ptr2의 주소
    printf("%d\n", *ptr2); // ptr2가 가리키는 변수에 값을 출력

    // ptr1과 ptr2의 주소값을 서로 변경함. 주소값을 저장해야하니깐 temp도 주소값으로 선언해줌!
    temp = ptr1;
    ptr1 = ptr2;
    ptr2 = temp;

    printf("-------------------------------------------\n");
    printf("%d\n", ptr1); // ptr1의 주소
    printf("%d\n", *ptr1); // ptr1이 가리키는 변수에 값을 출력

    printf("%d\n", ptr2); // ptr2의 주소
    printf("%d\n", *ptr2); // ptr2가 가리키는 변수에 값을 출력


}
#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
/* p.328 [포인터] 도전1

길이가 10인 배열을 선언하고 총 10개의 정수를 입력 받아서, 홀수와 짝수를 구분 지어 출력하는 
프로그램을 작성하시오. 일단 홀수부터 출력하고 나서 짝수를 출력한다. 단, 10개의 정수는 main 함수 내에서
입력 받도록 하고, 배열 내에 존재하는 홀수만 출력하는 함수와 배열내에 존재하는 짝수만 출력하는 
함수를 각각 정의해서 이 두함수를 호출하는 방식으로 완성하시오

출력예시)
입력 : 1
입력 : 2
......
홀수 출력 : 1 3 5 7 9
짝수 출력 : 2 4 6 8 0

*/
void odd_num(int arr[]){
    for(int i=0; i<10; i++){
        if(arr[i] % 2 !=0){
            printf("%d",arr[i]);
        }
    }
}
void even_num(int arr[]){
    for(int i=0; i<10; i++){
        if(arr[i] % 2 ==0){
            printf("%d",arr[i]);
        }
    }
}
void main(){
    int i;
    int arr[10];
    for(i=0; i<10; i++){
        scanf("%d", &arr[i]);
    }
    printf("even num : ");
    even_num(arr);
    printf("\n");
    printf("odd num : ");
    odd_num(arr);
}   
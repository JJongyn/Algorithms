#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
/* p.328 [포인터] 도전2

프로그램 사용자로부터 10진수 형태로 정수를 하나 입력 받은 다음, 이를 2진수로 변환해서
출력하는 프로그램을 작성해보자

*/

void main(){
    int num,r;
    int arr[100];
    int i=0;
    scanf("%d", &num);

    while(1){
        r = num % 2;
        arr[i] = r;
        num = num / 2;
        if (num == 0) break;
        i++;
    }

    for(i;i>=0;i--){
        printf("%d", arr[i]);
    }
    
}   
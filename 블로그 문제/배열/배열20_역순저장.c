#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

크기가 10인 배열을 통해 정수 10개를 입력 받고,
이를 역순으로 저장하는 함수를 만들어보아라.

문제 출처 : https://velog.io/@gnoeyah/C%EC%96%B8%EC%96%B4-%EA%B8%B0%EC%B4%88-08.-%EC%97%B0%EC%8A%B5-%EB%AC%B8%EC%A0%9C

 */

void main(){
    int data[10];
    for(int i=1; i<11; i++){
        scanf("%d", &data[10-i]);
    }
    
    for(int i=0; i<10; i++){
        printf("%d", data[i]);
    }
}

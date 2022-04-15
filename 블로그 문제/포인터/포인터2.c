#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [포인터] 
정수 배열 A[]를 다른 정수 배열 B[]에 복사하는 함수를 작성하고 테스트하라.
*/
void array_copy(int *x, int *y, int size);

void main(){
    int a[5] = {1,2,3,4,5};
    int b[5];
    array_copy(a,b,5);

    for(int i=0; i<5; i++){
        printf("%d", b[i]);
    }

}
void array_copy(int *x, int *y, int size){
    for(int i=0; i<size; i++){
        y[i] = x[i];
    }
}


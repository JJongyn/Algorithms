#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [������] 
���� �迭 A[]�� �ٸ� ���� �迭 B[]�� �����ϴ� �Լ��� �ۼ��ϰ� �׽�Ʈ�϶�.
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


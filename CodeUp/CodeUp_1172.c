#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [���� ����] 

�� ���� ������������ �����Ϸ��� �Ѵ�. (���� ���� -> ���� ����)

��)
5 8 2   ====> 2 5 8    �� ���

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

/* [�߰�]


*/
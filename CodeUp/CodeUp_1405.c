#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [������] 

n���� ���ڰ� �ԷµǸ�,

n���� ���ڸ� �������� �ϳ��� ������ ����Ͻÿ�.

��) 1 2 3 4 5�� �Էµ� ���,

1 2 3 4 5

2 3 4 5 1

3 4 5 1 2

4 5 1 2 3

5 1 2 3 4

*/

void main(){
    int i, j, n;
    scanf("%d", &n);
    int arr[n];
    for(i=0; i<n; i++)
    {
        scanf("%d", &arr[i]);
    }
    
    for(i=0; i<n; i++)
    {
        for(j=0; j<n-i; j++) // 345 
        {
            printf("%d ", arr[j+i]);
        }

        for(j=0; j<i; j++) // 12
        {
            printf("%d ", arr[j]);
        }
        printf("\n");
    }
}

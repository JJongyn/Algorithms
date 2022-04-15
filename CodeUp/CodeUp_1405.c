#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [포인터] 

n개의 숫자가 입력되면,

n개의 숫자를 왼쪽으로 하나씩 돌려서 출력하시오.

예) 1 2 3 4 5가 입력된 경우,

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

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

배열 내 특정 배수 값 제외 코드

문제 출처 : https://m.blog.naver.com/njmk990/220702523543

 */

int DeleteArray(int x[], int n, int k);
void PrintArray(int v[], int n);
void main()
{
   int arr[9] = {1,2,3,4,5,6,7,8,9};
   int k, s;
   scanf("%d", &k);
   s = DeleteArray(arr,9,k);
   PrintArray(arr,s);
}
int DeleteArray(int x[], int n, int k){
    for(int i=0; i<n; i++){ 
        if(x[i] % k == 0)
        {
            for(int j=i; j<n; j++){
                x[j] = x[j+1];
            }
            n--;
            i--;
        }
    }
    return n;
}
void PrintArray(int v[], int n){
    for(int i=0; i<n; i++){
        printf("%d", v[i]);
    }
}
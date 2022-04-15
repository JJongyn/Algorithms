#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [포인터] 

어떤 규칙에 따라 수를 순서대로 나열한 것을 수열이라고 한다. 예를 들어 1 -1 -3 -5
11 -21 43 ...은 시작 값 1부터 시작해 이전해 만든 수를 곱할 값 -2를 곱한 다음 더할 값 1을
더해 다음 수를 만든 수열이다.

: 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
n번째수까지 수열을 출력하는 프로그램을 만들어보자.
*/
void arr_print(int a, int m, int d, int n, int *arr);
void main(){
    int a, m, d, n;
    scanf("%d %d %d %d", &a, &m, &d, &n);
    int arr[n];
    arr_print(a, m, d, n, arr);

    for(int i=0; i<n; i++){
        printf("%d ", arr[i]);
    }
}
void arr_print(int a, int m, int d, int n, int *arr){
    arr[0] = a;
    for(int i=1; i<n; i++){
        arr[i] = arr[i-1] * m + d;
        }
    }



#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
#define SIZE 5
/* [ 배열 ]

입력된 5개의 정수들 중에서 중간값을 출력하는 프로그램을 작성하시오.

문제 출처 : https://m.blog.naver.com/njmk990/220820485266

 */

void selection(int arr[], int n);

void main()
{
   int i;
   int data[SIZE];
   for(i=0; i<SIZE; i++)
   {
       scanf("%d", &data[i]);
   }
   selection(data,SIZE);
   printf("%d", data[2]);
}

void selection(int arr[], int n)
{   
    int i,j,temp;
    for(i=0; i<n; i++){
        for(j=0; j<n-1; j++){
            if(arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
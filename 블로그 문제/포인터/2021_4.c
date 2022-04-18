#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* 2021 4번 

세 개의 자연수를 입력 받아, 약수의 개수에 따라 내림차순으로 정렬하여 출력하는 프로그램을 작성하여라.


*/
void sortNdiv(int *a, int *b, int *c){
    int cnt[3] = {0};
    int arr[3] = {*a, *b, *c};
    for(int i = 1; i <= arr[0]; i++){
        if( arr[0] % i == 0) cnt[0]++;
    }
    for(int j = 1; j <= arr[1]; j++){
        if( arr[1] % j == 0) cnt[1]++;
    }
    for(int k = 1; k <= arr[2]; k++){
        if( arr[2] % k == 0) cnt[2]++;
    }
    printf("%d %d %d\n", cnt[0], cnt[1] ,cnt[2]);

    int most, tmp;
   for(int i=0; i<2; i++){
       most = i;
       for(int j=i+1; j<3; j++){
           if(cnt[i] < cnt[j]){
               most = j;
           }
           tmp = cnt[i];
           cnt[i] = cnt[most];
           cnt[most] = tmp;

           tmp = arr[i];
           arr[i] = arr[most];
           arr[most] = tmp;
        
       }
   }

    *a = arr[0];
    *b = arr[1];
    *c = arr[2];
}


void main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    sortNdiv(&a, &b, &c);
    printf("%d %d %d", a, b, c);
}



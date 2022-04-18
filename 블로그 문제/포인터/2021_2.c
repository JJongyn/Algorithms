#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* 2021 2번 

자연수 원소들로 구성된 두 집합을 입력받고, 두 집합의 합집합을 출력한다.

각 집합의 원소들은 0이 입력될 때까지 숫자가 작은 순서대로 각각 입력받는다.
각 집합의 최대 크기는 100이다.
getIntArray(int arr[])함수에서 0이 입력될 때까지 배열 arr에 차례대로 저장하고, 입력의 개수를 리턴한다.
setUnion(int *a, int size_a, int *b, int size_b, int *c)함수에서 크기가 size_a인 배열 a와 크기가 size_b인 배열 b의
합집합을 구해 
ex:
1 2 3 4 5 0
4 5 6 7 0 ->
1 2 3 4 5 6 7 )

*/
int getIntArray(int arr[]){
    int num;
    int i = 0;
    while(1){
        scanf("%d", &num);
        if(num == 0) break;
        arr[i] = num;
        i++;
    }
    return i;

}

int setUnion(int *a, int size_a, int *b, int size_b, int *c){
    int j = 0;
    int d[200] = {0};
    for(int i=0; i<size_a; i++){           
        c[i] = a[i];
    }
    for(int i=size_a; i<size_a + size_b; i++){
        c[i] = b[j];
        j++;
    }
    int n = size_a + size_b;
    for(int i=0; i<n;i++){
        printf("%d", c[i]);
    }
    printf("\n");

    int k = 0;
    for(int i=0; i<size_a+size_b; i++){
        int cnt = 0;
        for(int j = 0; j<k; j++){
            if(c[i] == d[j]) cnt++;
        }

        if(cnt == 0){
            d[k] = c[i];
            k++;
        }

    }

    for(int i=0; i<k; i++){
        c[i] = d[i];
    }
    printf("%d\n", k);
    return k;
}


void main(){
    int a[100], b[100], c[200], size_a, size_b, size_c;
    size_a = getIntArray(a);
    size_b = getIntArray(b);
    size_c = setUnion(a, size_a, b, size_b, c);
    for(int i=0; i<size_c; i++){
        printf("%d ", c[i]);
    }

}



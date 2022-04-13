#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

0이 입력될 때까지 임의의 개수(100개 이하)의 양의 정수들을 입력 받아
마지막으로 입력된 0을 제외한 숫자들의 크기를 나타내는 세로 막대그래프를 출력하시오.

문제 출처 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=njmk990&logNo=220702044748
 */
void main()
{  
    int num, j, k, data_len, temp;
    int size = 100;
    int data[size];
    int i = 0; 
    int max = 0;

    while(1){
        scanf("%d", &num);
        if(num==0) break;
        data[i] = num;
        i++;

        if(max < num){
            max = num;
        }
    }
    printf("data_len : %d\n", i);
    temp = max;
    for(j=0; j<max; j++){
        for(k=0; k<i; k++){
            if(temp <= data[k]){
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
        temp--;
    }
}

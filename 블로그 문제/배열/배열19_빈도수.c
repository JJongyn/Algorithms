#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

0부터 9까지의 정수 중에서 20개의 수를 입력 받아 가장 많이 입력 받은 빈도 수는 무엇이고,
빈도 수는 몇 번인지 출력하는 프로그램 작성

문제 출처 : https://devbase.tistory.com/18

 */

void main(){
    int num_freq[10] = {0};
    int max = 0;
    int num, i, idx;

    for(i=0; i<20; i++){
        scanf("%d", &num);
        num_freq[num]++;
    }

    for(i=0; i<10; i++){
        if(num_freq[i] > max){
            max = num_freq[i];
            idx = i;
        }
    }
    printf("1 . %d : %d\n",idx, max);
    for(i=0; i<10; i++){
        printf("%d : %d\n", i, num_freq[i]);
    }
}

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

길이가 10인 배열에 10개의 정수를 입력 받으면서 입력받은 정수가 배열의 앞에서부터
채워나가고 짝수면 배열의 맨 뒤에서부터 채워나가는 프로그램을 만들어보자.


문제 출처 : https://billnairk.tistory.com/53
 */

void main()
{      
    int data[10];
    int num;
    int j = 9;
    int k = 0;
    for(int i=0; i<10; i++){
        scanf("%d", &num);
        if(num % 2 == 0){
            data[j] = num;
            j--;
        }
        else{
            data[k] = num;
            k++;
        }
    }
    for(int i=0; i<10; i++){
        printf("%d", data[i]);
    }
}

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

10개의 정수를 입력 받는다. 각 정수가 몇 번 등장했는지를 입력받은 순서대로 출력하시오
입력받은 숫자와 총 입력 횟수를 함께 출력하시오. 동일한 숫자에 대해서는 한번만 출력하시오.
입력 예시: 13 2 2 5 6 3 3 3 3 5
출력 예시: 
13 1
2 2 
5 2
6 1 
3 4
문제 출처 : https://man-25-1.tistory.com/16?category=940891
 */

void main()
{      
    int data[10] = {0};
    int cnt[10] = {0};
    int pass[10] = {0};
    int flag = 0;
    for(int i=0; i<10; i++){
        scanf("%d", &data[i]);
    }

    for(int i=0; i<10; i++){
        // cnt햇는지 검사
        for(int k=0; k<10; k++)
        {
            if(pass[k] == data[i]){ //2
                flag = 1;
                break;
            }
            else{
                flag = 0;
            }
        }
        // 중복되는 값들은 빼기 위함
        if (flag == 0)
        {
            pass[i] = data[i];
            for(int j=i; j<10; j++){
                if(data[i] == data[j]){
                    cnt[i]++;
                }
            }
        }
    }

    
    for(int i=0; i<10; i++){
        if(pass[i] != 0)
            printf("%d %d\n", pass[i], cnt[i]);
    }
    
    

}

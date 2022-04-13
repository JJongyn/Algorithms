#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

양의 정수 n을 입력 받아 소인수 분해 하여 출력하는 코드

문제 출처 : https://m.blog.naver.com/PostView.naver?blogId=njmk990&logNo=220709399374&targetKeyword=&targetRecommendationCode=1

 */
int GetPrime(void);

void main()
{
    int num, i;
    scanf("%d", &num);  
    i = GetPrime();
    while(1)
    {
        if(num % i == 0){
            num = num / i;
            printf("%d", i);
        }
        else{
            i = GetPrime();
        }
        if(num < i){
            break;
        }
    }

}
int GetPrime(void)
{
    static int prime = 1;
    while(1){

        int cnt = 0;
        prime++;
        for(int i=1; i<=prime; i++){
            if(prime % i == 0){
                cnt += 1;
            }
        }
        if(cnt == 2)
        {
            break;
        }
    }
    return prime;
}
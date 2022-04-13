#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

분모가 0인 분수가 입력될 때까지 분수들을 입력 받아 마지막
분수를 제외한 분수들의 합을 출력하는 프로그램.

문제 출처 : https://m.blog.naver.com/PostView.naver?blogId=njmk990&logNo=220702064997&targetKeyword=&targetRecommendationCode=1

 */
int getGCD(int a, int b);
void addFraction(int m1, int n1, int m2, int n2, int *m3, int *n3);

void main()
{  
   int n1,m1,n2,m2,n3,m3;
   int sum_n = 0;
   int sum_m = 0;

   while(1){

       scanf("%d %d", &m1,&n1); // m1/n1
       if(n1 == 0) break;

       if(sum_n == 0){
           sum_m = m1;
           sum_n = n1;
       }
       else{
           addFraction(m1,n1,sum_m,sum_n,&sum_m,&sum_n);
       }
   }
   printf("%d %d",sum_m,sum_n);
}

void addFraction(int m1, int n1, int m2, int n2, int *m3, int *n3){
    int m3_, n3_, gcd;
    m3_ = (m1 * n2) + (m2 * n1);
    n3_ = n1 * n2;
    gcd = getGCD(m3_, n3_);

    *m3 = m3_ / gcd;
    *n3 = n3_ / gcd;
}

int getGCD(int a, int b){
    int n;
    while(b!=0)
    {
        n = a%b;
        a = b;
        b = n;
    }
    return a;
}
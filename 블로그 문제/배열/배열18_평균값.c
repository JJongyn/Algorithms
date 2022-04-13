#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
#define SIZE 5
/* [ 배열 ]

5개의 정수를 입력 받아 짝수들의 평균과 홀수들의 평균을 화면에 출력

문제 출처 : https://m.blog.naver.com/njmk990/220820487259
 */

void GetintArray(int v[], int n);
void Avg(int v[], int n, double *p_even_avg, double *p_odd_avg);

void main(){
    int data[5];
    double e,o;
    GetintArray(data, 5);
    Avg(data, 5, &e, &o);
    printf("%g\n",e);
    printf("%g",o);
}

void GetintArray(int v[], int n){
    for(int i=0; i<n; i++){
        scanf("%d", &v[i]);
    }
}

void Avg(int v[], int n, double *p_even_avg, double *p_odd_avg){
    double e_sum, cnt1 = 0;
    double o_sum, cnt2 = 0; // 자료형 선언 신경쓰기!
    for(int i=0; i<n; i++){
        if(v[i] % 2 == 0){
            e_sum += v[i];
            cnt1++;
        }
        else{
            o_sum += v[i];
            cnt2++;
        }
    }
    *p_even_avg = e_sum / cnt1;
    *p_odd_avg = o_sum / cnt2;
    
    if(e_sum == 0){
        *p_even_avg = 0;
    }
    else if(o_sum == 0){
        *p_odd_avg = 0;
    }
    
}
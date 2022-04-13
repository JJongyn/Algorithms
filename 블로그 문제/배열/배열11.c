#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [ 배열 ]

5개 이하의 정수를 입력받은 후 역순으로 출력하는 코드

문제 출처 : https://m.blog.naver.com/PostView.naver?blogId=njmk990&logNo=220702519414&targetKeyword=&targetRecommendationCode=1
 */
void main()
{  
    int N,i;
    int data[5];
    for(i=0; i<5; i++){
        scanf("%d", &data[i]);
    }
    for(i=5; i>0; i--){
        printf("%d", data[i-1]);
    }

}

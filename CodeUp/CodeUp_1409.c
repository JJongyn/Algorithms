#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* [배열] 

n개의 숫자가 입력되면, 다음과 같이 크기를 비교한 후 양식에 맞춰 출력하시오.

예를 들어, 1 2 3 2 1 이라는 숫자가 입력되면,

첫 번째 1과 나머지 2, 3, 2, 1을 비교하면 1 < 2,  1 < 3, 1 < 2, 1 = 1 이므로 < < < = 를 출력한다.

두 번째 2와 나머지 1, 3, 2, 1을 비교하면 2 > 1, 2 < 3, 2 = 2, 2 > 1 이므로 > < = > 를 출력한다.

세 번째 3과 나머지 1, 2, 2, 1을 비교하면 3 > 1, 3 > 2, 3 > 2, 3 > 1 이므로 > > > > 를 출력한다.

같은 방법으로 네 번째는 > = < >, 다섯번째는 = < < < 를 출력한다.

이와 같은 방식의 대소 비교 결과를 출력하시오. 

입력 예시   
5
1 2 3 2 1 

출력 예시
1: < < < = 
2: > < = > 
3: > > > > 
4: > = < > 
5: = < < < 
*/

int main(){
    int i, j, k, n;
    char ch[3] = {'>', '<', '='};
    scanf("%d", &n);
    int data[n];
    for(i=0; i<n; i++)
    {
        scanf("%d", &data[i]);
    }

    for(i=0; i<n; i++)
    {
        printf("%d: ",i+1);
        // 현재 idx의 왼쪽 부분
        for(j=0; j<i; j++)
        {
            if(data[i] > data[j]) printf("> ");
            else if(data[i] < data[j]) printf("< ");
            else printf("= ");
        }
        // 현재 idx의 오른쪽 부분
        for(k=i+1; k<n; k++){
            if(data[i] > data[k]) printf("> ");
            else if(data[i] < data[k]) printf("< ");
            else printf("= ");
        }
        printf("\n");
    }
}

/* [추가]

왼쪽, 오른쪽 나눠서 하지 말고
인덱스 i = j 가 같아질 때는 continue하면 for문 하나로 해결 가능!

*/
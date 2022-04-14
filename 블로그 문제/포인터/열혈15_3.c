#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
/* p.328 [포인터] 도전2

길아가 10인 배열을 선언하고 총 10개의 정수를 입력 받는다. 단, 입력받은 숫자가 홀수이면
배열의 앞에서 부터 채워나가고, 짝수이면 뒤에서부터 채워나가는 형식을 취하기로 하자.
따라서 사용자가 [1,2,3,4,5,6,7,8,9,10]을 입력했다면, 배열에는 [1,3,5,7,9,10,8,6,4,2]순으로
저장이 되어야 한다.

*/

void main(){
    int i, num;
    int arr[10];
    int o = 0;
    int e = 9;
    for(i=0; i<10; i++){
        scanf("%d", &num);
        if (num % 2 != 0){
            arr[o] = num;
            o++;
        }
        else{
            arr[e] = num;
            e--;
        }
    }
    for(i=0; i<10; i++){
        printf("%d", arr[i]);
    }

    
}   
#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
/* p.328 [������] ����2

���α׷� ����ڷκ��� 10���� ���·� ������ �ϳ� �Է� ���� ����, �̸� 2������ ��ȯ�ؼ�
����ϴ� ���α׷��� �ۼ��غ���

*/

void main(){
    int num,r;
    int arr[100];
    int i=0;
    scanf("%d", &num);

    while(1){
        r = num % 2;
        arr[i] = r;
        num = num / 2;
        if (num == 0) break;
        i++;
    }

    for(i;i>=0;i--){
        printf("%d", arr[i]);
    }
    
}   
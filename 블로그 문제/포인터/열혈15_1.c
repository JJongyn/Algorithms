#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
/* p.328 [������] ����1

���̰� 10�� �迭�� �����ϰ� �� 10���� ������ �Է� �޾Ƽ�, Ȧ���� ¦���� ���� ���� ����ϴ� 
���α׷��� �ۼ��Ͻÿ�. �ϴ� Ȧ������ ����ϰ� ���� ¦���� ����Ѵ�. ��, 10���� ������ main �Լ� ������
�Է� �޵��� �ϰ�, �迭 ���� �����ϴ� Ȧ���� ����ϴ� �Լ��� �迭���� �����ϴ� ¦���� ����ϴ� 
�Լ��� ���� �����ؼ� �� ���Լ��� ȣ���ϴ� ������� �ϼ��Ͻÿ�

��¿���)
�Է� : 1
�Է� : 2
......
Ȧ�� ��� : 1 3 5 7 9
¦�� ��� : 2 4 6 8 0

*/
void odd_num(int arr[]){
    for(int i=0; i<10; i++){
        if(arr[i] % 2 !=0){
            printf("%d",arr[i]);
        }
    }
}
void even_num(int arr[]){
    for(int i=0; i<10; i++){
        if(arr[i] % 2 ==0){
            printf("%d",arr[i]);
        }
    }
}
void main(){
    int i;
    int arr[10];
    for(i=0; i<10; i++){
        scanf("%d", &arr[i]);
    }
    printf("even num : ");
    even_num(arr);
    printf("\n");
    printf("odd num : ");
    odd_num(arr);
}   
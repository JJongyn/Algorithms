#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

/* 2021 2�� 

�ڿ��� ���ҵ�� ������ �� ������ �Է¹ް�, �� ������ �������� ����Ѵ�.

�� ������ ���ҵ��� 0�� �Էµ� ������ ���ڰ� ���� ������� ���� �Է¹޴´�.
�� ������ �ִ� ũ��� 100�̴�.
getIntArray(int arr[])�Լ����� 0�� �Էµ� ������ �迭 arr�� ���ʴ�� �����ϰ�, �Է��� ������ �����Ѵ�.
setUnion(int *a, int size_a, int *b, int size_b, int *c)�Լ����� ũ�Ⱑ size_a�� �迭 a�� ũ�Ⱑ size_b�� �迭 b��
�������� ���� 
ex:
1 2 3 4 5 0
4 5 6 7 0 ->
1 2 3 4 5 6 7 )

*/
int getIntArray(int arr[]){
    int num;
    int i = 0;
    while(1){
        scanf("%d", &num);
        if(num == 0) break;
        arr[i] = num;
        i++;
    }
    return i;

}

int setUnion(int *a, int size_a, int *b, int size_b, int *c){
    int j = 0;
    int d[200] = {0};
    for(int i=0; i<size_a; i++){           
        c[i] = a[i];
    }
    for(int i=size_a; i<size_a + size_b; i++){
        c[i] = b[j];
        j++;
    }
    int n = size_a + size_b;
    for(int i=0; i<n;i++){
        printf("%d", c[i]);
    }
    printf("\n");

    int k = 0;
    for(int i=0; i<size_a+size_b; i++){
        int cnt = 0;
        for(int j = 0; j<k; j++){
            if(c[i] == d[j]) cnt++;
        }

        if(cnt == 0){
            d[k] = c[i];
            k++;
        }

    }

    for(int i=0; i<k; i++){
        c[i] = d[i];
    }
    printf("%d\n", k);
    return k;
}


void main(){
    int a[100], b[100], c[200], size_a, size_b, size_c;
    size_a = getIntArray(a);
    size_b = getIntArray(b);
    size_c = setUnion(a, size_a, b, size_b, c);
    for(int i=0; i<size_c; i++){
        printf("%d ", c[i]);
    }

}



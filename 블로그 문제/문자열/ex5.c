#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(void)
{

    char src[] = "HI MYNAME";
    char dst[] = "\0";

    int j = 0;
    for(int i=0; i<strlen(src); i++){
        if(isspace(src[i])) 
            continue;
        else{
            dst[j] = src[i];
            j++;
        }
    }   
    dst[j] = '\0';
    printf("%s",dst);
    
}

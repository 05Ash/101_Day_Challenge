#include<stdio.h>
#include<stdlib.h>

void main(){
    int x=543210, divisor = 10, y, index, z = x;
    while( z > 0){
        index = (x%divisor)*10/divisor;
        printf("index = %d, num = %d\n", index, x);
        divisor *= 10;
        z /= 10;
    }
}

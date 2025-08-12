//misc_codes.h

#include "misc_codes.h"
#include <stdlib.h>
#include <stdio.h>

int print_array(int *data, int m){
    printf("\n");
    for(int i = 0; i < m; i++){
        printf("%d\t", data[i]);
    }
    printf("\n");
    return 0;
}

int swap_num(int *data, int a, int b){
    int temp;
    temp = data[a];
    data[a] = data[b];
    data[b] = temp;

    return 0;
}

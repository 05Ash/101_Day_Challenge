#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "misc_codes.h"

int radix_sort(int *data, int m){
    int **radix_array = (int **)malloc(10 * sizeof(int *));
    if(radix_array == NULL){
        printf("Memory allocation failed.\n");
        return EXIT_FAILURE;
    }
    for(int i=0; i<10;i++){
        radix_array[i] = (int *)malloc(m * sizeof(int));
        if(radix_array[i] == NULL){
            printf("Memory allocation failed.\n");
            for(int j=0; j<i; j++){
                free(radix_array[j]);
            }
            free(radix_array);
            return EXIT_FAILURE;
        }
        radix_array[i][0] = 0;
    }
    int max_value = data[0];
    for(int j = 0; j < m; j++){
        if(data[j] > max_value)
            max_value = data[j];
    }
    int num, current_size, index, divisor = 1, arr_pointer = 0;
    while(max_value > 0){
        //sorts the number based on the digit
        for(int k = 0; k < m; k++){
            num = data[k];
            index = (int)(num / divisor) %10;
            radix_array[index][0]++;
            current_size = radix_array[index][0];
            radix_array[index][current_size] = num;
            //printf("index: %d, current_size: %d, radix: %d\n", index, current_size, radix_array[index][current_size]);
        }
        // Puts the new sorted data in the input again.
        arr_pointer = 0;
        for(int l = 0; l < 10; l++){
            current_size = radix_array[l][0];
            for(int x = 1; x < current_size+1; x++){
                data[arr_pointer++] = radix_array[l][x];
            }
            // reset the counter
            radix_array[l][0] = 0;
        }
        max_value /= 10;
        divisor *= 10;
    }

    //free radix array
    for(int i=0; i<10; i++){
        free(radix_array[i]);
    }
    free(radix_array);

    print_array(data, m);

    return EXIT_SUCCESS;
}

int main(int argc, char *argv[]){
    FILE *fileptr;
    char filename[50];
    if(argc < 2){
        printf("Please enter the filename: ");
        scanf("%s", filename);
    }
    else{
        strcpy(filename, argv[1]);
    }

    fileptr = fopen(filename, "r");

    if(fileptr == NULL){
        perror("File not found. Invalid input.\n");
        return EXIT_FAILURE;
    }

    int temp, count = 0;

    while(fscanf(fileptr, "%d", &temp)==1){
        count++;
    }

    rewind(fileptr);

    int *numsarray = (int *)malloc(count * sizeof(int));

    if(numsarray == NULL){
        perror("Memory allocation failed.\n");
        fclose(fileptr);
        return EXIT_FAILURE;
    }
    for(int i = 0; i < count; i++){
        if(fscanf(fileptr, "%d", &numsarray[i]) != 1){
            printf("Unable to read the entry at %d. File format might be incorrect.\n", i);
            fclose(fileptr);
            free(numsarray);
            return EXIT_FAILURE;
        }
    }

    print_array(numsarray, count);

    radix_sort(numsarray, count);

    return EXIT_SUCCESS;
}

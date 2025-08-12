#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "misc_codes.h"

void counting_sort(int *data, int n, int max_value){
    int *count_array = (int *)calloc((max_value+1), sizeof(int));

    for(int i = 0; i < n; i++){
        count_array[data[i]]++;
    }

    int j = 0, k = 0;
    for(int l = 0; l < max_value+1; l++){
        j = count_array[l];
        while(j > 0 && k < n){
            data[k] = l;
            j--;
            k++;
        }
    }
    print_array(data, n);
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
        printf("File not found. Invalid input.\n");
        return EXIT_FAILURE;
    }

    // read the size of data.
    int temp, count = 0, max_value;
    while(fscanf(fileptr, "%d", &temp)==1){
        if(count == 0){
            max_value = temp;
        }
        if(temp > max_value){
            max_value = temp;
        }

        count++;
    }

    rewind(fileptr);

    // initializing array.
    int *numsarray = (int *)malloc(count * sizeof(int));
    for(int i = 0; i < count; i++){
        if(fscanf(fileptr, "%d", &numsarray[i]) != 1){
            printf("Unable to read entry at %d. File format might be incorrect.\n", i);
            free(numsarray);
            fclose(fileptr);
            return EXIT_FAILURE;
        }
    }
    fclose(fileptr);
    printf("File Closed.\n");

    print_array(numsarray, count);

    counting_sort(numsarray, count, max_value);

    free(numsarray);

    return EXIT_SUCCESS;
}

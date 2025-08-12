#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "misc_codes.h"

int partition(int *data, int low, int high){
    int r_index = low+(rand()%(high-low+1));
    swap_num(data, r_index, high);
    int pivot = data[high];
    int j = low -1;
    for(int i=low; i< high; i++){
        if(data[i]<pivot){
            j++;
            swap_num(data, i, j);
        }
    }
    swap_num(data, j+1, high);
    return j+1;
}

void quick_sort(int *data, int low_index, int high_index){
    if(low_index < high_index){
        int pivot = partition(data, low_index, high_index);
        quick_sort(data, low_index, pivot-1);
        quick_sort(data, pivot+1, high_index);
    }
}

int main(int argc, char *argv[]){
    FILE *fileptr;
    char filename[50];
    if(argc < 2){
        printf("Enter the file name: ");
        scanf("%s", filename);
    }
    else{
        strcpy(filename, argv[1]);
    }

    fileptr = fopen(filename, "r");
    if(fileptr == NULL){
        printf("File not found.\n");
        return EXIT_FAILURE;
    }

    //counting the number of entries.
    int count=0, temp;
    while(fscanf(fileptr, "%d", &temp) == 1){
        count++;
    }
    rewind(fileptr);
    //Intializing array to enter data.
    int *numsarray = (int *)malloc(count * sizeof(int));

    if(numsarray == NULL){
        printf("Memory intialization failed.\n");
        fclose(fileptr);
        return EXIT_FAILURE;
    }

    for(int i = 0; i < count; i++){
        if(fscanf(fileptr, "%d", &numsarray[i]) != 1){
            printf("Failed to read file at %d. File format might be incorrect.\n", i);
            fclose(fileptr);
            free(numsarray);
            return EXIT_FAILURE;
        }
    }

    print_array(numsarray, count);

    srand(time(NULL));

    quick_sort(numsarray, 0, count-1);

    print_array(numsarray, count);

    return EXIT_SUCCESS;

}

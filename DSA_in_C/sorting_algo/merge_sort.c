#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "misc_codes.h"

void merge(int *data, int start, int mid, int end){
    int *sorted_arr = (int *)malloc((end-start+1)*sizeof(int));
    int i = start, j = mid+1, k = 0;
    while(i <= mid && j <= end){
        if(data[i] < data[j]){
            sorted_arr[k++] = data[i++];
        }
        else{
            sorted_arr[k++] = data[j++];
        }
    }

    while(i <= mid){
        sorted_arr[k++] = data[i++];
    }

    while (j <= end){
        sorted_arr[k++] = data[j++];
    }

    for(int n = 0; n < k; n++){
        data[start + n] = sorted_arr[n];
    }

    free(sorted_arr);

}

void merge_sort(int *data, int start, int end){
    if(start < end){
        int mid = (start+end)/2;
        merge_sort(data, start, mid);
        merge_sort(data, mid+1, end);
        merge(data, start, mid, end);
    }
}

int main(int argc, char *argv[]){
    FILE *fileptr;

    if(argc < 2){
        perror("Enter filename and try again!!!\n");
        return EXIT_FAILURE;
    }

    fileptr = fopen(argv[1], "r");

    if(fileptr == NULL){
        perror("File not found.\n");
        return EXIT_FAILURE;
    }

    int temp, count = 0;

    while(fscanf(fileptr, "%d", &temp) == 1){
        count++;
    }

    rewind(fileptr);

    int *numsarray = (int *)malloc(count * sizeof(int));

    if(numsarray == NULL){
        perror("Memory allocation failed.\n");
        fclose(fileptr);
        return EXIT_FAILURE;
    }

    for(int i=0; i < count; i++){
        if(fscanf(fileptr, "%d", &numsarray[i]) != 1){
            printf("Error reading the entry at %d. FIle format might be wrong.\n", i);
            fclose(fileptr);
            free(numsarray);
            return EXIT_FAILURE;
        }
    }

    print_array(numsarray, count);

    merge_sort(numsarray, 0, count-1);

    print_array(numsarray, count);

    free(numsarray);

    return EXIT_SUCCESS;

}

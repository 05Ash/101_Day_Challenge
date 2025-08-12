#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "misc_codes.h"

int insertion_sort(int *data, int m){
    int j, temp;
    for(int i = 1; i < m; i ++){
        j = i;
        // insert the data in the correct position
        while((j>0) && data[j] < data[j-1]){
            temp = data[j];
            data[j] = data[j-1];
            data[j-1] = temp;
            j--;
            //printf("%d, %d, %d\n", data[j], data[j-1], temp);
        }
    }
    print_array(data, m);
    return 0;
}

int main(int argc, char *argv[]){
    FILE *fileptr;
    char filename[50];
    if(argc < 2){
        //Get the name of the file if name not given
        printf("Enter file name: ");
        scanf("%s", filename);
    }
    else{
        strcpy(filename, argv[1]);
    }

    fileptr =  fopen(filename, "r");
    if(fileptr == NULL){
        printf("Error opening the file.\n");
        return EXIT_FAILURE;
    }
    //count the number of entries in file
    int count = 0, temp;
    while(fscanf(fileptr, "%d", &temp)==1){
        count++;
    }

    rewind(fileptr);

    //initialize array to store data

    int *numarray = (int *)malloc(count * sizeof(int));
    for(int i = 0; i < count; i++){
        if(fscanf(fileptr, "%d", &numarray[i]) != 1){
            printf("Error reading the entry at %d. Incorrect file formad.\n", i);
            fclose(fileptr);
            free(numarray);
            return EXIT_FAILURE;
        }
    }
    fclose(fileptr);
    printf("File closed.\n");

    print_array(numarray, count);

    insertion_sort(numarray, count);

    free(numarray);
    printf("\n");

    return 0;
}

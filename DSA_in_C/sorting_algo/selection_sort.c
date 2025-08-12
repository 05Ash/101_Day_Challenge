#include <stdio.h>
#include <stdlib.h>

int print_arr(int *data, int m){
    for(int i = 0; i < m; i++){
        printf("%d\t", data[i]);
    }
    printf("\n");
    return 0;
}

int selection_sort(int *data, int m){
    int index, temp, exchanged;
    for(int i = 0; i < m; i++){
        index = i;
        exchanged = 0;
        for(int j = i; j < m; j++){
            if(data[index] > data[j]){
                index = j;
                exchanged = 1;
            }
        }
        if(exchanged){
            temp = data[i];
            data[i] = data[index];
            data[index] = temp;
        }
    }
    print_arr(data, m);
    return 0;
}

int main(){
    FILE *fileptr;
    char filename[50];

    printf("Enter file name: ");
    scanf("%s", filename);
    printf("%s\n", filename);

    fileptr = fopen(filename, "r");
    if(fileptr == NULL){
        printf("Invalid file name.\n");
        return EXIT_FAILURE;
    }
    //Checking for number of elements in file
    int temp, count = 0;
    while(fscanf(fileptr, "%d", &temp) == 1){
        count++;
    }
    rewind(fileptr);

    int *num_array = (int *)malloc(count * sizeof(int));

    if(num_array == NULL){
        printf("Memory allocation failed.\n");
        return EXIT_FAILURE;
    }

    printf("Successfully allocated memory.\n");

    printf("Reading numbers\n");

    for(int j = 0; j < count; j++){
        if(fscanf(fileptr, "%d", &num_array[j]) != 1){
            printf("Error reading %d number from the file. File format might be incorrect.\n", j);
            free(num_array);
            fclose(fileptr);
            return EXIT_FAILURE;
        }
    }

    fclose(fileptr);
    printf("File closed.\n");

    print_arr(num_array, count);

    selection_sort(num_array, count);

    free(num_array);

    return 0;
}

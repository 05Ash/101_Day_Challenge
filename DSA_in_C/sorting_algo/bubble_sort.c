#include <stdio.h>
#include <stdlib.h>

void print_Array(int *data, int m){
    for(int i = 0; i < m; i++){
        printf("%d\t", data[i]);
    }
    printf("\n");
}

int bubble_sort(int *data, int m){
    // Sort array using bubble sort
    int temp, passed;

    for(int i = 0; i < (m-1); i++){

        passed = 0;
        for(int j = 0; j < (m-i-1); j++){

            if(data[j] > data[j+1]){
                temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;
                passed = 1;
            }
        }

        if(!passed)
            break;
    }
    return 0;
}

int main(){
    //Intialize file pointer, and get filename
    FILE *file_ptr;
    char filename[50];
    printf("Enter the filename: ");
    scanf("%s", filename);
    printf("%s\n", filename);

    file_ptr = fopen(filename, "r");

    if(file_ptr == NULL){
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    // read the number of elements in file
    int tempnum, count = 0;

    while(fscanf(file_ptr, "%d", &tempnum) == 1){
        count++;
    }
    // We need to rewind it to read from the beginning again.
    rewind(file_ptr);

    //Initialize array
    int *num_arr = (int *)malloc(count * sizeof(int));

    if(num_arr==NULL){
        printf("Memory allocation failed.\n");
        return EXIT_FAILURE;
    }

    printf("Successfully allocated memory for %d numbers.\n", count);

    printf("Reading numbers from file.\n");

    for(int i = 0; i < count; i++){
        if(fscanf(file_ptr, "%d", &num_arr[i]) != 1){
            printf("Error reading number at position %d. File format might be incorrect.\n", i);
            free(num_arr);
            fclose(file_ptr);
            return EXIT_FAILURE;
        }
    }

    fclose(file_ptr);
    printf("File closed.\n");

    print_Array(num_arr, count);
    bubble_sort(num_arr, count);
    print_Array(num_arr, count);

    free(num_arr);


}

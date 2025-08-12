#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]){
    int count = 0, min_val = 0, max_val = 10;
    if(argc < 2){
        printf("Enter how many numbers to generate:");
        scanf("%d", &count);
    }
    else{
        count = atoi(argv[1]);
    }

    FILE *file_ptr;
    char filename[] = "data.txt";
    file_ptr = fopen(filename, "w");

    if(file_ptr == NULL){
        perror("Error opening file to write.\n");
        return EXIT_FAILURE;
    }
    srand(time(NULL));
    for(int i = 0; i < count; i++){
        int random_num = (rand()%(max_val - min_val + 1) + min_val);
        fprintf(file_ptr, "%d\t", random_num);
        printf("%d\t", random_num);
    }

    printf("\n");

    fclose(file_ptr);
    return EXIT_SUCCESS;
}

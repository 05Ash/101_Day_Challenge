#include<stdio.h>
#include<stdlib.h>

typedef struct Stack{
    int *S; //Pointer to the start
    int top;
    int max; //Denotes the top index or end of the stack
}Stack;

void create_stack(Stack *arr, int size);
int is_empty(Stack *arr);
int is_full(Stack *arr);
void push(Stack *arr, int element);
int pop(Stack *arr);


int main(int argc, char *argv[]){
    int n = 0;
    printf("Enter the size of the stack you want to create:");
    scanf("%d", &n);
    Stack x;
    create_stack(&x, n);
    int i = 0;
    printf("%s\n", argv[1]);

    return 0;
}

//Create a stack of given length
void create_stack(Stack *arr, int size){
    arr->S = (int *)malloc(size*sizeof(int));
    if(arr->S == NULL){
        printf("Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    arr->top = -1;
    arr->max = size;
}

//Check if the stack is empty or not
int is_empty(Stack *arr){
    return arr->top < 0;
}


//Check if full
int is_full(Stack *arr){
    return arr->top == arr->max;
}
//Push an element to the end of the stack and updates the top
void push(Stack *arr, int element){
    int full = is_full(arr);
    if(full == 0){
        arr->top = arr->top + 1;
        arr->S[arr->top] = element;
    }
}

// pop the last element and decrease the top position by 1
int pop(Stack *arr){
    arr->top = arr->top - 1;
    return arr->S[arr->top+1];
}

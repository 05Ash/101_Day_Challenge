#include "linked_list.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char *argv[]){
    if(argc < 2){
        printf("No arguments entered.\n");
        return EXIT_FAILURE;
    }
    Node *head = arguments_to_list(argv, argc);
    Node *reverse_head = copy_list(head);
    reverse_list(&reverse_head);
    if(is_identical(head, reverse_head)){
        printf("The given list is a palindrome.\n");
    }
    else{
        printf("The given list is not a palindrome.\n");
    }
    traverse_list(head);
    traverse_list(reverse_head);
    return 0;
}

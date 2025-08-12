#include "linked_list.h"
#include <stdlib.h>
#include <stdio.h>

void remove_duplicates(Node *head){
    printf("Current ");
    traverse_list(head);
    if(head == NULL){
        printf("List is empty.\n");
    }
    Node *current_ptr = head, *next_ptr = NULL;
    while(current_ptr->next != NULL){
        next_ptr = current_ptr->next;
        if(current_ptr->data == next_ptr->data){
            current_ptr->next = next_ptr->next;
            free(next_ptr);
        }
        else{
            current_ptr = next_ptr;
        }
    }
    printf("New ");
    traverse_list(head);
}

int main(int argc, char *argv[]){
    Node *head = NULL;
    int num = 0;
    if(argc < 2){
        int count = 0;
        printf("Please enter the length of the list:\t");
        scanf("%d", &count);
        for(int i = 0; i < count; i++){
            printf("Enter the data for the node %d:\t", i+1);
            scanf("%d", &num);
            if( head == NULL){
                head = create_node(num);
            }
            else{
                insert_at_end(num, &head);
            }
        }
    }
    for(int i = 1; i < argc; i++){
        num = atoi(argv[i]);
        if(head == NULL){
            head = create_node(num);
        }
        else{
            insert_at_end(num, &head);
        }
    }

    remove_duplicates(head);

    return 0;
}

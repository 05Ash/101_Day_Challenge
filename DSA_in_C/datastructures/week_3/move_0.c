#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
    struct Node *prev;
}Node;

Node *create_node(int data){
    Node *new_node = (Node *)malloc(sizeof(Node));
    if(new_node == NULL){
        printf("Memory allocation failed for %d!!!!\n", data);
        exit(EXIT_FAILURE);
    }
    new_node->data = data;
    new_node->prev = NULL;
    new_node->next = NULL;

    return new_node;
}

int insert_at_beginning(int data, Node **head_ref, Node **tail_ref){
    Node *new_node = create_node(data);
    if(*head_ref == NULL){
        *tail_ref = new_node;
    }
    else{
        new_node->next = *head_ref;
        (*head_ref)->prev = new_node;
    }
    *head_ref = new_node;
    return 0;
}

int insert_at_tail(int data, Node **head_ref, Node **tail_ref){
    Node *new_node = create_node(data);
    if(*head_ref == NULL){
        *head_ref = new_node;
    }
    else{
        (*tail_ref)->next = new_node;
        new_node->prev = *tail_ref;
    }
    *tail_ref = new_node;
    return 0;
}

//delets the node and returns the data
int delete_node(Node *target_node, Node **head_ref, Node **tail_ref){
    int temp = target_node->data;
    if(target_node->prev != NULL) target_node->prev->next = target_node->next;
    else *head_ref = target_node->next;
    if(target_node->next != NULL) target_node->next->prev = target_node->prev;
    else *tail_ref = target_node->prev;
    target_node->next = NULL;
    target_node->prev = NULL;
    free(target_node);
    return temp;
}

//Insert a node at given target
int insert_after(int data, Node *target_node, Node **tail_ref){
    Node *new_node = create_node(data);
    new_node->next = target_node->next;
    new_node->prev = target_node;
    target_node->next = new_node;
    if(new_node->next != NULL){
        new_node->next->prev = new_node;
    }
    else{
        *tail_ref = new_node;
    }
    return 0;
}

int traverse_list(Node *head){
    Node *current_ptr = head;
    printf("Linked List: ");
    if(head == NULL) printf("EMPTY!\n");
    else printf("\n");
    while(current_ptr!= NULL){
        printf("%d\t", current_ptr->data);
        current_ptr = current_ptr->next;
    }
    printf("\n");
    return 0;
}

//Clears the list
int clear_list(Node **head_ref, Node **tail_ref){
    Node *current_ptr = *head_ref, *temp = NULL;
    while(current_ptr != NULL){
        temp = current_ptr->next;
        free(current_ptr);
        current_ptr = temp;
    }
    free(temp);
    *head_ref = NULL;
    *tail_ref = NULL;
    return 0;
}

int main(int argc, char *argv[]){
    if(argc < 2){
        printf("No argument entered.\n");
        return EXIT_FAILURE;
    }
    Node *head = NULL, *tail = NULL;
    Node *current_ptr = NULL, *new_node = NULL;
    int data = 0;
    for(int i = 1; i < argc; i++){
        data = atoi(argv[i]);
        if(head == NULL){
            head = tail = create_node(data);
        }
        else{
            insert_at_tail(data, &head, &tail);
        }
    }
    traverse_list(head);
    current_ptr = head;
    Node *prev_ptr = NULL;
    int count_zero = 0;
    while(current_ptr != NULL){
        prev_ptr = current_ptr;
        current_ptr = current_ptr->next;
        if(prev_ptr->data == 0){
            count_zero++;
            delete_node(prev_ptr, &head, &tail);
        }
    }
    for(int i = 0; i < count_zero; i++){
        insert_at_tail(0, &head, &tail);
    }
    traverse_list(head);
    clear_list(&head, &tail);
    return 0;
}

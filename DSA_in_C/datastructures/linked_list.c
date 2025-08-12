//#include "linked_list.h"
#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
    /* data */
    int data;
    struct Node* next;
}Node;

//Creates a node for a given data

Node* create_node(int data){
    Node* new_node = (Node *)malloc(sizeof(Node));
    if(new_node == NULL){
        printf("Memory Allocation Failed.\n");
        //Terminates the program on failure
        exit(EXIT_FAILURE);
    }
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

//Count and returns the number of heads given the head pointer
int count_nodes(Node *head){
    int count = 0;
    Node *current_ptr = head;
    //Runs the loop until the end of the list
    while(current_ptr != NULL){
        count++;
        current_ptr = current_ptr->next;
    }
    return count;
}

//Check if the list is empty and returns True(1) of False(0)
int is_empty(Node *head){
    if(head == NULL){
        printf("List is empty.\n");
        return 1;
    }
    else{
        printf("List is not empty.\n");
        return 0;
    }
}

//Traverse the entire list and prints the elements
void traverse_list(Node *head){
    Node *current_ptr = head;
    if(head == NULL){
        printf("Linked List: EMPTY\n");
    }
    else{
        printf("Linked List:\n");
        while(current_ptr != NULL){
            printf("\t%d", current_ptr->data);
            current_ptr = current_ptr->next;
        }
        printf("\n");
    }
}

//Inserts a node at a given index
int insert_at(int element, int index, Node **head_ref){
    Node *current_ptr = *head_ref;
    int count = count_nodes(*head_ref);
    if(index < 0){
        printf("Invalid index.\n");
        exit(EXIT_FAILURE);
    }
    Node *new_node = create_node(element);
    if(index == 0 || *head_ref == NULL){
        if(*head_ref == NULL){
            printf("List is empty. ");
        }
        printf("Inserting at the beginning of the list.\n");
        new_node->next = *head_ref;
        *head_ref = new_node;
        return 0;
    }
    if(index > count){
        //checks if the index is given greater than the length of the list
        index = count;
        printf("Index given is greater than count.\nInserting the node at the end.\n");
    }
    for(int i = 0; i < index-1; i++){
        if(current_ptr == NULL){
            printf("Cannot insert at the given index, as list prematurely terminated before reaching the specified index.\n");
            free(new_node);
            exit(EXIT_FAILURE);
        }
        current_ptr = current_ptr->next;
    }
    new_node->next = current_ptr->next;
    current_ptr->next = new_node;
    return 0;
}


//inserts at the begging of the list
void insert_at_beginning(int data, Node **head_ref){
    insert_at(data, 0, head_ref);
}

//Insert at the end of the list
void insert_at_end(int data, Node **head_ref){
    int index = count_nodes(*head_ref);
    insert_at(data, index, head_ref);
}

//Search for a given element in the list, if it's present returns index, else returns -1
int search_list(int data, Node *head){
    Node *current_ptr = head;
    int index = 0;
    while(current_ptr != NULL){
        if(current_ptr->data = data){
            printf("%d found at index: %d\n", data, index);
            return index;
        }
        index++;
        current_ptr = current_ptr->next;
    }
    printf("%d is not present in the list.\n", data);
    return -1;
}

//Delets a node in the list
int delete_node(int data, Node **head_ref){
    int index = search_list(data, *head_ref);
    if(index < 0){
        return -1;
    }
    Node *current_ptr = *head_ref, *prev_ptr = NULL;
    if(index == 0){
        *head_ref = current_ptr->next;
        free(current_ptr);
        return 0;
    }
    for(int i=0; i < index; i++){
        prev_ptr = current_ptr;
        current_ptr = current_ptr->next;
    }
    prev_ptr->next = current_ptr->next;
    free(current_ptr);
    return 0;
}

//Clears a linked list
int clear_list(Node **head_ref){
    Node *current_ptr = *head_ref, *next_ptr = NULL;
    while(current_ptr != NULL){
        next_ptr = current_ptr->next;
        free(current_ptr);
        current_ptr = next_ptr;
    }
    *head_ref = NULL;
    printf("Linked list cleared successfully.\n");
    return 0;
}

int reverse_list(Node **head_ref){
    Node *current_ptr = *head_ref, *next_ptr = NULL, *prev_ptr = NULL;
    if(count_nodes(current_ptr)<=1){
        printf("List is empty or has one node. No reversal needed.\n");
        return 0;
    }
    while(current_ptr!= NULL){
        //moves the ptr to next node
        next_ptr = current_ptr->next;
        //points the current_ptr.next to prev_ptr
        current_ptr->next = prev_ptr;
        //points the prev_ptr to current node
        prev_ptr = current_ptr;
        //points the current_ptr to next node
        current_ptr = next_ptr;
    }
    //update the head_ptr to the ptr to the last node
    *head_ref = prev_ptr;
    printf("Linked list reversed successfully.\n");
    return 0;
}

//Merges list 1 to list 2 and resets the head pointer to list2 to NULL
int merge_lists(Node **list1_ref, Node **list2_ref){
    if(list1_ref == NULL || list2_ref == NULL){
        printf("Invalid reference pointers.\n");
        return -1;
    }
    if(*list2_ref == NULL){
        printf("List 2 is empty. No needed to merge anything.\n");
        return 0;
    }
    if(*list1_ref == NULL){
        *list1_ref = *list2_ref;
        *list2_ref = NULL;
    }
    else{
        Node *current_ptr = *list1_ref;
        while(current_ptr->next != NULL){
            current_ptr = current_ptr->next;
        }
        current_ptr->next = *list2_ref;
        *list2_ref = NULL;
    }

    printf("List 2 successfully combined to list 1.\n");
    return 0;
}

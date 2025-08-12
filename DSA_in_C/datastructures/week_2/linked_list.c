#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
    int data;
    struct Node* next;
}Node;

//Function declaration
Node* create_node(int);
void insert_new(Node *, int);
void traverse_list(Node *);
void insert_beginning(Node **, int);
int search(Node *, int);
int delete_node(Node **, int);
void insert_after(Node *, int, int);
int count_nodes(Node *);
void reverse_list(Node **);
void concat_2_list(Node *, Node *);
int find_middle(Node *);
int node_at(Node *, int);
int is_empty(Node *);
void clear_list(Node **);


int main(int argc, char *argv[]){
    FILE *fileptr;
    if(argc < 2){
        printf("Enter the file name.\n");
        return EXIT_FAILURE;
    }

    fileptr = fopen(argv[1], "r");
    if(!fileptr){
        printf("File not found.\n");
        return EXIT_FAILURE;
    }

    int temp;
    Node *head = NULL;
    while(fscanf(fileptr, "%d", &temp) == 1){
        if(head == NULL){
            head = create_node(temp);
        }
        else{
            insert_new(head, temp);
        }
    }

    printf("Created the linked list.\n");
    fclose(fileptr);
    printf("File Closed.\n");
    traverse_list(head);
    clear_list(&head);
    printf("%d\n", is_empty(head));
    return EXIT_SUCCESS;

}




//Creates a new node
Node* create_node(int data){
    Node* newnode = (Node *)malloc(sizeof(Node));
    if(!newnode){
        printf("Memory allocation failed for Node with data %d.", data);
        exit(1);
    }
    newnode->data = data;
    newnode->next = NULL;
    return newnode;
}

//Insert a new node at the end of the list
void insert_new(Node *head, int data){
    Node *next_node = create_node(data);
    Node *current_node = head;
    while(current_node->next){
        current_node = current_node->next;
    }
    current_node->next = next_node;
}

//Traverse the list forward, and print the corresponding data
void traverse_list(Node *head){
    Node *current_node = head;
    printf("Linked List.\n\n");
    while(current_node != NULL){
        printf("%d\t", current_node->data);
        current_node = current_node->next;
    }
    printf("\n\n");
}

//Insert data at the begining of the list
void insert_beginning(Node **head_ref, int data){
    Node *new_node = create_node(data);
    new_node->next = *head_ref;
    *head_ref = new_node;
}

//Search for an element in the linked list and returns the index if not found, else -1
int search(Node *head, int element){
    Node *current_node = head;
    int index = 0;
    while(current_node){
        if(current_node->data == element){
            printf("Element %d found in the linked list at index %d.\n", element, index);
            return index;
        }
        else{
            current_node = current_node->next;
            index++;
        }
    }
    printf("Element not present in the linked list.\n");
    return -1;
}

//Deletes an element from the list and returns the index if present
int delete_node(Node **head, int element){
    Node *current_node = *head, *next_node = NULL, *prev_node = *head;
    int index = 0;
    while(current_node){
        next_node = current_node->next;
        if(current_node->data == element){
            if(prev_node == NULL){
                *head = next_node;
            }
            else if(next_node == NULL){
                prev_node->next == NULL;
            }
            else{
                prev_node->next = next_node;
            }
            printf("Element found at position %d, and deleted.\n", index);
            index++;
            free(current_node);
            return index;
        }
        prev_node = current_node;
        current_node =  current_node->next;
        index++;
    }
    printf("Element not present in the list.\n");
    return -1;
}

//Insert a nodes for a given index
void insert_after(Node *head, int index, int element){
    Node *current_node = head, *next_node = NULL;
    int count = 0;
    Node *new_node = create_node(element);
    while(current_node){
        next_node = current_node->next;
        if(count == index){
            current_node->next = new_node;
            new_node->next = next_node;
            printf("Element inserted at index %d.\n", index);
            break;
        }
        current_node = current_node->next;
        count++;
    }
}



//Count number of nodes in the list
int count_nodes(Node *head){
    Node *current_node = head;
    int count = 0;
    while(current_node){
        current_node = current_node->next;
        count++;
    }
    printf("There are a total no. of %d elements in the list.\n", count);
    return count;
}

//Reverse the entire list.
void reverse_list(Node **head){
    Node *current_node = *head, *prev_node = NULL, *next_node = NULL;
    while(current_node){
        next_node = current_node->next;
        current_node->next = prev_node;
        prev_node = current_node;
        current_node = next_node;
    }
    *head = prev_node;
}


//Concatenate second list to the first list

void concat_2_list(Node *list1, Node *list2){
    Node *current_head = list1;
    while(current_head->next){
        current_head = current_head->next;
    }
    current_head->next = list2;
}

//print the data of the node at a given index and return the data
int node_at(Node *head, int index){
    int count = 0;
    Node *curr_node = head;
    while(curr_node){
        if(count == index){
            printf("Data at index %d: %d\n", count, curr_node->data);
            return curr_node->data;
        }
        count++;
        curr_node = curr_node->next;
    }
    printf("Out of bound.\n");
    return EXIT_FAILURE;

}

//Find the middle node, print the data, and return the index.
int find_middle(Node *head){
    int count = count_nodes(head);
    int mid_index = count/2;
    node_at(head, mid_index);
    return mid_index;

}

//Check if the linked list is empty
int is_empty(Node *head){
    return (head == NULL);
}

//Clears the entire list and frees the memory.

void clear_list(Node **head){
    Node *curr_node = *head, *prev_node = NULL;
    while(curr_node){
        prev_node = curr_node;
        curr_node = curr_node->next;
        free(prev_node);
    }
    *head = NULL;
}

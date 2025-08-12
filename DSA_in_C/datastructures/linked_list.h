#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct Node{
    int data;
    struct Node *next;
}Node;

Node* create_node(int data);
int count_nodes(Node *head);
int is_empty(Node *head);
void traverse_list(Node *head);
int insert_at(int element, int index, Node **head_ref);
void insert_at_beginning(int data, Node **head_ref);
void insert_at_end(int data, Node **head_ref);
int search_list(int data, Node *head);
int delete_node(int data, Node **head_ref);
int clear_list(Node **head_ref);
int reverse_list(Node **head_ref);
int merge_lists(Node **list1_ref, Node **list2_ref);

#endif

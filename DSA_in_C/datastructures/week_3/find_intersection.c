#include "linked_list.h"
#include <stdio.h>
#include <stdlib.h>

int main(){
    int arr1[6] = {1,2,6,3,4,5}, arr2[4] = {5,3,4,6};
    Node *list1 = array_to_list(arr1, 6), *list2 = array_to_list(arr2, 4);
    int len1 = count_nodes(list1), len2 = count_nodes(list2), i = len1, k = 0, intersect, found_common = 0;
    reverse_list(&list1);
    reverse_list(&list2);
    Node *l1_curr = list1, *l2_curr = list2;
    if(len1 > len2) i = len2;
    while(k < i){
        if(l1_curr->data != l2_curr->data){
            break;
        }
        intersect = l1_curr->data;
        l1_curr = l1_curr->next;
        l2_curr = l2_curr->next;
        found_common = 1;
        k++;
    }
    if(!found_common){
        printf("Intersection not found.\n");
    }
    else{
        printf("Intersection found at %d.\n", intersect);
    }

    return 0;
}

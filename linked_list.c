#include <stdio.h> 
#include <stdlib.h>

struct Node { 
	const char* data; 
	struct Node* next; 
};

struct LinkedList {
	struct Node* head;
    // struct Node* tail;	
};


void add_data(struct LinkedList* ll, const char* data) {
	if (ll == NULL || data == NULL) { return; }
	
	struct Node* node = malloc(sizeof(struct Node)); 
	if (node == NULL) { return; } 
	
	node->data = data; 
	if (ll->head == NULL) {
		ll->head = node;
	}
	else {
		node->next = ll->head;
		ll->head = node;
	}
	
}

int get_size(const struct LinkedList* ll) {
    int count = 0;
    struct Node* current = ll->head;
    if (current == NULL) { return 0;}
    
    for (int i = 0; current != NULL; i++) {
	    current = current->next;
	    count++;
    }	    
    return count;
}

void get_elements(const struct LinkedList* ll) {
	struct Node* current = ll->head;
	for (int i = 0; i < get_size(ll); i++) {
		if (current == NULL) { break; }
		printf("Node index %d, data: %s\n", i, (current->data));
		current = current->next;
	}
}

void free_nodes(struct LinkedList* ll) {
    struct Node* current = ll->head;
	if (current == NULL) {
		return; // 1st edge case: empty list
	}
	else if (current->next == NULL) {
		free(current); //2nd edge case: list with only one element
		return;
	}
	else {
		struct Node* previous = NULL;
		while (current != NULL) {
			previous = current;
			current = current->next;
			free(previous);
		}
	}
}

void delete_node(struct LinkedList* ll, const int index) {
	int size =  get_size(ll);
	if (index < 0 || index > size) {
		return;
	}
	
	struct Node* current = ll->head;
	if (index == 0) {
		ll->head = current->next;
		free(current);
		return;
	}

	struct Node* previous = NULL;
	for (int i = 0; i < size; i++) {
		if (i == index - 1) {
			previous = current;
		}
		else if (i == index) {
			if (current->next == NULL) {
				previous->next = NULL;
			}
			else {
				previous->next = current->next;
			}
			
			free(current);
			break;
		}
		current = current->next;
	}
}

int main() {
	struct LinkedList ll;
	ll.head = NULL; 
	// ll.tail = NULL;

	const char* d1 = "Hello";
	const char* d2 = "World";

	add_data(&ll, d1);
	add_data(&ll, d2);

	get_elements(&ll);
	printf("Size: %d\n", get_size(&ll));
	delete_node(&ll, 0);
	printf("Size after deletion: %d\n", get_size(&ll));
	get_elements(&ll);
	
	free_nodes(&ll);
	return 0;
}

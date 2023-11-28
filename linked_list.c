#include <stdio.h> 
#include <stdlib.h>

struct Node { 
	const char* data; 
	struct Node* next; 
};

struct LinkedList {
	struct Node* head;
    struct Node* tail;	
};


void add_data(struct LinkedList* ll, const char* data) {
	if (ll == NULL || data == NULL) { return; }
	
	struct Node* node = malloc(sizeof(struct Node)); 
	if (node == NULL) { return; } // Handle malloc failure
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

void get_elements(struct LinkedList* ll) {
	struct Node* current = ll->head;
	for (int i = 0; i < get_size(ll); i++) {
		if (current == NULL) { break; }
		printf("Node %d, element: %s\n", i, (current->data));
		current = current->next;
	}

}

void free_nodes(struct LinkedList* ll) {
    struct Node* current = ll->head;
	struct Node* next = current->next;
    if (current == NULL || next == NULL) { return;}
    
    for (int i = 0; next != NULL; i++) {
		free(current);
	    next = next->next;
    }	
}

int main() {
	struct LinkedList ll;
	ll.head = NULL; 
	ll.tail = NULL;

	const char* d1 = "Hello";
	const char* d2 = "World";

	add_data(&ll, d1);
	add_data(&ll, d2);

	get_elements(&ll);
	free_nodes(&ll);

	return 0;
}

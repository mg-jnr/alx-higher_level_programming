#ifndef LIST_H
#define LIST_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list (DSA)
 * @n: integer (int)
 * @next: points to the next node(Node)
 *
 * Description: singly linked list node structure (DSA for C)
 *
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

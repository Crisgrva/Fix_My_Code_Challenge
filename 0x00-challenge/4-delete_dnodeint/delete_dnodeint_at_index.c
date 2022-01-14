#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *aux1 = *head, *aux2 = *head, *to_delete = *head;
	unsigned int node = 0;

	if (*head == NULL)
		return (-1);
	if (index == 0)
	{
		if ((*head)->next != NULL)
		{
			aux1->next->prev = NULL;
			*head = (*head)->next;
		}
		else
			*head = NULL;
		free(to_delete);
		return (1);
	}
	to_delete = to_delete->next;
	aux2 = aux2->next;
	while (aux2 && node < (index - 1))
	{
		node++;
		aux1 = aux1->next;
		aux2 = aux2->next;
		to_delete = to_delete->next;
	}
	if (node == (index - 1))
	{
		aux1->next = aux2->next;
		if (aux2->next != NULL)
			aux2->next->prev = aux1;
		free(to_delete);
		return (1);
	}
	return (-1);
}

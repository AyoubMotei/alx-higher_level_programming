#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks cycle
 * @list: giving list
 *
 * Return: 0 (success)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

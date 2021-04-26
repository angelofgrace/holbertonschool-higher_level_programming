#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


int check_cycle(listint_t *list)
{

	listint_t *tortoise_tmp = NULL;
	listint_t *hare_tmp = NULL;

	tortoise_tmp = list;
	hare_tmp = list;
	while (tortoise_tmp && hare_tmp && hare_tmp->next)
	{
		tortoise_tmp = tortoise_tmp->next;
		hare_tmp = hare_tmp->next->next;
		if (tortoise_tmp == hare_tmp)
		{
			return (1);
		}	
	}
	return (0);
}

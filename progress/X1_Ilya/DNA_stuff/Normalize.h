#ifndef _INC_NORMALIZE
#define _INC_NORMALIZE

#include <math.h>

void normalizeDnaProbTable(double* table, int k)
{
	int sum = 0;
	for (int i = 0; i < pow(4, k); i++)
	{
		sum += table[i];
		if ((i + 1) % 4 == 0)
		{
			table[i] /= sum;
			table[i - 1] /= sum;
			table[i - 2] /= sum;
			table[i - 3] /= sum;

			sum = 0;
		}
	}
}

#endif

#ifndef _INC_COMBO_COUNTER
#define _INC_COMBO_COUNTER

#include <cctype>

enum nuc { A, T, G, C, N };

void countCombo(char* tok, double* table, const int k)
{
	assert(tok);
	assert(table);

	nuc* combo = new nuc[k];
	bool readable = true;
	
	for (int i = 0; tok[i + k - 1]; i++)
	{
		for (int j = 0; j < k; j++)
		{
			switch (tok[i + j])
			{
			case 'A':
				combo[j] = A;
				break;

			case 'T':
				combo[j] = T;
				break;

			case 'G':
				combo[j] = G;
				break;

			case 'C':
				combo[j] = C;
				break;
			default:
				readable = false;
				break;
			}
		}

		int curTablePos = 0;
		for (int j = 0; j < k && readable; j++)
			curTablePos += pow(4, j) * combo[j];

		if (readable) table[curTablePos]++;
	}

	for (int i = 0; i >= 0; i--)
	{
		for (int j = 0; j < k && readable; j++)
		{
			switch (tok[i + j])
			{
			case 'A':
				combo[j] = T;
				break;

			case 'T':
				combo[j] = A;
				break;

			case 'G':
				combo[j] = C;
				break;

			case 'C':
				combo[j] = G;
				break;
			default:
				readable = false;
				break;
			}
		}

		int curTablePos = 0;
		for (int j = 0; j < k && readable; j++)
			curTablePos += pow(4, j) * combo[j];

		if (readable) table[curTablePos]++;
	}

	delete combo;
}

#endif
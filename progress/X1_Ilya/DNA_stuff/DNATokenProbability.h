#ifndef _INC_DNATOKENPROBABILITY
#define _INC_DNATOKENPROBABILITY

#include "ComboCounter.h"
#include <math.h>

double calcTokenProb(int tableSize, char* token, double* table, const int k)
{
	double logProb = 0;
	double* xTable = new double[tableSize];
	for (int i = 0; i < tableSize; i++) xTable[i] = 1;
	
	countCombo(token, table, k);
	for (int j = 0; j < tableSize; j++)
		logProb += log(pow(table[j], xTable[j]));

	delete xTable;
	return logProb;
}

#endif

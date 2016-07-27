#ifndef _INC_COMPLIMENT
#define _INC_COMPLIMENT

#include <cassert>

void makeComp(char* triplet, char* outputTriplet)
{
	assert(triplet);
	
	for (int i = 0; i < 3; i++)
	{
		switch (triplet[i])
		{
		case 'A':
			outputTriplet[i] = 'T';
			break;

		case 'T':
			outputTriplet[i] = 'A';
			break;

		case 'G':
			outputTriplet[i] = 'C';
			break;

		case 'C':
			outputTriplet[i] = 'G';
			break;

		default:
			outputTriplet[i] = 0;
			break;
		}
	}
}

#endif
#ifndef _INC_TOKEN_DNA
#define _INC_TOKEN_DNA

#include <Windows.h>

void tokenDna(char delim[], char str[], int sz, bool eTokenType[], char* tokens[])
{
	assert(str && delim);
	char* type = 0;
	type = strtok(str, delim);

	for (int i = 0; i < sz && type; i++)
	{
		if (type[0] == 'E' && !type[1])
		{
			eTokenType[i] = true;
			tokens[i] = strtok(NULL, delim);
		}
		else if (type[0] == 'C' && !type[1])
		{
			eTokenType[i] = false;
			tokens[i] = strtok(NULL, delim);
		}
		else tokens[i] = type;

		type = strtok(NULL, delim);
	}
}

#endif
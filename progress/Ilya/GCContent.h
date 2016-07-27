#ifndef _INC_GCCONTENT
#define _INC_GCCONTENT

#include <cassert>

double gcContent(char* tok, int sz)
{
	assert(tok);
	int gcAmnt = 0;
	int i = 0;

	for (; tok[i]; i++)
		if (tok[i] == 'G' || tok[i] == 'C') gcAmnt++;

	return gcAmnt / static_cast<double>(i);
}

#endif
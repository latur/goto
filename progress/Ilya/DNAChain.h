#ifndef _INC_DNA_CHAIN
#define _INC_DNA_CHAIN

#include "DNAClasses.h"

class dnaChain
{
private:
	dnaToken* tokens_;
	unsigned int* types_;
	int amnt;

public:
	dnaChain() = delete;
	dnaChain(char* filepath, unsigned int* types, char* delim);
	~dnaChain();

	dnaToken* operator[](int i) { return tokens_ + i; }

	int Amnt() { return amnt;  }
};

dnaChain::dnaChain(char* filepath, unsigned int* types, char* delim)
{

}

#endif
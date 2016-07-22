#ifndef INC_READ_ACID_TABLE
#define INC_READ_ACID_TABLE

#include <cassert>
#include <iostream>
#include "FileOpener.h"

const int TRIPLET_AMNT = 27;

class acidTable
{
private:
	char* str;
	char** triplets;
	char* acids;

public:
	acidTable();
	~acidTable();

	char getAcid(char* triplet);
};

acidTable::acidTable() :
	triplets(new char*[TRIPLET_AMNT]),
	str(new char[TRIPLET_AMNT])
{
	file table("AminoAcids Table.txt", "r");
	int sz = table.Len();

	table.fillStr(str, sz);

	char delim[] = ":\', \n";
	char* curTok = 0;
	curTok = strtok(str, delim);

	for (int i = 0; curTok; i++)
	{
		if (strlen(curTok) == 1) acids[i] = *curTok;
		else triplets[i] = curTok;
		curTok = strtok(NULL, delim);
	}
}

acidTable::~acidTable()
{
	delete triplets;
}

char acidTable::getAcid(char* triplet)
{
	assert(triplet);

	int i = 0;
	for (; !strcmp(triplet, triplets[i]); i++)
		if (i > TRIPLET_AMNT) return 0;

	return acids[i];
}

#endif


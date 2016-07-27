#ifndef INC_READ_ACID_TABLE
#define INC_READ_ACID_TABLE

#include <cassert>
#include <iostream>
#include "FileOpener.h"

const int TRIPLET_AMNT = 64;

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
	str(0),
	acids(new char[TRIPLET_AMNT])
{
	file table("AminoAcids Table.txt", "r");
	int sz = table.Len();
	str = new char[sz];

	table.fillStr(str, sz);

	char delim[] = ":\', \n\t";
	char* curTok = strtok(str, delim);

	for (int i = 0; curTok && i < TRIPLET_AMNT; i++)
	{
		triplets[i] = curTok;

		curTok = strtok(NULL, delim);
		if (!curTok) break;
		acids[i] = *curTok;

		curTok = strtok(NULL, delim);
	}
}

acidTable::~acidTable()
{
	delete [] triplets;
	delete [] str;
	delete [] acids;
}

char acidTable::getAcid(char* triplet)
{
	assert(triplet);
	bool equal = false;

	int i = 0;
	for (; i < TRIPLET_AMNT; i++)
	{
		equal = true;
		for (int j = 0; j < 3; j++)
		{
			if (triplet[j] != triplets[i][j])
			{
				equal = false;
			}
		}

		if (equal) break;
	}

	if (i >= TRIPLET_AMNT) return 0;
	return acids[i];
}

#endif


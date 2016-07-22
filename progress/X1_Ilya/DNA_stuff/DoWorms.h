#ifndef _INC_DOWORMS
#define _INC_DOWORMS

#include <Windows.h>
#include <cstdio>
#include <cassert>
#include <math.h>
#include "FileOpener.h"
//#include "GCAmount.h"
#include "ComboCounter.h"
#include "TokenDnaFile.h"
#include "Normalize.h"
#include "DnaTokenProbability.h"

const int CHR_AMNT = 6000000;
const int SPEC_AMNT = 6000;

void doWorms()
{	
	const int k = 2;
	
	file dna("train.fa.txt", "r");
	char* str = new char[CHR_AMNT];
	int sz = dna.Len();

	char** tokens = new char*[CHR_AMNT];
	bool* eTokenType = new bool[CHR_AMNT];
	char* type = 0;

	dna.fillStr(str, CHR_AMNT);
	char delim[] = "qwertyuioplkjhgfdsazxcvbnm,./;'[]_1234567890\n>";

	const int tableSize = pow(4, k);
	double* eTable = new double[tableSize];
	double* cTable = new double[tableSize];

	for (int i = 0; i < tableSize; i++)
	{
		eTable[i] = 1;
		cTable[i] = 1;
	}

	tokenDna(delim, str, sz, eTokenType, tokens);
	for (int i = 0; i < SPEC_AMNT; i++)
	{
		if (eTokenType[i]) countCombo(tokens[i], eTable, k);
		else countCombo(tokens[i], cTable, k);
	}

	normalizeDnaProbTable(eTable, k);
	normalizeDnaProbTable(cTable, k);
	file eDic("eDic.txt", "w");
	file cDic("cDic.txt", "w");

	for (int i = 0; i < tableSize; i++)
	{
		fprintf(eDic.Res(), "%lg ", eTable[i]);
		fprintf(cDic.Res(), "%lg ", cTable[i]);
	}

	file x("test.fa.txt", "r");
	x.fillStr(str, sz);

	file output("output.txt", "w");

	tokenDna(delim, str, sz, eTokenType, tokens);

	double* xTable = new double[tableSize];
	double logEProb = 0;
	double logCProb = 0;

	for (int i = 0; i < tableSize; i++) xTable[i] = 0;
	for (int i = 0; i < SPEC_AMNT; i++)
	{
		logEProb = calcTokenProb(tableSize, tokens[i], eTable, k);
		logCProb = calcTokenProb(tableSize, tokens[i], cTable, k);

		if (logEProb > logCProb)
			 fprintf(output.Res(), "E ");
		else fprintf(output.Res(), "C ");

		logEProb = 0;
		logCProb = 0;
	}

	delete str;
	delete eTable;
	delete cTable;
	delete tokens;
}

#endif
#ifndef _INC_DO_CHINCHILLAS
#define _INC_DO_CHINCHILLAS

#include "FileOpener.h"
#include "ReadAcidTable.h"
#include "TokenDnaFile.h"
#include "Compliment.h"
#include <Windows.h>

const int CHR_AMNT = 16000000;
const int SPEC_AMNT = 1000;
const int SPEC_SIZE = 15486;

void doChinchillas()
{
	file input("reads.fa", "r");
	file hint("EndDNAChain.txt", "r");
	int hintSz = hint.Len();
	char* hintStr = new char[hintSz];
	char* str = new char[CHR_AMNT];
	char** tokens = new char*[SPEC_AMNT];
	bool exUnfit[SPEC_SIZE][3][2] = {};

	input.fillStr(str, CHR_AMNT);
	hint.fillStr(hintStr, hintSz);
	
	char delim[] = "qwertyuiopasdfghjklzxcvbnm,./;\'[]1234567890QWERYUIOP{}|SDFHJKL:ZXVBM<>\n\t ";
	tokenDna(delim, str, SPEC_AMNT, NULL, tokens);
	
	acidTable data;
	char acid = 0;
	int matched = 0;
	int found = 0;
	int starts[15] = {};
	int ends[15] = {};

	char reverse[4] = "";
	_strrev(*tokens);
	char acidStr[3][SPEC_SIZE / 3] = {};

	for (int j = 0; j < 3; j++)
	{
		for (int i = j; i + 3 < SPEC_SIZE; i += 3)
		{
			makeComp(*tokens + i, reverse);
			acidStr[j][i / 3] = data.getAcid(reverse);
		}
	}

	for (int j = 0; j < 3; j++)
	{
		/*for (; col + 3 < SPEC_SIZE; col += 3)
		{
			acid = data.getAcid(tokens[0] + col);

			for (int row = 1; row < SPEC_AMNT; row++)
			{
				qAcid = data.getAcid(tokens[row] + col);
				if (acid != qAcid || !acid)
				{
					exUnfit[col][j][0] = true;
					break;
				}

				else exUnfit[col][j][0] = false;
			}
		}*/

		const int minExAmnt = 7;
		for (int col = 0; col < SPEC_SIZE/3; col++)
		{			
			for (; acidStr[j][col] == hintStr[matched] && col < SPEC_SIZE / 3 && matched < hintSz; matched++) col++;

			if (matched >= minExAmnt)
			{

				starts[found] = col - matched;
				ends[found] = col;
				found++;
				matched = 0;
			}
			/*for (int row = 1; row < SPEC_AMNT; row++)
			{
				qAcid = data.getAcid(tokens[row] + col);
				if (acid != qAcid || !acid)
				{
					exUnfit[col][j][1] = true;
					break;
				}

				else exUnfit[col][j][1] = false;
			}*/
		}
	}

	for (int i = 0; i < found; i++)
	{
		printf("%d - %d|", starts[found], ends[found]);
	}

	delete [] str;
	delete [] tokens;

	printf("Done");
	while (!GetAsyncKeyState(VK_ESCAPE));
}

#endif
#ifndef _INC_DNA_TOKEN
#define _INC_DNA_TOKEN

#include <cstring>
#include <cassert>
#include "ReadAcidTable.h"
#include "Compliment.h"

enum shift { SHIFT0, SHIFT1, SHIFT2 };
enum orient { STRAIGHT, REVERSED };

const int TOKEN_SIZE = 1000;

class dnaToken
{
private:
	char* str_;

public:
	dnaToken() = delete;
	dnaToken(char* str);
	~dnaToken();
	
	operator char*() { return str_; }
	char operator[](int i) { return str_[i]; }
	dnaToken& operator=(char* str);
	bool*** operator==(dnaToken that);
	bool*** operator==(dnaChain that);
};

dnaToken::dnaToken(char* str) :
	str_(new char[TOKEN_SIZE])
{
	assert(str && strlen(str) == TOKEN_SIZE);
	strcpy(str_, str);
}

dnaToken::~dnaToken()
{
	delete [] str_;
}

dnaToken& dnaToken::operator=(char* str)
{
	assert(str && strlen(str) == TOKEN_SIZE);
	strcpy(str_, str);
}

bool*** dnaToken::operator==(dnaToken that)
{
	bool*** compData = new bool**[TOKEN_SIZE];

	for (int i = 0; i < TOKEN_SIZE; i++)
	{
		compData[i] = new bool*[REVERSED + 1];
		compData[i][0] = new bool[SHIFT2 + 1];
		compData[i][1] = new bool[SHIFT2 + 1];
	}

	acidTable data;
	char acid[2] = {};
	char reverse[2][3] = {};

	for (int j = 0; j < 3; j++)
	{
		int col = j;
		for (int i = 1; i > -2; i -= 2)
		{
			for (; col + 3 < TOKEN_SIZE; col += 3 * i)
			{
				makeComp(str_	   + col, reverse[0]);
				makeComp(that.str_ + col, reverse[1]);
				
				acid[0] = data.getAcid(reverse[0]); 
				acid[1] = data.getAcid(reverse[1]);

				if (acid[0] != acid[1] || !acid[0])
				{
					compData[col][(-i + 1)/2][j] = false;
					break;
				}
				else compData[col][(-i + 1) / 2][j] = true;
			}
		}
	}

	return compData;
}

bool*** dnaToken::operator==(dnaChain that)
{
	bool*** compData = new bool**[TOKEN_SIZE];

	for (int i = 0; i < TOKEN_SIZE; i++)
	{
		compData[i] = new bool*[REVERSED + 1];
		compData[i][0] = new bool[SHIFT2 + 1];
		compData[i][1] = new bool[SHIFT2 + 1];
	}

	char** reverse = new char*[that.Amnt()];
	acidTable data;
	char acid[2] = {};

	for (int i = 0; i < that.Amnt(); i++) reverse[i] = new char[3];
	
	for (int j = 0; j < 3; j++)
	{
		int col = j;
		for (int i = 1; i > -2; i -= 2)
		{
			for (; col + 3 < TOKEN_SIZE; col += 3 * i)
			{
				if (i == -1)
				{
					makeComp(str_ + col, reverse[0]);
					acid[0] = data.getAcid(reverse[0]);
				}
	
				for (int row = 1; row < that.Amnt(); row++)
				{
					makeComp(*that[row] + col, reverse[1]);
					acid[1] = data.getAcid(reverse[1]);
					if (acid[0] != acid[1] || !acid[0])
					{
						compData[col][(-i + 1) / 2][j] = false;
						break;
					}
					else compData[col][(-i + 1) / 2][j] = true;
				}
			}
		}
	}

	return compData;
}

#endif
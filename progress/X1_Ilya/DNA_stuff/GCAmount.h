#ifndef _INC_GCAMOUNT
#define _INC_GCAMOUNT

void gcAmnt(double* eGC, double* cGC, char* str, int sz)
{
	assert(str);
	
	int filledESpec = 0;
	int filledCSpec = 0;

	for (int i = 0; str[i]; i++)
	{
		if (str[i] == '>')
		{
			i++;
			int start = i;
			int gcAmnt = 0;
			int specSz = 0;

			switch (str[i])
			{
			case 'E':
				for (; str[i] != '>' && str[i] != EOF; i++)
				{
					if (str[i] == 'G' || str[i] == 'C') gcAmnt++;
				}

				specSz = i - start;
				eGC[filledESpec] = gcAmnt / static_cast<double>(specSz);
				filledESpec++;
				break;
			case 'C':
				for (; str[i] != '>' && str[i] != EOF; i++)
				{
					if (str[i] == 'G' || str[i] == 'C') gcAmnt++;
				}

				specSz = i - start;
				cGC[filledESpec] = gcAmnt / static_cast<double>(specSz);
				filledCSpec++;
				break;
			}
			i--;
		}
	}
}

#endif
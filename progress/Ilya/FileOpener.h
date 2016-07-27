#ifndef _INC_FILE_OPENER
#define _INC_FILE_OPENER

#include <cstdio>

class file
{
private:
	FILE* res_;
	int len_;

public:
	file(char* address, char* mode);
	~file();

	FILE* Res() { return res_; }
	int Len() { return len_; }
	char Getc() { return getc(res_); }
	void putc(char chr) { fputc(chr, res_); }
	void fillStr(char* str, int len);
};

file::file(char* address, char* mode)
{
	res_ = fopen(address, mode);
	fseek(res_, 0L, SEEK_END);
	len_ = ftell(res_);
	rewind(res_);
}

file::~file()
{
	fclose(res_);
}

void file::fillStr(char* str, int len)
{
	char curchr = Getc();
	for (int i = 0; curchr != EOF && i < len; i++)
	{
		str[i] = curchr;
		curchr = Getc();
	}
}

#endif
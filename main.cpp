#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	FILE *fin, *fout;
	fin=fopen("simple.in","rb");
	fout=fopen("simple.out","wb");
	
	int a,b,s;
	fscanf(fin,"%d %d",&a,&b);
	s=a*b;
	fprintf(fout,"%d\n",stdout);
	
	fclose(stdin);
	fclose(stdout);
	return 0; 
}

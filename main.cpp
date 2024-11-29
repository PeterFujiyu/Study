#include <iostream>
#include <cstdio>
using namespace std;

//int main() {
//	FILE *fin, *fout;
//	fin=fopen("simple.in","rb");
//	fout=fopen("simple.out","wb");
//	
//	int a,b,s;
//	fscanf(fin,"%d %d",&a,&b);
//	s=a*b;
//	fprintf(fout,"%d\n",stdout);
//	
//	fclose(stdin);
//	fclose(stdout);
//	return 0; 
//}

int factorial(int n) {
	if (n==1) return 1;
	return n*factorial(n-1);
}

int main() {
	int i=0;
	cin >> i;
	cout << factorial(i) << endl;
}

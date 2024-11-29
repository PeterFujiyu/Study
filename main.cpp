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

#include <iostream>
using namespace std;

void hanoi(int n, char source, char target, char auxiliary) {
    if (n == 1) {
        cout << source << " to " << target << "; ";
        return;
    }
    hanoi(n - 1, source, auxiliary, target);
    cout << source << " to " << target << "; ";
    hanoi(n - 1, auxiliary, target, source);
}

int main() {
    int n;
    cout << "请输入汉诺塔的盘子数量: ";
    cin >> n;
    hanoi(n, 'A', 'C', 'B');
    cout << endl;
    return 0;
}

//int main() {
//	int i=0;
//	cin >> i;
//	cout << factorial(i) << endl;
//}

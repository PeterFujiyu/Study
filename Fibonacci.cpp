#include <iostream>
using namespace std;

int pell(int N) {
	if (N == 1) {
		return 1;
	} else if (N == 2) {
		return 2;
	} else {
		int f1 = 1, f2 = 2, f3;
		for (int i = 0; i < (N - 2); i++) {
			f3 = (2 * f2 + f1) % 32767;
			f1 = f2;
			f2 = f3;
		}
		return f2;
	}
}
int Fibonacci(int num) {
	if (num==1 || num==2) {
		return 1;
	} else {
		return Fibonacci(num-2)+Fibonacci(num-1); 
	}
}

int main() {
	int a;
	int num[10001] = {};
	cin >> a; 
	for (int i=0;i<a;i++) {
		cin >> num[i]; 
	}
	for (int i=0;i<a;i++) {
		cout << pell(num[i]) << endl;
	}
}

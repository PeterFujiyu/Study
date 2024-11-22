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

//int main() {
//	int a;
//	int num[10001] = {};
//	cin >> a; 
//	for (int i=0;i<a;i++) {
//		cin >> num[i]; 
//	}
//	for (int i=0;i<a;i++) {
//		cout << pell(num[i]) << endl;
//	}
//}

int main() {
    int x, y, z;

    cout << "���� x���ɳ濪ʼ���ѵ���������y��ÿ�Գɳ�ÿ�β�����������z��Ŀ��������: ";
    cin >> x >> y >> z;

    int adults = 1;
    int eggsLastMonth = 0, eggsTwoMonthsAgo = 0;

    for (int month = 1; month <= z; ++month) {
        int newAdults = eggsTwoMonthsAgo;
        eggsTwoMonthsAgo = eggsLastMonth;
        if (month >= x) {
            eggsLastMonth = adults * y;
        } else {
            eggsLastMonth = 0; 
        }
        adults += newAdults;
    }
    cout << "�� " << z << " ���º�ɳ��������: " << adults << endl;
    return 0;
}


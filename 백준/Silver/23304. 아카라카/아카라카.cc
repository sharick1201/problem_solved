#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string input;
bool flag = true;

void isPalin(string s) {
	if (s.size() == 1 || !flag) return;

	string rev = s;
	reverse(rev.begin(), rev.end());

	if (s != rev) {
		flag = false;
		return;
	}
	else {
		string sub = s.substr(0, s.size() / 2);
		isPalin(sub);

		if (s.size() % 2 == 1) {
			sub = s.substr(s.size() / 2 + 1);
			isPalin(sub);
		}
		else {
			sub = s.substr(s.size() / 2);
			isPalin(sub);
		}
	}

}


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> input;

	isPalin(input);

	if (flag) {
		cout << "AKARAKA";
	}
	else {
		cout << "IPSELENTI";
	}

	return 0;
}
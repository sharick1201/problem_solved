#include <iostream>
#include <string>
using namespace std;
string input;

bool isPikachuWord(const string& s) {
	int i = 0;
	while (i < s.length()) {
		if (s.substr(i, 2) == "pi") {
			i += 2;
		}
		else if (s.substr(i, 2) == "ka") {
			i += 2;
		}
		else if (s.substr(i, 3) == "chu") {
			i += 3;
		}
		else {
			return false;
		}
	}
	return true;
}
int main() { 
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);

	cin >> input;

	if (isPikachuWord(input)) {
		cout << "YES";
	}
	else {
		cout << "NO";
	}

	return 0;
}

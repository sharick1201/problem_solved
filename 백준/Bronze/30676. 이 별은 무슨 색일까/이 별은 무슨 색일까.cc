#include <iostream>
using namespace std;
int input;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);

	cin >> input;
	if (620 <= input && 780 >= input) {
		cout << "Red";
	}
	else if (590 <= input && 620 > input) {
		cout << "Orange";
	}
	else if (570 <= input && 590 > input) {
		cout << "Yellow";
	}
	else if (495 <= input && 570 > input) {
		cout << "Green";
	}
	else if (450 <= input && 495 > input) {
		cout << "Blue";
	}
	else if (425 <= input && 450 > input) {
		cout << "Indigo";
	}
	else if (380 <= input && 425 > input) {
		cout << "Violet";
	}
	return 0;
}
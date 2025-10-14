#include <iostream>
using namespace std;
int N;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	
	cin >> N;
	for (int i = 0; i < N; ++i) {
		int a, b;
		cin >> a >> b;
		cout << a + b << "\n";
	}
	return 0;
}
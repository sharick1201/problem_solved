#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int chair[1025][1025];

int findmychair(int x, int y, int size) {
	if (size == 1) {
		return chair[x][y];
	}

	vector<int> prizenum;

	int newSize = size / 2;
	prizenum.push_back(findmychair(x, y, newSize)); // 왼쪽 위
	prizenum.push_back(findmychair(x, y + newSize, newSize)); // 오른쪽 위
	prizenum.push_back(findmychair(x + newSize, y, newSize)); // 왼쪽 아래
	prizenum.push_back(findmychair( x + newSize, y + newSize, newSize)); // 오른쪽 아래 

	sort(prizenum.begin(), prizenum.end());

	return prizenum[1];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	
	cin >> N;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> chair[i][j];
		}
	}
	cout << findmychair(0, 0, N);
	return 0;
}
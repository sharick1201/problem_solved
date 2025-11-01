#include <iostream>
#include <algorithm>
using namespace std; 

int N;
int A[100'001];

int M;

int binarySearch(int target) {
	int st = 0;
	int en = N-1;
	int mid;

	while (st <= en) {
		mid = ( st + en ) / 2;
		if (target > A[mid]) {
			st = mid + 1;
		} else if (target < A[mid]) {
			en = mid - 1;
		} else {
			return 1;
		}
	}

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);

	cin >> N;

	for (int i = 0; i < N; ++i) {
		cin >> A[i];
	}
    
    sort(A, A+N);
	
	cin >> M;

	for (int i = 0; i < M; ++i) {
		int target;
		cin >> target;
		cout << binarySearch(target) << "\n";
	}

	return 0;
}
#include <iostream>
#include <algorithm>
using namespace std; 

int N;
int A[100'001];
int M;

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
		cout << binary_search(A, A+N, target) << "\n";
	}

	return 0;
}
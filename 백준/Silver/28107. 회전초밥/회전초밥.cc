#include <iostream>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

int N, M;
queue<int> ord[200'001];
int cstm_cnt[100'001] = { 0, };


int main() { 
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);

	cin >> N >> M;

	for (int i = 0; i < N; ++i) {
		int ttl;
		cin >> ttl;
		for (int j = 0; j < ttl; ++j) {
			int input;
			cin >> input;
			ord[input].push(i);
		}
	}

	for (int i = 0; i < M; ++i) {
		int sushi;
		cin >> sushi;
		if (!ord[sushi].empty()) {
			int now = ord[sushi].front();
			ord[sushi].pop();
			cstm_cnt[now]++;
		}
	}

	for (int i = 0; i < N; ++i) {
		cout << cstm_cnt[i] << " ";
	}


	return 0;
}
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

int tc; // 테스트케이스 갯수 

//* 각 테케마다 필요한 변수들 *//

int V, E; // 정점 수, 간선 수

// 그래프(인접 리스트)
vector<int> adj[501];      // adj[i]: i에서 갈 수 있는 노드들
vector<int> rev_adj[501];  // rev_adj[i]: i로 올 수 있는 노드들

// 각 노드 방문했는지 확인. 노드가 1번부터 있음.
int visited[501];

// 자신이 키가 몇 번째인지 알 수 있는 학생
int ans = 0;
////////////////////////////////



///* 초기화하는 함수 */
//void init() {
//	for (int i = 0; i <= 500; i++) {
//		adj[i].clear();
//		rev_adj[i].clear();
//	}
//	// visited 초기화는 매 노드마다 해줄 것.
//	ans = 0;
//}




/* 특정 기준값에 맞도록 DFS */
void dfs(int now, int flag) {

	if (flag == 1) {
		for (int i = 0; i < rev_adj[now].size(); i++) {
			int next = rev_adj[now][i];
			// cout << now << "에서 " << next << "방문 ";
			if (visited[next] == 1) continue;
			visited[next] = 1;
			dfs(next, 1);
		}
	}
	else if (flag == 2) {
		for (int i = 0; i < adj[now].size(); i++) {
			int next = adj[now][i];
			// cout << now << "에서 " << next << "방문 ";
			if (visited[next] == 1) continue;
			visited[next] = 1;
			dfs(next, 2);
		}
	}
}


/* 기준점(start)과 연결된 노드들을 확인하고, 기준점이 to인 경우와 기준점이 from인 경우 나눈다. */
void startDfs(int start) {

	// 기준점이 to인 경우 (flag 1)
	for (int i = 0; i < rev_adj[start].size(); i++) {
		int next = rev_adj[start][i];
		if (visited[next] == 1) continue;
		visited[next] = 1;
		dfs(next, 1);
	}

	// 기준점이 from인 경우 (flag 2)
	for (int i = 0; i < adj[start].size(); i++) {
		int next = adj[start][i];
		if (visited[next] == 1) continue;
		visited[next] = 1;
		dfs(next, 2);
	}
}





// 전부 다 방문했는지 확인(모두 방문했으면 내 키 순서를 아는 것)
bool isVisitedAll() {
	for (int i = 1; i <= V; i++) {
		if (visited[i] == 0) {
			// cout << i << "번째 방문 안 함" << "\n";
			return false;
		}
	}
	return true;
}





int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// cin >> tc;
	// for (int t = 1; t <= tc; t++) {
		// 이전 테케 초기화 및 현재 테케에 대한 값 입력받기
		cin >> V >> E;

		// init();

		for (int i = 0; i < E; i++) {
			int from, to;
			cin >> from >> to;
			adj[from].push_back(to);      // from에서 to로 가는 간선
			rev_adj[to].push_back(from);  // to로 from에서 오는 간선
		}

		// 과정
		// 각 노드에 대해, 자신의 키 아는지 확인
		for (int i = 1; i <= V; i++) {
			// visited 초기화 (memset 대신 반복문 사용)
			for (int j = 0; j <= 500; j++) {
				visited[j] = 0;
			}

			visited[i] = 1;
			startDfs(i);

			if (isVisitedAll()) {
				ans++;
				// cout << "내키를안다:" << i << "\n";
			}
		}

		// 출력
		// cout << "#" << t << " "
		cout << ans << "\n";
	// }

	return 0;
}

#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

int V, E, K;

struct Edge {
	int toNode;
	int cost;
	
	bool operator<(Edge right) const {
		if (cost < right.cost) return false;
		if (cost > right.cost) return true;
		return false;
	}
};

// 그래프 정보 담을 인접리스트
vector<Edge> alis[300001];
// 경로 저장
int dest[300001];

void dijkstra(int start) {
	// 준비
	priority_queue<Edge>pq;
	for (int i = 1; i <= V; i++) {
		dest[i] = 21e8;
	}

	// 시작점 처리
	pq.push({ start, 0 });
	dest[start] = 0;

	while (!pq.empty()) {
		Edge now = pq.top(); pq.pop();
		if (dest[now.toNode] < now.cost) continue;

		for (int i = 0; i < alis[now.toNode].size(); i++) {
			// 다음 후보지를 찾는다.
			Edge next = alis[now.toNode][i];
			int newcost = dest[now.toNode] + next.cost;

			if (dest[next.toNode] <= newcost) continue;

			dest[next.toNode] = newcost;
			pq.push({next.toNode, newcost});

		}
	}
    for (int i = 1; i <= V; i++) {
		if (dest[i] == 21e8) {
			cout << "INF" << "\n";
		}
		else {
			cout << dest[i] << "\n";
		}
	}
}




int main() {
	
	cin >> V >> E >> K;

	for (int i = 0; i < E; i++) {
		int from, to, cost;
		cin >> from >> to >> cost;
		alis[from].push_back({ to, cost });
		// alis[to].push_back({ from, cost });
	}

	dijkstra(K);
	return 0;
}
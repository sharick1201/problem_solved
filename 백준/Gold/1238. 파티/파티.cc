#include <iostream> //
#include <string>
#include <vector> //
#include <queue> //
#include <set>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

// 가중치가 음수인 간선은 없다.
// 다익스트라를 두 번 돌리자.

// 간선 구조체 (비용을 담기 위해 구조체로 정의)
struct Edge {
	int to; // 도착노드
	int cost;

	// 우선순위 큐 사용할 것이므로 연산자 반대로 
	bool operator<(Edge right)const {
		if (cost < right.cost) return false;
		if (cost > right.cost) return true;
		return false;
	}
};

int V, E, X;
vector<Edge> alis[1001]; // 노드번호 1번부터 시작임
vector<Edge> alis_rev[1001]; // 노드번호 1번부터 시작임
int visited[1001]; // 갈 때, 인덱스번호의 노드 방문했는지 체크 + cost 저장  +++ 나중에 visited_sec랑 합쳐서 최종 왔다갔다비용 저장
int visited_sec[1001]; // 올 때, 인덱스번호의 노드 방문했는지 체크 + cost 저장
int ans = -1;

void dijkstra_rev(int start) {
	// 준비
	for (int i = 1; i <= V; i++) {
		visited[i] = 21e8;
	}
	priority_queue<Edge> pq1;

	// 시작점
	pq1.push({ start, 0 });
	visited[start] = 0;

	while (!pq1.empty()) {
		Edge now = pq1.top(); pq1.pop();
		if (now.cost > visited[now.to]) continue; // 꺼냈는데 이미 visited에 최단경로 저장되어 있다면 버려야됨

		for (int i = 0; i < alis_rev[now.to].size(); i++) {
			Edge next = alis_rev[now.to][i];
			int nextcost = now.cost + next.cost;

			if (nextcost >= visited[next.to]) continue; // 더 큰데 큐에 굳이 넣을 필요 없다.
			visited[next.to] = nextcost;
			pq1.push({ next.to, nextcost });
		}
	}
}

void dijkstra(int start) {
	// 준비
	for (int i = 1; i <= V; i++) {
		visited_sec[i] = 21e8;
	}
	priority_queue<Edge> pq2;

	// 시작점
	pq2.push({ start, 0 });
	visited_sec[start] = 0;

	while (!pq2.empty()) {
		Edge now = pq2.top(); pq2.pop();
		if (now.cost > visited_sec[now.to]) continue; // 꺼냈는데 이미 visited에 최단경로 저장되어 있다면 버려야됨

		for (int i = 0; i < alis[now.to].size(); i++) {
			Edge next = alis[now.to][i];
			int nextcost = now.cost + next.cost;

			if (nextcost >= visited_sec[next.to]) continue; // 더 큰데 큐에 굳이 넣을 필요 없다.
			visited_sec[next.to] = nextcost;
			pq2.push({ next.to, nextcost });
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> V >> E >> X;

	// 입력받을 때, 역방향 인접리스트도 하나 만든다.
	for (int i = 0; i < E; i++) {
		int from, to, cost; 
		cin >> from >> to >> cost;
		alis[from].push_back({ to, cost });
		alis_rev[to].push_back({ from, cost });
	}

	// 파티 가는 길~ 야호
	// 역방향 인접리스트에 대하여 X -> 모든 i까지 다익스트라하고, visited 배열에 저장
	dijkstra_rev(X);
	
	// 파티에서 오는 길~
	// 원본 방향 인접리스트에 대하여, X -> 모든 i까지 다익스트라하고, visited_sec 배열에 저장
	  // 이때 더하면서 "가장 오래 걸리는 학생의 소요시간" 도 함께 체크
	dijkstra(X);

	// visited[i] + visited_sec[i] 더해서 결과 생성
	for (int i = 1; i <= V; i++) {
		visited[i] += visited_sec[i];
		if (ans < visited[i]) {
			ans = visited[i];
		}
	}

	// 출력
	cout << ans;

	return 0;
}

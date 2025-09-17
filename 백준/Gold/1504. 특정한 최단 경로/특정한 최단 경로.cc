#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

int N, E, v1, v2;

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
    priority_queue<Edge> pq;
    for (int i = 1; i <= N; i++) {
        dest[i] = 21e8;
    }

    // 시작점 처리
    pq.push({start, 0});
    dest[start] = 0;

    while (!pq.empty()) {
        Edge now = pq.top(); 
        pq.pop();
        if (dest[now.toNode] < now.cost) continue;

        for (int i = 0; i < alis[now.toNode].size(); i++) {
            // 다음 후보지 찾는다
            Edge next = alis[now.toNode][i];
            int newcost = dest[now.toNode] + next.cost;

            if (dest[next.toNode] <= newcost) continue;

            dest[next.toNode] = newcost;
            pq.push({next.toNode, newcost});
        }
    }
}

int main() {
    cin >> N >> E;

    for (int i = 0; i < E; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        alis[from].push_back({to, cost});
        alis[to].push_back({from, cost});
    }

    cin >> v1 >> v2;

    // 1번에서 시작
    dijkstra(1);
    long long dist1tov1 = dest[v1];
    long long dist1tov2 = dest[v2];

    // v1에서 시작
    dijkstra(v1);
    long long distv1tov2 = dest[v2];
    long long distv1toN = dest[N];

    // v2에서 시작
    dijkstra(v2);
    long long distv2tov1 = dest[v1];
    long long distv2toN = dest[N];

    // 두 가지 경로 계산해서 더 적은 거
    long long path1 = dist1tov1 + distv1tov2 + distv2toN;  // 1->v1->v2->N
    long long path2 = dist1tov2 + distv2tov1 + distv1toN;  // 1->v2->v1->N

    long long result = min(path1, path2);

    if (result >= 21e8) {
        cout << -1;
    } else {
        cout << result;
    }

    return 0;
}

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;


struct Edge {
    int to;
    int cost;
    bool operator>(const Edge &right) const {
        return cost > right.cost;
    }
};

vector<Edge> alis[10001];
int dist[10001]; // 각 노드까지의 감염 시간

void dijkstra(int start) {
    priority_queue<Edge, vector<Edge>, greater<Edge>> pq; // min heap으로 해야됨

    for (int i = 1; i <= 10000; i++) {
        dist[i] = 21e8;
    }

    // 시작점 처리
    pq.push({start, 0});
    dist[start] = 0;

    while (!pq.empty()) {
        Edge now = pq.top();
        pq.pop();
        if (dist[now.to] < now.cost)
            continue;

        for (Edge &next : alis[now.to]) {
            int newcost = dist[now.to] + next.cost;

            if (dist[next.to] > newcost) {
                dist[next.to] = newcost;
                pq.push({next.to, newcost});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    
    int t; // 테스트 케이스 수
    cin >> t;

    for (int tc = 0; tc < t; tc++) {
        int n, d, c;
        cin >> n >> d >> c;

        // 그래프 초기화
        for (int i = 1; i <= n; i++) {
            alis[i].clear();
        }

        for (int i = 0; i < d; i++) {
            int a, b, s;
            cin >> a >> b >> s;
            alis[b].push_back({a, s});
        }

        dijkstra(c);

        int cnt = 0;
        int maxcost = 0;

        for (int i = 1; i <= n; i++) {
            if (dist[i] != 21e8) {
                cnt++;
                maxcost = max(maxcost, dist[i]);
            }
        }

        cout << cnt << " " << maxcost << "\n";
    }

    return 0;
}

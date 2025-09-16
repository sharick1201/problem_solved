#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int VN; // 도시 개수
int EN; // 버스 개수
int startV, endV;

struct Edge {
    int vert;
    int cost;

    bool operator<(Edge next)const {
        if (cost > next.cost) return true;
        return false;
    }
};

vector<Edge> alis[1001]; // 인접 리스트
int before[1001]; // 직전 노드를 저장
int visited[1001] = {0, }; // 최소 비용 저장(인덱스: 도시번호, 값: 최소비용)

vector<int> ansroad; // 경로 저장(인덱스: 현재 노드, 값: 인덱스번 노드의 직전 경로)

void dijkstra(int start) {
    for (int i = 0; i <= VN; i++) {
        visited[i] = 21e8;
    }

    priority_queue<Edge> pq;
    before[start] = -1;
    visited[start] = 0;
    pq.push({start, 0});

    while (!pq.empty()) {
        Edge now = pq.top(); pq.pop();
        if (visited[now.vert] < now.cost) continue;

        for (int i = 0; i < alis[now.vert].size(); i++) {
            Edge next = alis[now.vert][i];

            int nextcost = visited[now.vert] + next.cost;
            if (nextcost >= visited[next.vert]) continue;
            visited[next.vert] = nextcost;
            before[next.vert] = now.vert;

            pq.push({next.vert, nextcost});
        }
    }
}



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> VN >> EN;

    for (int i = 0; i < EN; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        alis[from].push_back({to, cost});
    }

    cin >> startV >> endV;

    dijkstra(startV);

    cout << visited[endV] << "\n";   // 최소 비용

    int ansN = 0;
    int idx = endV;

    while(idx != -1) {
        ansroad.push_back(idx);
        idx = before[idx];
        ansN++;
    }

    cout << ansN << "\n";

    for (int i = ansroad.size()-1; i >= 0; i--) {
        cout << ansroad[i] << " ";
    }
    return 0;
}

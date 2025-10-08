#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int INF = 21e8;
int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};

struct Node {
    int y, x, fuel;
    bool operator<(Node other) const {
        if (fuel < other.fuel) return false;
        if (fuel > other.fuel) return true;
        return false;
    }
};

int H, W;
vector<string> map;
vector<vector<int>> dist;
pair<int, int> start, treasure;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    
    cin >> H >> W;

    for (int i = 0; i < H; i++) {
        string input;
        cin >> input;
        map.push_back(input);
        for (int j = 0; j < W; j++) {
            if (map[i][j] == 'K') start = {i, j}; // 배 위치
            if (map[i][j] == '*') treasure = {i, j}; // 보물 위치
        }
    }

    priority_queue<Node> pq;
    dist.assign(H, vector<int>(W, INF));
    
    dist[start.first][start.second] = 0;
    pq.push({start.first, start.second, 0});

    while (!pq.empty()) {
        Node cur = pq.top(); pq.pop();
        
        if (dist[cur.y][cur.x] < cur.fuel) continue;

        // 보물에 도달한 경우
        if (cur.y == treasure.first && cur.x == treasure.second) {
            cout << cur.fuel;
            return 0;
        }
            // 다음 탐색
        for (int i = 0; i < 8; i++) {
            int ny = cur.y + dy[i];
            int nx = cur.x + dx[i];

            // 범위체크
            if (ny < 0 || ny >= H || nx < 0 || nx >= W) continue;

            int newfuel = cur.fuel;

            // 물살을 타고 이동할 경우
            if (i >= 5) { // 오른쪽으로 이동하는 경우
                // 연료 소모 X
            } else {
                newfuel += 1; // 그 외의 경우 연료 소모
            }

            // 이동할 수 있는 경우
            if (map[ny][nx] != '#') {
                if (newfuel < dist[ny][nx]) {
                    dist[ny][nx] = newfuel;
                    pq.push({ny, nx, newfuel});
                }
            }
        }
    }

    // 도달 불가하면...
    cout << -1;
    return 0;
}
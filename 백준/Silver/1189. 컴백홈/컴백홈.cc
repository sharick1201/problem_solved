#include <iostream>
#include <string>
using namespace std;

int R, C, K;
bool MAP[5][5]; // 갈 수 있으면 true
bool visited[5][5]; // 방문했으면 true
pair<int, int> startpoint, endpoint; // y, x

int ans = 0;

int ydir[4] = { -1, 1, 0, 0 };
int xdir[4] = { 0, 0, -1, 1 };

void bfs(int dist, pair<int, int> now) {
    if (now.first == endpoint.first && now.second == endpoint.second) {
        if (dist == K) {
            ans++;
        }
        return;
    }

    if (dist >= K) return;

    for (int i = 0; i < 4; ++i) {
        int nexty = now.first + ydir[i];
        int nextx = now.second + xdir[i];

        if (nexty < 0 || nexty >= R || nextx < 0 || nextx >= C) continue;
        if (!MAP[nexty][nextx]) continue;
        if (visited[nexty][nextx]) continue;

        visited[nexty][nextx] = true;
        bfs(dist+1, { nexty, nextx });
        visited[nexty][nextx] = false;
    }

}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> R >> C >> K;

    startpoint = { R - 1, 0 };
    endpoint = { 0 , C - 1 };

    for (int i = 0; i < R; ++i) {
        string input;
        cin >> input;
        for (int j = 0; j < C; j++) {
            if (input[j] == '.') {
                MAP[i][j] = true;
            }
            else {
                MAP[i][j] = false;
            }
        }
    }

    visited[startpoint.first][startpoint.second] = true;
    bfs(1, startpoint);

    cout << ans;

    return 0;
}

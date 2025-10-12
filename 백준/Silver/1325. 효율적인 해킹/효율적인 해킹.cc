#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<int> alis[10001];
int maxcnt = 0;
vector<int> result;

int dfs(int start, vector<bool> &visited) {
    visited[start] = true;
    int count = 1;

    for (int i = 0; i < alis[start].size(); i++) {
        int next = alis[start][i];
        if (!visited[next]) count += dfs(next, visited);
    }
    return count;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        int to, from;
        cin >> to >> from;
        alis[from].push_back(to);
    }

    // 각 컴퓨터에 대해 계산
    for (int i = 1; i <= N; i++) {
        vector<bool> visited(N + 1, false);
        int nowcnt = dfs(i, visited);

        if (nowcnt > maxcnt) {
            maxcnt = nowcnt;
            result.clear(); // 최대값이 갱신됐으니 기존 값들은 버리셈
            result.push_back(i);
        }
        else if (nowcnt == maxcnt) {
            result.push_back(i);
        }
    }

    sort(result.begin(), result.end());
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }

    return 0;
}

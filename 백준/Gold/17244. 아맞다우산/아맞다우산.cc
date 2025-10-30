#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int N, M;
char house[51][51];
int dist[6][7] =
	{
		{-1, -1, -1, -1, -1, -1, -1}, // 이거는 안 씀
		{-1, -1, -1, -1, -1, -1, -1},
		{-1, -1, -1, -1, -1, -1, -1},
		{-1, -1, -1, -1, -1, -1, -1},
		{-1, -1, -1, -1, -1, -1, -1},
		{-1, -1, -1, -1, -1, -1, -1}
	};
// 각 물건을 1~5번 이라고 하자
// 시작점 - 물건 i 거리 : [i][0]
// 물건 i - 다른 물건 거리: [i][다른 물건 인덱스]
	// = [다른물건인덱스][i] 랑 같다
// 물건 i - 끝점 거리 : [i][6]

pair<int, int> start;
pair<int, int> door;
vector<pair<int, int>> items;
vector<int> order;

int ans = 21e8;
int dx[] = { 1,0,-1,0 };
int dy[] = { 0,1,0,-1 };

int bfs(pair<int, int> start, pair<int, int> target) {
	queue<pair<int, int>> q;
	vector<vector<int>> tdistance(M, vector<int>(N, -1)); 
	q.push(start);
	tdistance[start.first][start.second] = 0;

	while (!q.empty()) {
		pair<int, int> now = q.front(); q.pop();

		if (now == target) {
			return tdistance[now.first][now.second];
		}

		for (int i = 0; i < 4; ++i) {
			int ny = now.first + dy[i];
			int nx = now.second + dx[i];
			if (ny >= 0 && ny < M && nx >= 0 && nx < N && house[ny][nx] != '#' && tdistance[ny][nx] == -1) {
				tdistance[ny][nx] = tdistance[now.first][now.second] + 1;
				q.push({ ny, nx });

				if (ny == target.first && nx == target.second) return tdistance[ny][nx];
			}
		}
	}
	return -1;
}

int main() { 
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);

	cin >> N >> M;

	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> house[i][j];
			if (house[i][j] == 'S') {
				start = { i, j };
			}
			else if (house[i][j] == 'E') {
				door = { i, j };
			}
			else if (house[i][j] == 'X') {
				items.push_back({ i, j });
			}
		}
	}
	
	if (items.size() == 0) {
		ans = bfs(start, door);
	}
	else {

		// 거리 계산
		for (int i = 1; i <= items.size(); ++i) {
			dist[i][0] = bfs(start, items[i - 1]);
			dist[i][6] = bfs(items[i - 1], door);

			for (int j = i + 1; j <= items.size(); ++j) {
				dist[i][j] = bfs(items[i - 1], items[j - 1]);
				dist[j][i] = dist[i][j];
			}
		}


		// 물건 줍는 순서를 만들어보자~~~
		for (int i = 0; i < items.size(); ++i) {
			order.push_back(i + 1);
		}

		do {
			int cur_dist = dist[order[0]][0];
			for (int i = 0; i < order.size() - 1; ++i) {
				cur_dist += dist[order[i]][order[i + 1]];
			}
			cur_dist += dist[order.back()][6];

			ans = min(ans, cur_dist);
		} while (next_permutation(order.begin(), order.end()));


	}

	cout << ans;

	return 0;
}

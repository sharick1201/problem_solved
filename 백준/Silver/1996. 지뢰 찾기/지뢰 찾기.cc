#include <iostream>
#include <vector>
using namespace std;
 
int N;
vector<vector<int>> map;

int dy[] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int dx[] = { -1, 0, 1, -1, 1, -1, 0, 1 };

int main() { 
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);

	cin >> N;

	map.assign(N, vector<int>(N, 0));

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			char input;
			cin >> input;

			if (input >= '1' && input <= '9') {
				map[i][j] = -1;
				for (int k = 0; k < 8; ++k) {
					int ny = i + dy[k];
					int nx = j + dx[k];
					if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;
					if (map[ny][nx] == -1) continue;
					map[ny][nx] += (int)(input - '0');

				}
			}
		}
	}

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			if (map[i][j] > 9) {
				cout << 'M';
			}
			else if (map[i][j] == -1) {
				cout << '*';
			}
			else {
				cout << map[i][j];
			}
		}
		cout << "\n";
	}
	
	return 0;
}

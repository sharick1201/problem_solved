#include <iostream>
#include <vector>
#include <cmath>
#include <climits>
using namespace std;

struct Coor {
	int y;
	int x;
};

int N, M;
vector<Coor> houses;
vector<Coor> chickens;
vector<vector<int>> housetochickdist;
vector<bool> selectedchickens;
int ans = 21e8;

int caldist(Coor house, Coor chicken) {
	return abs(house.y - chicken.y) + abs(house.x - chicken.x);
}

void calculateCityDistance() {
	int totalDistance = 0;

	// 각 집에 대해
	for (int i = 0; i < houses.size(); i++) {
		int minDist = 21e8;

		// 선택된 치킨집들 중 가장 가까운 거리 찾기
		for (int j = 0; j < chickens.size(); j++) {
			if (selectedchickens[j]) {
				minDist = min(minDist, housetochickdist[i][j]);
			}
		}
		totalDistance += minDist;
	}

	ans = min(ans, totalDistance);
}

void dfs(int depth, int start) { 
	// M개 다 선택했으면 계산 ㄱ
	if (depth == M) {
		calculateCityDistance();
		return;
	}

	// start부터 끝까지 탐색
	for (int i = start; i < chickens.size(); i++) {
		selectedchickens[i] = true;         
		dfs(depth + 1, i + 1);              
		selectedchickens[i] = false;         
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N >> M;

	int input;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> input;
			if (input == 1) {
				houses.push_back({ i, j });
			}
			else if (input == 2) {
				chickens.push_back({ i, j });
			}
		}
	}

	// 거리 테이블 크기 설정
	housetochickdist.resize(houses.size());
	selectedchickens.resize(chickens.size(), false);

	// 각 집에 대해, 각 치킨집들까지 가는 거리를 저장한다.
	for (int i = 0; i < houses.size(); i++) {
		for (int j = 0; j < chickens.size(); j++) {
			housetochickdist[i].push_back(caldist(houses[i], chickens[j]));
		}
	}

	// 조합 생성
	dfs(0, 0);

	cout << ans;

	return 0;
}

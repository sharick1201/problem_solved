#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

struct Difficulty {
	int tier_idx;
	int step;

	bool operator<(Difficulty other)const {
		if (tier_idx > other.tier_idx) return true;
		if (tier_idx < other.tier_idx) return false;
		if (tier_idx == other.tier_idx) {
			if (step < other.step) return true;
			if (step > other.step) return false;
		}
		return false;
	}
};

char tier[] = { 'B', 'S', 'G', 'P', 'D' };
int N;
string input;
priority_queue<Difficulty> pq;
vector<Difficulty> vect;
vector<Difficulty> ans;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	
	cin >> N;

	for (int i = 0; i < N; ++i) {
		cin >> input;
		int now_tier_idx = 0;
		int now_step;
		switch (input[0]) {
		case 'B': now_tier_idx = 0; break;
		case 'S': now_tier_idx = 1; break;
		case 'G': now_tier_idx = 2; break;
		case 'P': now_tier_idx = 3; break;
		case 'D': now_tier_idx = 4; break;
		}
		now_step = stoi(input.substr(1));

		pq.push({ now_tier_idx, now_step });
		vect.push_back({ now_tier_idx, now_step });
	}

	for (int i = 0; i < N; ++i) {
		Difficulty now = pq.top(); pq.pop();
		if (now.tier_idx != vect[i].tier_idx || now.step != vect[i].step) ans.push_back(now);
	}

	if (ans.empty()) {
		cout << "OK";
	}
	else {
		cout << "KO\n" << tier[ans[0].tier_idx] << ans[0].step << " " << tier[ans[1].tier_idx] << ans[1].step;
	}
	return 0;
}
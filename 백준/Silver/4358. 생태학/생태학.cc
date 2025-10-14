#include <iostream>
#include <string>
#include <map>
using namespace std;

string input;
map<string, int> trees; // 나무이름:빈도
int total = 0;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	
	while (getline(cin, input)) {
		trees[input]++;
		total++;
	}
	// map은 자동으로 키를 사전순으로 정렬하여 저장
	// map의 entry 타입은 pair<const Key, T>
	// entry.first는 나무 종 이름 (Key)
	// entry.second는 나무의 빈도 (Value)

	for (auto& entry : trees) {
		double percentage = (double(entry.second) / total) * 100;
		printf("%s %.4f\n", entry.first.c_str(), percentage);
	}
	return 0;
}
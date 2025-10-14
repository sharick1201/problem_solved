#include <iostream>
#include <string>
#include <map>
#include <iomanip>
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

	cout << fixed << setprecision(4); // 출력 형식 지정
	// fixed : 소수점 이하의 자리수를 고정(고정 소수점 형식)
	// setprecision : 출력할 소수점 이하의 자릿수를 설정
	
	for (auto& entry : trees) {
		double percentage = (double(entry.second) / total) * 100;
		cout << entry.first << " " << percentage << "\n";
	}
	return 0;
}
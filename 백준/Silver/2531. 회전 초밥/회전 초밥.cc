#include <iostream>
#include <algorithm>
using namespace std;

int N, d, k, c; // 접시 수, 초밥 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
int sushi[30'000];
int cnt[3'001]{ 0, }; // 현재 초밥 갯수
int ans = 0;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);

	// 입력
	cin >> N >> d >> k >> c;
	for (int i = 0; i < N; i++) {
		cin >> sushi[i];
	}

	int now = 0; // 지금 초밥 가짓수

	// 초기 윈도우 설정
	for (int i = 0; i < k; i++) {
		if (cnt[sushi[i]] == 0) now++;
		cnt[sushi[i]]++;
	}
	ans = now + (cnt[c] == 0 ? 1 : 0);

	// 연산
	for (int i = 0; i < N; i++) {
		// if (ans == k + 1) break; // 이미 가능한 최대값의 최대값이니까 볼장다봄

		// i번째 초밥 하나 지우고
		cnt[sushi[i % N]]--;
		if (cnt[sushi[i % N]] == 0) now--;

		// i+k번째 초밥 하나 추가
		if (cnt[sushi[(i + k) % N]] == 0) now++;
		cnt[sushi[(i + k) % N]]++;

		ans = max(ans, now + (cnt[c] == 0 ? 1 : 0)); // 최대값 업데이트
		// cnt[c] == 0 일 때 꽁짜초밥 처리를 now에 반영하면 윈도우 처리가 꼬인다는 걸 유의하자
	}

	// 출력
	cout << ans;
	return 0;
}
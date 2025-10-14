#include <iostream>
#include <string>
using namespace std;

int N;
string act;

int lever_pulled = 0; // 0: 안 당김, 1: A구역일 때 당김, 2: B구역일 때 당김
int area = 0; // 0: A, 1: B, 2: C
int ans = 0;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	
	cin >> N >> act;

	for (int i = 0; i < N; ++i) {

		if (act[i] == 'W') {
			if (area == 0) {
				area = 1;
			} else if (area == 1) { // 이제 마네킹이 깔림
				if (lever_pulled == 0) {
					ans = 5;
				}
				else if (lever_pulled == 1) {
					ans = 1;
				}
				else if (lever_pulled == 2) {
					ans = 6;
				}
				break;
			}
		}
		else if (act[i] == 'P') {
			if (lever_pulled == 0) {
				if (area == 0) {
					lever_pulled = 1;
				} else {
					// area B일 때
					lever_pulled = 2;
				}
			}
			else {
				if (area == 0) {
					lever_pulled = 0;
				}
				else {
					lever_pulled = 2; // B일때는 안 바뀜
				}
			}
		}
	}

	cout << ans;
	return 0;
}
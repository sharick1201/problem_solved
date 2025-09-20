#include <iostream>
#include <string>
#include <vector>
using namespace std;
// 완전탐색 + 비트마스킹
// 각 기타의 연주가능여부를 비트마스킹으로 표현해보자.
// 1개로 되는지 확인 -> 2개로 되는지 확인 -> ... -> n개로 되는지 확인한다.

// ㅁㅊ 모두 연주 불가하면 -1이 아니라 연주할 수 있는 곡이 아예 없으면 -1이고, 최대한 많이 연주 가능할 때 필요 기타수의 최솟값이엇음 ㅋㅋ

int N, M;
vector<unsigned long long> guitars;
int ans = -1; // 정답: 필요한 기타 최소 개수
int maxsong = 0; // 최대 연주 가능한 곡 수

unsigned long long convert(string s) {
    unsigned long long result = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'Y') result |= (1ULL << i);
    }
    return result;
}

void dfs(int idx, int cnt, unsigned long long mask) {
    if (idx == N) {
        int songcnt = __builtin_popcountll(mask);
        if (songcnt == 0) return; // 아무 곡도 못 치면 패스
        if (songcnt > maxsong) {
            maxsong = songcnt;
            ans = cnt;
        } else if (songcnt == maxsong && cnt < ans) {
            ans = cnt;
        }
        return;
    }
    dfs(idx + 1, cnt + 1, mask | guitars[idx]); // idx번째 기타 선택
    dfs(idx + 1, cnt, mask); // idx번째 기타 선택 안 함
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        string name, play;
        cin >> name >> play;
        guitars.push_back(convert(play));
    }

    dfs(0, 0, 0);

    cout << ans << '\n';
    return 0;
}

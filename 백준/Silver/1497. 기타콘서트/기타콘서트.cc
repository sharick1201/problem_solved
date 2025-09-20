#include <iostream>
#include <string>
#include <vector>
using namespace std;

// 완전탐색 + 비트마스킹
// 각 기타의 연주가능여부를 비트마스킹으로 표현해보자.
// 1개로 되는지 확인 -> 2개로 되는지 확인 -> ... -> n개로 되는지 확인한다.

// ㅁㅊ 모두 연주 불가하면 -1이 아니라 연주할 수 있는 곡이 아예 없으면 -1이고, 최대한 많이 연주 가능할 때 필요 기타수의 최솟값이엇음 ㅋㅋ

/////////////////////////////////////////////////////////////
// 비트마스크는
// 메모리 효율성이 대단히 좋고
// 초기화에 있어서... 배열은 싹 다 순회해야 하는 것에 반면, 비트마스크는 한 번이면 되고 ( = 0)
// 집합 연산이 매우 간단하며
// 상태 체크가 빠르다: 모두 true인지 보고싶은 상황에서, 배열 쓰면 0~n-1번째 전부 다 순회해서 확인해야 하는데 비트마스킹은 (1 << n)-1 이거 한 줄로 확인 가능

// 대신
// 가독성 안 좋고
// 숫자 하나로 표현하는 거기 때문에 디버깅이 어렵다
// int 쓰면 32비트 -> 32개만 상태체크 가능. long long 써도 64개까지만...

// 그래서
// 크기 작을 때 (보통 20개즈음)
// 집합 연산이 많을 때
// DP 상태압축 필요할 때
// 메모리 부족할 때
// 쓴다.
//////////////////////////////////////////////////////////////

int N, M;
vector<unsigned long long> guitars;
int ans = -1;
int maxsong = 0; // 최대 연주 가능한 갯수

// 문자열 -> 숫자
unsigned long long convert(string s) {
    unsigned long long result = 0;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'Y')
            result |= (1ULL << i); // 2^i 더함 (i번째 비트를 1로 만든다!!)
    }

    return result;
}

// mask: 현재 상태에서 가능한 곡들에 대한 비트마스크
// 각 기타에 대해 선택/비선택
void dfs(int idx, int cnt, unsigned long long mask) {
    if (idx == N) {
        int songcnt = __builtin_popcountll(mask); // 1인 비트의 개수 세줌(gcc 컴파일러 제공)
        if (songcnt == 0) return; // 아무 곡도 못 치면 패스

        if (songcnt > maxsong) { // 최대 가능한 곡 수 갱신
            maxsong = songcnt;
            ans = cnt;
        } else if (songcnt == maxsong && cnt < ans) {
            ans = cnt; // 최대 가능한 곡 수는 동일한데 필요 기타 수 적으면 정답 갱신
        }

        return;
    }

    // idx번째를 선택하는 경우
    dfs(idx + 1, cnt + 1, mask | guitars[idx]);
    // idx번째를 선택 X 경우
    dfs(idx + 1, cnt, mask);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        string name, play;
        cin >> name >> play; // name 필요없으니 버림
        guitars.push_back(convert(play));
    }

    dfs(0, 0, 0);

    if (maxsong == 0) ans = -1; // 아무 곡도 연주할 수 없으면 -1
    cout << ans;

    return 0;
}
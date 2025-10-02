#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<int> arr;
int ans[8];

void dfs(int now, int depth) {
    if (depth == M) {
        for (int i = 0; i < M; i++) {
            cout << ans[i] << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = now; i < arr.size(); i++) {
        ans[depth] = arr[i];
        dfs(i, depth + 1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;

    for (int i = 0; i < N; ++i) {
        int num;
        cin >> num;
        arr.push_back(num);
    }

    // 오름차순 정렬 후 중복값 제거
    sort(arr.begin(), arr.end());
    arr.erase(unique(arr.begin(), arr.end()), arr.end()); // unique는 쓰레기값의 첫번째 반환함

    dfs(0, 0);
    return 0;
}
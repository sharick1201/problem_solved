#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N, M;
vector<int> num;
int ans[8];

void dfs(int nowidx, int depth) {
    if (depth == M) {
        for (int i = 0; i < M; i++) {
            cout << ans[i] << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = nowidx; i < num.size(); i++) {
        ans[depth] = num[i];
        dfs(i, depth + 1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> N >> M;
    for (int i; i < N; i++) {
        int input;
        cin >> input;
        num.push_back(input);
    }
    sort(num.begin(), num.end());
    num.erase(unique(num.begin(), num.end()), num.end());

    dfs(0, 0);

    return 0;
}
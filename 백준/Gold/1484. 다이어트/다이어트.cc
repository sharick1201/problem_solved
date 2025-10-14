#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

int G;
vector<int> ans;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> G;

    for (int i = 1; i <= sqrt(G); ++i) {
        if (G % i == 0) {
            int a = i;
            int b = G / i; // b가 항상 더 큼

            // x랑 y가 정수가 되기 위해
            if ((b + a) % 2 == 0 && (b - a) % 2 == 0) {
                    int x = (b + a) / 2;
                    int y = (b - a) / 2;

                    // x, y가 음수만 아니면
                    if (x > 0 && y > 0)
                    {
                        ans.push_back(x);
                    }
                }
        }
    }

    if (ans.empty()) {
        cout << -1;
    } else {
        sort(ans.begin(), ans.end());
        for (int i = 0; i < ans.size(); ++i) {
            cout << ans[i] << "\n";
        }
    }

    return 0;
}


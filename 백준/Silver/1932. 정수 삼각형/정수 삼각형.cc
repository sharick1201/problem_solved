#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> triangle;
vector<vector<int>> dp; // 해당 위치에서의 최대값

int N;
int ans = 0;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> N;

    triangle.resize(N);
    dp.resize(N);

    for (int i = 0; i < N; ++i) {
        triangle[i].resize(i + 1);
        for (int j = 0; j <= i; ++j) {
            cin >> triangle[i][j];
        }
    }

    dp[0].resize(1);
    dp[0][0] = triangle[0][0];
    
    if (N == 1) {
        cout << dp[0][0];
        return 0;   
    }

    dp[1].resize(2);
    dp[1][0] = dp[0][0] + triangle[1][0];
    dp[1][1] = dp[0][0] + triangle[1][1];

    for (int i = 2; i < N; ++i) {
        dp[i].resize(i + 1);
        
        for (int j = 0; j <= i; ++j) {
            if (j == 0) {
                dp[i][j] = dp[i - 1][j] + triangle[i][j];
            } else if (j == i) {
                dp[i][j] = dp[i - 1][j -  1] + triangle[i][j];
            } else {
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j];
            }

            // 마지막 라인이면
            if (i == N-1) {
                ans = max(ans, dp[i][j]);
            }
        }
    }

    cout << ans;
    return 0;
}
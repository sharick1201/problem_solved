#include <iostream>
#include <vector>
using namespace std;

int N;
int arr[1'001];

int dp[1'001]; // i번째 원소를 마지막으로 하는 LIS의 길이
int ans = 0;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];

        int now = 0;
        for (int j = 0; j < i; ++j) {
            if (arr[i] > arr[j]) now = max(now, dp[j]);
        }
        dp[i] = now + 1; // 현재 원소를 포함한 LIS 길이
        ans = max(ans, dp[i]);
    }

    cout << ans;
    return 0;
}
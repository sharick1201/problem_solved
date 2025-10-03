#include <iostream>
using namespace std;

// 이딴거어케혼자생각해내서푸는건데;;ㅗㅗ

int N, K;
pair<int, int> jims[100]; // first: 무게, second: 가치
int dp[101][100'001];
// 첫번쨰 인덱스: 현재 고려 중인 물건의 개수, 두번째인덱스: 첫번쨰 인덱스값의 물건 개수를 고른 상태에서, 현재 배낭의 최대용량
// dp[i][j]: i개의 물건을 고려했을 때, 용량 j에서의 최대 가치

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> N >> K;

    for (int i = 0; i < N; ++i) {
        int weight, val;
        cin >> weight >> val;
        jims[i] = { weight, val };
    }

    for (int i = 0; i < N; ++i) { // 현재 고려중인 물건의 인덱스
        for (int j = 0; j <= K; ++j) { // 현재 배낭 용량

            if (jims[i].first <= j) { // 이 물건 배낭에 담을 수 있음?
                // 담을 수 있으면
                // 그 물건 선택할래말래
                dp[i+1][j] = max(dp[i][j],  // 현재 물건을 포함하지 않는 경우
                               dp[i][j - jims[i].first] + jims[i].second);
                               // 현재 물건을 포함하는 경우
                                // -> 현재 물건의 무게만큼을 빼고 남은 용량(DP 테이블 두번째 인덱스)에서,
                                // i-1개의 물건(DP 테이블 첫번째 인덱스) 으로 얻을 수 있는 최대 가치
            } else {
                dp[i+1][j] = dp[i][j]; // 못담음 ㅠㅠ
            }
        }
    }
    
    cout << dp[N][K];

    return 0;
}
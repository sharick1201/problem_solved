#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int T, C, V;
vector<int> hoobos; // 각 후보의 득표수
vector<vector<int>> vote; // vote[유권자][후보] = 선호도 순위

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> T;

    for (int t = 0; t < T; t++) {
        cin >> C >> V;
        
        // 벡터 크기 초기화
        hoobos.assign(C + 1, 0);
        vote.assign(V, vector<int>(C + 1, 0));

        // 입력받기
        for (int j = 0; j < V; j++) {
            for (int k = 0; k < C; k++) {
                int candidate;
                cin >> candidate;
                vote[j][candidate] = k; // k번째 선호도에 candidate 저장
                if (k == 0) { // 1순위 후보
                    hoobos[candidate]++;
                }
            }
        }

        // 1차 투표에서 최다 득표자 찾기
        int maxVotes = -1;
        int winner = 0;
        for (int i = 1; i <= C; i++) {
            if (hoobos[i] > maxVotes) {
                maxVotes = hoobos[i];
                winner = i;
            }
        }

        // 과반수 득표 확인
        if (maxVotes > V / 2) {
            cout << winner << " " << 1 << "\n";
        } else {
            // 2위 후보 찾기
            int secondMaxVotes = -1;
            int runnerUp = 0;
            for (int i = 1; i <= C; i++) {
                if (hoobos[i] > secondMaxVotes && hoobos[i] < maxVotes) {
                    secondMaxVotes = hoobos[i];
                    runnerUp = i;
                } else if (hoobos[i] == maxVotes && i != winner) {
                    // 동점인 경우 처리
                    runnerUp = i;
                    secondMaxVotes = hoobos[i];
                }
            }

            // 2차 투표 (결선투표)
            int winnerVotes = 0, runnerUpVotes = 0;
            for (int j = 0; j < V; j++) {
                // 각 유권자의 선호도에서 winner와 runnerUp 중 누가 더 선호되는지 확인
                if (vote[j][winner] < vote[j][runnerUp]) {
                    // 선호도가 낮을수록 더 선호함 (0이 1순위)
                    winnerVotes++;
                } else {
                    runnerUpVotes++;
                }
            }
            
            // 결선투표 승자 결정
            int finalWinner = (winnerVotes > runnerUpVotes) ? winner : runnerUp;
            cout << finalWinner << " " << 2 << "\n";
        }
    }
    return 0;
}

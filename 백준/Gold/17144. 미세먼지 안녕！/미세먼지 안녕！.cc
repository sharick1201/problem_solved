#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int room[50][50];
int nextroom[50][50]; // 먼지 확산은 동시에 일어나므로, 업데이트될 값을 여기 저장해두고 한꺼번에 갱신한다.

int R, C, T;
vector<pair<int, int>> mech; // 공청기

int ans = 0; 

// 미세먼지 확산
void munji() {

    int ydir[] = {-1, 1, 0, 0};
    int xdir[] = {0, 0, -1, 1};

    // nextroom 죄다 0으로 초기화해두고 ㄱㄱ
    // 시뮬돌리면서 동시에 초기화하면 상하좌우업데이트값이 꼬이니까 미리 해두셈
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            nextroom[i][j] = 0;
        }
    }
    // 시뮬
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (room[i][j] > 0) { // 공청기도 아니고 빈칸도 아니면(=먼지가 있으면)
                
                int cnt = 0; // 남은 미세먼지 양 계산을 위해 몇 칸에 확산됐는지 카운트
                int munjipart = room[i][j] / 5;

                for (int k = 0; k < 4; k++) {
                    int ny = i + ydir[k];
                    int nx = j + xdir[k];

                    if (ny < 0 || nx < 0 || ny >= R || nx >= C) continue;
                    if (room[ny][nx] == -1) continue; 
                    cnt++;
                    nextroom[ny][nx] += munjipart;
                }
                nextroom[i][j] -= munjipart * cnt; // 남은 미세먼지 양
            }
        }
    }
}

// 확산된 미세먼지 상태 갱신
void nowroomstatus() {
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            room[i][j] += nextroom[i][j];
        }
    }
}

// 공기청정기 윗부분 바람 (반시계방향)
void mechwork1()
{
    int my = mech[0].first;
    int mx = mech[0].second;

    // 1. 왼쪽 변: 아래에서 위로 당김
    for (int i = my - 1; i > 0; i--)
    {
        room[i][0] = room[i - 1][0];
    }

    // 2. 위쪽 변: 오른쪽에서 왼쪽으로 당김
    for (int j = 0; j < C - 1; j++)
    {
        room[0][j] = room[0][j + 1];
    }

    // 3. 오른쪽 변: 위에서 아래로 당김
    for (int i = 0; i < my; i++)
    {
        room[i][C - 1] = room[i + 1][C - 1];
    }

    // 4. 아래쪽 변 (공청기 행): 왼쪽에서 오른쪽으로 당김
    for (int j = C - 1; j > mx + 1; j--)
    {
        room[my][j] = room[my][j - 1];
    }

    // 공기청정기에서 나오는 바람
    room[my][mx + 1] = 0;
}

// 공기청정기 아랫부분 바람 (시계방향)
void mechwork2()
{
    int my = mech[1].first;
    int mx = mech[1].second;

    // 1. 왼쪽 변: 위에서 아래로 당김
    for (int i = my + 1; i < R - 1; i++)
    {
        room[i][0] = room[i + 1][0];
    }

    // 2. 아래쪽 변: 오른쪽에서 왼쪽으로 당김
    for (int j = 0; j < C - 1; j++)
    {
        room[R - 1][j] = room[R - 1][j + 1];
    }

    // 3. 오른쪽 변: 아래에서 위로 당김
    for (int i = R - 1; i > my; i--)
    {
        room[i][C - 1] = room[i - 1][C - 1];
    }

    // 4. 위쪽 변 (공청기 행): 왼쪽에서 오른쪽으로 당김
    for (int j = C - 1; j > mx + 1; j--)
    {
        room[my][j] = room[my][j - 1];
    }

    // 공기청정기에서 나오는 바람
    room[my][mx + 1] = 0;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    // 입력
    cin >> R >> C >> T;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> room[i][j];
            if (room[i][j] == -1) mech.push_back({i, j});
        }
    }
    
    // 연산
    for (int i = 0; i < T; i++) {
        munji();
        nowroomstatus();

        mechwork1();
        mechwork2();
    }

    // 출력
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (room[i][j] > 0) {
                ans += room[i][j];
            }
        }
    }
    cout << ans;
    
    return 0;
}
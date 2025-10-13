#include <iostream>
#include <algorithm>
using namespace std;

// 개어렵네ㅁㅊ

int K;
// ㄱ자이니까 변의 갯수는 항상 6
pair<int, int> arr[6]; // 방향, 길이
int extnt = 0;

// 각 방향별 최대 길이를 찾자
int max_width = 0;
int max_height = 0;
int max_width_idx = -1;
int max_height_idx = -1;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> K;

    for (int i = 0; i < 6; ++i) {
        cin >> arr[i].first >> arr[i].second;
    }

    for (int i = 0; i < 6; ++i) {
        // 가로
        if (arr[i].first == 1 || arr[i].first == 2)
        {
            if (arr[i].second > max_width) {
                max_width = arr[i].second;
                max_width_idx = i;
            }
        } else {
            // 세로
            if (arr[i].second > max_height) {
                max_height = arr[i].second;
                max_height_idx = i;
            }
        }
    }

    // 큰 직사각형 면적
    int big_rect = max_width * max_height;

    // 작은 직사각형의 가로와 세로
    // 최대 가로의 양 옆 변 중 작은 것
    int small_width = arr[(max_height_idx + 3) % 6].second;
    // 최대 세로의 양 옆 변 중 작은 것
    int small_height = arr[(max_width_idx + 3) % 6].second;

    // 작은 직사각형 면적
    int small_rect = small_width * small_height;

    int area = big_rect - small_rect;

    cout << area * K;

    return 0;
}


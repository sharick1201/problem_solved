#include <iostream>
#include <algorithm>
using namespace std;

int N, K;
int arr[100'000];
int ptr1, ptr2;
int sum = 0;
int ans = -200'000'000;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> N >> K;

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    // 초기값
    for (int i = 0; i < K; i++) {
        sum += arr[i];
    }
    ans = sum;

    // 투포인터로 확인
    int ptr1 = 0;
    int ptr2 = K;

    while (1) {
        if (ptr2 == N) break;
        sum -= arr[ptr1];
        sum += arr[ptr2];
        ans = max(ans, sum);
        ptr1++; ptr2++;
    }
    
    cout << ans;

    return 0;
}
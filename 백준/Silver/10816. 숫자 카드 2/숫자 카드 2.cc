#include <iostream>
#include <algorithm>
using namespace std;

int N;
int arr[500'001];
int M;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }
    sort(arr, arr + N);
    
    cin >> M;
    for (int i = 0; i < M; ++i) {
        int tar;
        cin >> tar;
        cout << upper_bound(arr, arr+N, tar) - lower_bound(arr, arr+N, tar) << " ";
    }
    return 0;
}
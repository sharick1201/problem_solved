#include <iostream>
#include <algorithm>
using namespace std;

int N;
int arr[500'001];
int M;

int lower_idx(int target) {
    int st = 0;
    int en = N;
    int mid; 
    while (st < en) {
        mid = (st + en) / 2;
        if (arr[mid] >= target) en = mid;
        else st = mid + 1;
    }
    
    return st;
}

int upper_idx(int target) {
    int st = 0;
    int en = N;
    int mid; 
    while (st < en) {
        mid = (st + en) / 2;
        if (arr[mid] > target) en = mid;
        else st = mid + 1;
    }
    
    return st;
}

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
        cout << upper_idx(tar) - lower_idx(tar) << " ";
    }
    return 0;
}
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int n;
int origin[1'000'000];
vector<int> sorted;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> origin[i];
        sorted.push_back(origin[i]);
    }

    sort(sorted.begin(), sorted.end());
    // unique: 중복된 원소는 다 뒤로 미뤄두고, 중복값들의 시작 인덱스 뱉는다.
    sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());

   
    for (int i = 0; i < n; i++) {
        cout << lower_bound(sorted.begin(), sorted.end(), origin[i]) - sorted.begin() << " ";
    }


    return 0;
}

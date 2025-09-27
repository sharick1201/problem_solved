#include <iostream>
#include <algorithm>
using namespace std;

int N;
long long maxprofit = 0;
long long minprice = 1e9;
long long a;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> a;
        minprice = min(minprice, a);
        maxprofit = max(maxprofit, a - minprice);
    }
    cout << maxprofit;

    return 0;
}

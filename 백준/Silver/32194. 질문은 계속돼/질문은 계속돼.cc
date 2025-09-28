#include <iostream>
#include <vector>
#include <string>
using namespace std;

int N;
int sum[200002]; // i번째 질문까지의 yes의 개수

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N;
    sum[1] = 1;

    for (int i = 2; i <= N+1; i++) { 
        int type, x, y;
        cin >> type >> x >> y;

        int count = sum[y] - sum[x - 1];

        if (type == 1) { 
            if (count == (y - x + 1))
            {
                cout << "Yes\n";
                sum[i] = sum[i-1] + 1;
            }
            else
            {
                cout << "No\n";
                sum[i] = sum[i - 1];
            }
        } else {

            if (count == 0)
            {
                cout << "Yes\n";
                sum[i] = sum[i - 1] + 1;
            }
            else
            {
                cout <<"No\n";
                sum[i] = sum[i - 1];
            }
        }
    }

    return 0;
}

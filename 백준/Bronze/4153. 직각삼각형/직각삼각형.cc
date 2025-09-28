#include <iostream>
#include <algorithm>
using namespace std;

int sides[3];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    while (true) {
        cin >> sides[0] >> sides[1] >> sides[2];
        if (sides[0] == 0 && sides[1] == 0 && sides[2] == 0) break;
  
        sort(sides, sides + 3); // 제일 긴 거 뒤로 오게
        
        if (sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2]) {
            cout << "right\n";
        } else {
            cout << "wrong\n";
        }
    }

    return 0;
}

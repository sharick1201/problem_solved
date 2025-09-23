#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int cnt = 1;

    while (1) {
        int L, P, V;
        cin >> L >> P >> V;

        if (L == 0 && P == 0 && V == 0) break;
        int use = V / P; // p로 나눈 결과물만큼 L일동안 풀로 쉴 수 있다.
        int rem = V % P;
        
        if (L < rem) rem = L; // 8일 중 3일 사용가능하다면 나머지가 3. rem = 4 이면... 4일 쉬어버리면 29일 쉬는 거라 안됨

        cout << "Case " << cnt++ << ": " << L * use + rem << "\n";
    }
    return 0;
}

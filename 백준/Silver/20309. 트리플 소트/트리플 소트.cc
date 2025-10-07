#include <iostream>
using namespace std;

int N;
int input;
bool flag = true;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    // 홀수번 인덱스의 원소는 홀수번 원소끼리만 스왑 가능(짝수도)
    // 홀수번에는 홀수만, 짝수번에는 짝수만 있어야함

    cin >> N;

    for (int i = 1; i <= N; i++) {
        cin >> input;
        if (i % 2 != input % 2) {
            flag = false;
            break;
        }
    }

    cout << (flag ? "YES" : "NO");
    return 0;
}
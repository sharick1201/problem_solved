#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int a, b;
    // 입력값이 몇번 들어올지 모른다면 이렇게 while 안에 cin 넣어서 해결 가능
    while (cin >> a >> b)  {
        cout << a + b << "\n";
    }
    
    return 0;
}

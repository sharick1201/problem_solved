#include <iostream>
using namespace std;

int N;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> N;
    for (int i = 1; i <= 9; i++) {
        cout << N << " * " << i << " = " << N * i << "\n";
    }
    
    return 0;
}

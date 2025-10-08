#include <iostream>
#include <string>
using namespace std;

string input;
int idx;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> input >> idx;

    cout << input[idx-1];
    return 0;
}

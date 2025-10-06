#include <iostream>
using namespace std;
int n1, n2;

int gcd(int a, int b) {
    // gcd(a, b) = gcd(b, a mod b)
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int lcm(int a, int b) {
    return a / gcd(a,b) * b; 
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n1 >> n2;

    cout << gcd(n1, n2) << "\n";
    cout << lcm(n1, n2);

    return 0;
}
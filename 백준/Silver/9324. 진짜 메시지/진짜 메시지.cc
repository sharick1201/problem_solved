#include <iostream>
#include <string>
using namespace std;

int T;
string input;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> T;

    for (int t = 0; t < T; t++) {
        bool isReal = true;
        int alphab[26] ={0, };
        cin >> input;

        for (int i = 0; i < input.length(); i++) {
            alphab[input[i] - 'A']++;
            if (alphab[input[i] - 'A'] == 3) {
                if (input[i] != input[i + 1]) {
                    isReal = false;
                    break;
                } else {
                    alphab[input[i] - 'A'] = 0;
                    i++;
                }
            }
        }

        cout << (isReal ? "OK\n" : "FAKE\n");
        
    }
    return 0;
}
#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_set>
#include <string>
using namespace std;

int TC;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> TC;

    cin.ignore(); // 개행 문자 제거

    for (int t = 0; t < TC; t++)
    {
        string soundline;
        getline(cin, soundline); // 한 줄 받아온다.

        // 순서 유지를 위해 소리들을 벡터에 저장
        vector<string> sounds;
        stringstream ss(soundline);
        string word;

        // stringstream 쓰면 공백으로 자동 분리됨
        while (ss >> word) {
            sounds.push_back(word);
        }

        // 여우 소리가 아닌 동물 소리 저장할 set
        unordered_set<string> notfoxsounds;

        string inputline;
        while (getline(cin, inputline))
        {
            if (inputline == "what does the fox say?") break;

            // 마지막 단어(동물 소리) 추출
            string animalsound = inputline.substr(inputline.rfind(' ') + 1);
            notfoxsounds.insert(animalsound);
        }

        // 여우 소리만
        for (int i = 0; i < sounds.size(); i++) {
            // 비-여우 소리 셋에 없으면 여우소리임
            if (notfoxsounds.count(sounds[i]) == 0) {
                cout << sounds[i] << " ";
            }
        }
        cout << "\n";
    }
    return 0;
}
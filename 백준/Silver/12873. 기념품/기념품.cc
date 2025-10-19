#include <iostream>
#include <vector>
using namespace std;

int N;
vector<int> people;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N;

    for (int i = 0; i < N; ++i)
    {
        people.push_back(i + 1);
    }

    long long t = 1;      // 단계
    int curidx = 0; // 현재 인덱스

    while (people.size() > 1)
    {
        // t * t * t - 1만큼 이동
        // 5000 ^ 3 까지 가능이니 long long 으로 해줘야됨........
        long long steps = t * t * t - 1;
        curidx = (curidx + steps) % people.size(); // 주의: 사람 수가 달라지므로 N 쓰면 안돼
        // t * t * t번째 사람 나가
        people.erase(people.begin() + curidx);
        if (curidx >= people.size()) curidx = 0; // 바로 윗줄에서 제거 후 curidx는 그 다음 인덱스를 지시하므로, 마지막 idx에 해당하는 값을 지웠으면 curidx가 요상한 곳을 지시하게 됨
        t++; // 다음 단계
    }

    cout << people[0];
    return 0;
}
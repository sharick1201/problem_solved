#include <iostream>
#include <string>
#include <sstream>
#include <bitset>
#include <vector>
using namespace std;

int N;
vector<bitset<8>> IPaddresses[1001]; // 8자리 이진수를 원소로 갖는 벡터... 들을 원소로 갖는 배열
bitset<8> compare[4];

// 비트셋 -> 10진수
int bitsettoint(bitset<8> bits) {
    return static_cast<int>(bits.to_ulong());
}

// 첫 번째로 차이가 발생하는 지점 찾기
int findfirstdifferencebit() {

    for (int i = 0; i < 4; i++)
    {
        if (compare[i].any())
        { // any: 이 비트셋에 1인 비트가 하나라도 있나요
            // bitset의 인덱싱은 역순이다 헐퀴~ 역순으로 표현크기가 커지니까인듯
            for (int bit = 7; bit >= 0; bit--)
            {
                if (compare[i][bit])
                    return (i * 8) + (7 - bit);
            }
        }
    }
    return 32; // 모두 같다
}

// 네트워크 주소 출력
void printnetworkaddress(int prefixlength) {
    for (int i = 0; i < 4; i++) {
        bitset<8> networkoctet = IPaddresses[0][i];

        int octetstartbit = i * 8;

        for (int bit = 0; bit < 8; bit++) {
            int globalbitpos = octetstartbit + (7 - bit);
            if (globalbitpos >= prefixlength) networkoctet[bit] = 0;
        }

        cout << bitsettoint(networkoctet);
        if (i < 3) cout << ".";
    }
}

// 네트워크 마스크 출력
void printnetworkmask(int prefixlength) {
    for (int octet = 0; octet < 4; octet++) {
        bitset<8> maskoctet;

        int octetstartbit = octet * 8;

        for (int bit = 0; bit < 8; bit++) {
            int globalbitpos = octetstartbit + (7 - bit);
            if (globalbitpos < prefixlength) {
                maskoctet[bit] = 1;
            } else {
                maskoctet[bit] = 0;
            }
        }

        cout << bitsettoint(maskoctet);
        if (octet < 3) cout << ".";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // compare 초기화
    for (int j = 0; j < 4; j++)
    {
        compare[j] = bitset<8>(0);
    }

    // 입력받는다.
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        // 십진수를 받아온다. . 기준으로 split하고, split한 거 이진수 비트마스킹으로 변환해서 저장
        string input;
        cin >> input;

        // stringstream을 사용할 때, 공백 대신 다른 문자를 기준으로 나누고 싶으면, 아래와 같이 while문 작성
        char delimiter = '.';
        stringstream ss(input);

        string splitedinput;
        while (getline(ss, splitedinput, delimiter))
        {
            IPaddresses[i].push_back(bitset<8>(stoi(splitedinput))); // 10진수 -> 2진수
        }

        // XOR 연산한다. 왜? 이 다음에 첫 번째로 차이가 발생하는 비트의 위치를 찾기 위해서
        if (i != 0)
        {
            for (int j = 0; j < 4; j++)
            {
                // compare[j] 가 이미 1이면 1 유지함 | 새 차이 발견하면 1 갱신
                // 근데 이러면 0 또는 1이 되는 거 아잉교?! => bitset끼리 연산하면 비트별로 연산이 된다 와웅 개꿀
                // 근데 왜 0이랑만 비교하냐? 어차피 첫 번째 차이를 발견하기만 하면 되기 때문에(이행성)
                // 일부 차이점을 놓쳐도 더 보수적으로 잡는 거라 ㄱㅊ
                compare[j] = compare[j] | (IPaddresses[0][j] ^ IPaddresses[i][j]);
            }
        }
    }

    // 첫 번째로 차이가 발생하는 지점 찾기
    int firstdiffidx = findfirstdifferencebit();

    // 출력
    printnetworkaddress(firstdiffidx);
    cout << "\n";
    printnetworkmask(firstdiffidx);

    return 0;
}

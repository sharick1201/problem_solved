#include <iostream>
#include <vector>  
using namespace std;

int main() {
    int N; // 풍선 갯수
    cin >> N;

    vector<int> arr(N); // 풍선 속 종이에 적힌 숫자들 저장
    vector<bool> popped(N, false); // 터진 풍선 체크

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }


    int idx = 0;

    for (int rep = 0; rep < N; rep++) {
        cout << idx + 1 << " ";
        int move = arr[idx];
        popped[idx] = true;

        if (rep == N - 1) break; // 마지막 풍선일 시 종료


        if (move > 0) {
            for (int i = 0; i < move; i++) { // move가 3이라면
                do {
                    idx = (idx + 1) % N; // 각 반복마다 일단 한 칸씩 이동하고, 터진 풍선이라면 한 칸씩 더이동
                } while (popped[idx]);
            }
        }
        else {
            for (int i = 0; i < -move; i++) {
                do {
                    idx = (idx - 1 + N) % N; 
                } while (popped[idx]);
            }
        }
    }

    return 0;
}

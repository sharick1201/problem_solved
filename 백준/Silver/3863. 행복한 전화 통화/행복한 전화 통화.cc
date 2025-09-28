#include <iostream>
#include <vector>
using namespace std;

int N, M;
vector<pair<int, int>> calls;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    while (true)
    {
        calls.clear();
        cin >> N >> M;

        if (N == 0 && M == 0) break;

        for (int i = 0; i < N; i++)
        {
            int source, dest, start, dur;
            cin >> source >> dest >> start >> dur;
            calls.push_back({start, start + dur});
        }

        for (int i = 0; i < M; i++)
        {
            int qstart, qdur;
            cin >> qstart >> qdur;
            int querye = qstart + qdur;

            int count = 0;

            for (const auto &call : calls)
            {
                int callst = call.first;
                int callen = call.second;

                if (callst < querye && callen > qstart)
                {
                    count++;
                }
            }
            cout << count << "\n";
        }
    }
        return 0;
    }
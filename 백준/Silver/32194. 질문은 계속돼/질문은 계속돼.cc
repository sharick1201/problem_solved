#include <iostream>
#include <vector>

using namespace std;

int n;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;

    vector<int> yes(n + 2, 0); 
    vector<int> no(n + 2, 0); 

    yes[1] = 1;

    int type, x, y;
    for (int i = 2; i <= n + 1; i++)
    {
        cin >> type >> x >> y;

        if (type == 1)
        {
            if ((yes[y] - yes[x - 1]) == (y - x + 1))
            { 
                cout << "Yes\n";
                yes[i] = yes[i - 1] + 1;
                no[i] = no[i - 1];
            }
            else
            {
                cout << "No\n";
                no[i] = no[i - 1] + 1;
                yes[i] = yes[i - 1];
            }
        }
        else if (type == 2)
        {
            if ((no[y] - no[x - 1]) == (y - x + 1))
            { 
                cout << "Yes\n";
                yes[i] = yes[i - 1] + 1;
                no[i] = no[i - 1];
            }
            else
            {
                cout << "No\n";
                no[i] = no[i - 1] + 1;
                yes[i] = yes[i - 1];
            }
        }
    }

    return 0;
}
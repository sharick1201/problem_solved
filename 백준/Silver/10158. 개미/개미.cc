#include <iostream>
using namespace std;

int main()
{
    int w, h, p, q, t;
    cin >> w >> h >> p >> q >> t;
    
    // x축 계산
    int x_pos = (p + t) % (2 * w);
    if (x_pos > w) {
        x_pos = 2 * w - x_pos;
    }
    
    // y축 계산  
    int y_pos = (q + t) % (2 * h);
    if (y_pos > h) {
        y_pos = 2 * h - y_pos;
    }
    
    cout << x_pos << " " << y_pos;
    
    return 0;
}
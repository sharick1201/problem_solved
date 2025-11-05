#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int temp_ans = 0;

void dfs(int depth, int now, vector<int>& numbers, int target) {
    if (depth == numbers.size()) {
        if (now == target) temp_ans++;
        return;
    }
    
    dfs(depth+1, now - numbers[depth], numbers, target);
    dfs(depth+1, now + numbers[depth], numbers, target);
}


int solution(vector<int> numbers, int target) {
    // 가능한 모든 순열을 얻고 싶으면 next_permutation 전에 오름차순으로 정렬해줘야 한다.
    sort(numbers.begin(), numbers.end());
    
    dfs(0, 0, numbers, target);
    
    int answer = temp_ans;
    
    return answer;    
}
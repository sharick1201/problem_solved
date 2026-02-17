N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

INF = 10**9
answer = INF

# 첫 집 색깔별로 시작하는 경우 3번 반복
for start_color in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    
    # 첫 집 색깔 정하기
    for color in range(3):
        if color == start_color:
            dp[0][color] = arr[0][color]
        else:
            dp[0][color] = INF

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

    # 마지막 집 색깔이 시작 집과 달라야 함
    for end_color in range(3):
        if end_color != start_color:
            answer = min(answer, dp[N - 1][end_color])

print(answer)

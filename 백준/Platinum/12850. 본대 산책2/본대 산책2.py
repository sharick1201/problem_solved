"""
정보과학관에서 출발해서 본대산책

한 건물에서 다른 인접한 건물로 이동하는데 1분
산책 도중에 한 번도 길이나 건물에 멈춰서 머무르지 않는다.
D 분만 산책할 거임 -> 산책한지 D분 됐을 때, 정보과학관에 도착해야된다.
가능한 경로의 경우의 수

D가 존나큼 / 시간제한 1초

출력: 가능한 경로의 수를 1,000,000,007로 나눈 나머지

DP[d][i][j] : i -> j 갈 때, d번만에 가는 경우의 수

인접행렬 거듭제곱... 인데 분할거듭제곱
인접행렬을 d제곱한 행렬 = DP[d]

개어렵네
"""
MOD = 1000000007

# 행렬의 곱
def mat_multiply(A, B):
    res = [[0] * 8 for _ in range(8)]

    # A * B 행렬곱
    for i in range(8):
        for j in range(8):
            element = 0
            for k in range(8):
                element += (A[i][k] * B[k][j]) % MOD
            res[i][j] = element % MOD

    return res


# 행렬의 거듭제곱
def mat_pow(power, adj_mat):
    res = [[0] * 8 for _ in range(8)]   # identity mat (어떤 행렬을 곱해도 자기자신을 반환)
    for i in range(8):
        res[i][i] = 1

    # 그냥 막 곱하지 않고, 분할 거듭제곱
    while power:

        # 홀수면
        # mat ^ N = mat ^ (N // 2) * mat ^ (N // 2) + >>> mat <<<
        if power % 2 == 1:
            res = mat_multiply(res, adj_mat)

        # mat ^ N = mat ^ (N // 2) * mat ^ (N // 2)
        adj_mat = mat_multiply(adj_mat, adj_mat)
        power //= 2

    return res[0][0]

"""
0: 정보과학관
1: 전산관
2: 미래관
3: 신양관
4: 한경직기념관
5: 진리관
6: 학생회관
7: 형남과학관
"""
adj_mat = [[0, 1, 1, 0, 0, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 0],
           [1, 1, 0, 1, 1, 0, 0, 0],
           [0, 1, 1, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 1],
           [0, 0, 0, 1, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 1, 0, 1, 0]]

D = int(input())
print(mat_pow(D, adj_mat))
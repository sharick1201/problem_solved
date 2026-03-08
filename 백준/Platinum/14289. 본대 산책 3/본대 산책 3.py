MOD = 1000000007

# 행렬의 곱
def mat_multiply(A, B):
    res = [[0] * V for _ in range(V)]

    # A * B 행렬곱
    for i in range(V):
        for j in range(V):
            element = 0
            for k in range(V):
                element += (A[i][k] * B[k][j]) % MOD
            res[i][j] = element % MOD

    return res


# 행렬의 거듭제곱
def mat_pow(power, adj_mat):
    res = [[0] * V for _ in range(V)]   # identity mat (어떤 행렬을 곱해도 자기자신을 반환)
    for i in range(V):
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
"""

V, E = map(int, input().split())
adj_mat = [[0] * V for _ in range(V)]

for _ in range(E):
    v1, v2 = map(int, input().split())
    adj_mat[v1-1][v2-1] = 1
    adj_mat[v2-1][v1-1] = 1

D = int(input())

print(mat_pow(D, adj_mat))
def backtracking(N, M, seq):
    if len(seq) == M:
        print(*seq)
        return

    for i in range(1, N + 1):
        seq.append(i)
        backtracking(N, M, seq)
        seq.pop()

N, M = map(int, input().split())
backtracking(N, M, [])
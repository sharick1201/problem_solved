def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

T = int(input())
results = []

for _ in range(T):
    N, M = map(int, input().split())
    # 조합 수 계산
    result = combinations(M, N)
    results.append(result)

for r in results:
    print(r)

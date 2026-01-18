# 행렬 크기 N과 M 입력받
N, M = map(int, input().split())

# 행렬 A와 B를 저장할 리스트를 초기화
A = []
B = []

# 행렬 A의 원소를 입력받
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 행렬 B의 원소를 입력받
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 C를 초기화하고 A + B의 합을 계산
C = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])  # A와 B의 같은 위치의 원소를 더한다
    C.append(row)

# 결과를 출력합니다.
for row in C:
    print(" ".join(map(str, row)))  # 각 행을 공백으로 구분하여 출력

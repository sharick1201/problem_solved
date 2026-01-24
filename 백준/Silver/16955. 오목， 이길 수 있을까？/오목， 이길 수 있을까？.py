# 이길 수 있을지 구한다
# -> 돌을 하나 더 두었을 때 연속한 5개 이상의 돌이 존재할 수 있는지 확인한다
# "연속한" 5개의 돌이 존재해야 이길 수 있으니까, 모든 바둑판 칸에 돌을 두어보는 대신,
# 구사과의 돌(X)에 인접한 상,하,좌,우, 좌하향대각선, 우하향대각선, 좌상향대각선, 우상향대각선 1칸씩만 확인해본다
# 어떻게? dx, dy 배열을 사용함으로써

# 모든 바둑판 칸에 대해서 순회하는데,
# 구사과의 칸에 도달했을 때만, 연속한 5개의 돌이 성립하는지 확인해본다.

# 인접한 칸에 돌을 둘 때, 조심해야 할 포인트
# 1. 바둑판 바깥에 돌을 둘 수는 없다 -> index out of range 조심하여 범위 체크하는 로직 추가
# 2. 큐브러버(O)가 이미 돌을 둔 곳에 돌을 덮어씌울 수는 없다 -> 이 부분도 체크하는 로직 추가
# 3. XX.XX 와 같은 경우, 반대쪽 방향도 모두 체크 후 5개인지 확인해야 함
# 4. 돌을 두고 체크 다 해본 뒤에, 그 자리에 뒀던 돌을 다시 회수해야 한다.

#바둑판은 10x10

dy = [-1, 1, 0, 0, 1, 1, -1, -1] # 상, 하, 좌, 우, 좌하향대각선, 우하향대각선, 좌상향대각선, 우상향대각선 순서
dx = [0, 0, -1, 1, -1, 1, -1, 1]

arr = [list(input()) for _ in range(10)] # 문자열 자체는 불변이라 수정이 안 됨. list로 감싸주자

ans = 0 # 이중포문 다 돌았는데 이길 수 있는 케이스가 없어서 ans = 1로 되는 조건문 진입 안하면 자연스럽게 안 되는 것임 -> 초기값 0

for i in range(10):
    for j in range(10):
        if arr[i][j] == 'X':

            for k in range(8):

                ny = i + dy[k]
                nx = j + dx[k]

                if 0 <= ny < 10 and 0 <= nx < 10 and arr[ny][nx] == '.': # 이미 X인 칸에 추가로 둘 순 없으니까

                    # 인접한 각 칸들에 돌을 하나 더 두어본다
                    arr[ny][nx] = 'X'
                    dol = 2   # 발견한 돌 하나, 내가 새로 둔 돌 하나 -> 총 2개 카운트가 이미 됨

                    # 그 대해서 체크(그럼 3번만 더 하면 총 5번 확인가능하죵)

                    for l in range(1, 4):
                        furthery = ny + dy[k] * l
                        furtherx = nx + dx[k] * l

                        if 0 <= furthery < 10 and 0 <= furtherx < 10 and arr[furthery][furtherx] == 'X':
                            dol += 1
                        else:
                            break # 이미 글러먹었으니까 더 볼 필요 없다

                    # 반대 방향 체크 (총 5개를 만들기 위해)
                    for l in range(1, 4):
                        furthery = i - dy[k] * l
                        furtherx = j - dx[k] * l

                        if 0 <= furthery < 10 and 0 <= furtherx < 10 and arr[furthery][furtherx] == 'X':
                            dol += 1
                        else:
                            break


                    if dol >= 5:
                        ans = 1
                        break

                    # 원상복구
                    arr[ny][nx] = '.'
        if ans == 1:
            break
    if ans == 1:
        break

print(ans)
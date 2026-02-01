# -1로 추가적으로 append하지말고 걍 수학적으로 접근하자

M, N = map(int, input().split())

cutnum = int(input())

ans = 0 # 가장 큰 종이조각 넓이

lines_v = [0, M]  # 수직
lines_h = [0, N]  # 수평

for _ in range(cutnum):
    bh, line = map(int, input().split())
    if bh == 0:
        lines_h.append(line)
    else:
        lines_v.append(line)

lines_v.sort()
lines_h.sort()

for i in range(len(lines_v) - 1):
    for j in range(len(lines_h) - 1):
        garo = lines_h[j+1] - lines_h[j]
        sero = lines_v[i+1] - lines_v[i]
        ans = max(ans, garo * sero)
print(ans)